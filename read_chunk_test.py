import os
import requests
import json
import numpy as  np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def create_embedding(text_list):
    r  = requests.post("http://localhost:11434/api/embed",json={
        "model": "bge-m3",
        "input": text_list
    })
    embedding = r.json()["embeddings"]
    return embedding

jsons = os.listdir("jsons")


for json_file in jsons:
    with open(f"jsons/{json_file}","r") as f:
              content  = json.load(f)
    print(f"Creating embedding for {json_file}")
    embeddings = 