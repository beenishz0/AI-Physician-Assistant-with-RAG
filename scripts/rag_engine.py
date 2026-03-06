import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vectordb/index.faiss")
chunks = np.load("vectordb/chunks.npy", allow_pickle=True)


def retrieve(query, k=2):

    q_embed = model.encode([query])

    D, I = index.search(np.array(q_embed), k)

    results = [chunks[i] for i in I[0]]

    return "\n\n".join(results)

