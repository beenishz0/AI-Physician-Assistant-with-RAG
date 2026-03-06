
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# Model to create embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Folder containing all guideline text files
guideline_folder = "guidelines"

all_chunks = []

# Iterate over all .txt files
for filename in os.listdir(guideline_folder):
    if filename.endswith(".txt"):
        path = os.path.join(guideline_folder, filename)
        with open(path) as f:
            text = f.read()
            # Split into chunks by double newline for better retrieval
            chunks = text.split("\n\n")
            # Keep track of source filename for reference
            all_chunks.extend([f"{filename}:\n{chunk}" for chunk in chunks])

# Create embeddings
embeddings = model.encode(all_chunks)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Save index and chunks
os.makedirs("vectordb", exist_ok=True)
faiss.write_index(index, "vectordb/index.faiss")
np.save("vectordb/chunks.npy", all_chunks)

print(f"Indexed {len(all_chunks)} guideline chunks from {len(os.listdir(guideline_folder))} files.")

