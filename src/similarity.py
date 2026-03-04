from sklearn.metrics.pairwise import cosine_similarity

def check_similarity(text1,text2,embeddings):

    emb1 = embeddings.embed_query(text1)
    emb2 = embeddings.embed_query(text2)

    score = cosine_similarity([emb1],[emb2])[0][0]

    return score