import openai
from openai.embeddings_utils import cosine_similarity


openai.api_key_path = '.env'


def get_embedding(text, model="text-similarity-davinci-001"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']


def label_score(review_embedding, label_embeddings):
    similarity = cosine_similarity(review_embedding, label_embeddings)
    return similarity