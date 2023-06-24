import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def hotelRecom():
    df = pd.read_csv('Hotel.csv', encoding='unicode_escape')
    location = input("Enter your preferred location: ")
    room_price = float(input("Enter your preferred room price: "))  # Convert input to float
    df['Room Price'] = df['Room Price'].str.replace('$', '', regex=True).str.strip()
    df['Room Price'] = pd.to_numeric(df['Room Price'], errors='coerce')
    filtered_df = df[(df['Location'] == location) & (df['Room Price'] <= room_price)].reset_index(drop=True)
    if len(filtered_df) > 0:
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(filtered_df['Hotel Name'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        indices = pd.Series(filtered_df.index, index=filtered_df['Hotel Name']).drop_duplicates()
        chosen_hotel_index = 0
        similarity_scores = list(enumerate(cosine_sim[chosen_hotel_index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        top_similar_hotels = similarity_scores[0:5]
        print("Recommended hotels:")
        for index, score in top_similar_hotels:
            recommended_hotel = filtered_df['Hotel Name'].iloc[index]
            print(f"- {recommended_hotel}")
    else:
        print("No hotels found matching your preferences.")