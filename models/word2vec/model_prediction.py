# Load the trained model
model = Word2Vec.load("hpo_word2vec.model")

# Input HPO terms
hpo_terms = ['HP:0000347', 'HP:0003020', 'HP:0009381']

# Predict the next HPO term
similar_terms = model.wv.most_similar(positive=hpo_terms, topn=3)
print(similar_terms)
