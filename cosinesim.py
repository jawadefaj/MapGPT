from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity




def cosine_sim(ref, pred):
    vectorizer = CountVectorizer()

    # Fit and transform the text data
    vectorized_text = vectorizer.fit_transform([ref, pred])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(vectorized_text[0], vectorized_text[1])
    # print(cosine_sim)
    # print("Cosine Similarity:", cosine_sim[0][0])
    return cosine_sim[0][0]

