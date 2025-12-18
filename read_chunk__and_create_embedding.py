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
my_dicts  = []
chunk_id  = 0

for json_file in jsons:
    with open(f"jsons/{json_file}","r") as f:
              content  = json.load(f)
    print(f"Creating embedding for {json_file}")
    embeddings = create_embedding([c['text'] for c in content['chunks']])
    for i,chunk in enumerate(content['chunks']):
          chunk['chunk_id'] = chunk_id
          chunk_id +=1
          chunk['embedding'] = embeddings[i]
          my_dicts.append(chunk)

    break

df = pd.DataFrame.from_records(my_dicts)


incoming_query  = input("Ask any question : ")
question_embedding  = create_embedding([incoming_query])[0]

similarityes  = cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
print(similarityes)
top_result  = 3
max_index  = similarityes.argsort()[::-1][0:top_result]
print(max_index)
new_df = df.loc[max_index]
print(new_df[["title","number","text"]])