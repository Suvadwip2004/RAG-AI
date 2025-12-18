import requests
import json
import os
import pandas as pd

API_URL = "https://jade-seattle-coat-fantastic.trycloudflare.com/embed"

def create_embedding(text_list):
    # payload = {
    #     "texts": [text, "second sentence"],
    #     "normalize": True,
    #     "file": "/mnt/data/d9dd9b82-d0d8-4200-8eb8-a7e041af14c3.png"
    # }
    payload = {
    "texts": text_list,        # <-- send user-provided list
    "normalize": True,
    "file": "/mnt/data/d9dd9b82-d0d8-4200-8eb8-a7e041af14c3.png"
    }

    embedding = requests.post(API_URL, json=payload, timeout=700)
    return embedding.json()['embeddings']

# a  = create_embedding(["cat set on mat","Harry is a very good boy."])
# print(a)


jsons  = os.listdir("jsons")
my_dicts  =[]
chunk_id  = 0
for json_file in jsons:
    with open (f"jsons/{json_file}") as f:
        content  = json.load(f)
    print(f"Creating Embedding for{json_file}")
    embeddings  = create_embedding([c['text'] for c in content['chunks']])
    for i,chunk in enumerate(content["chunks"]):
        # print(chunk)
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]
        chunk_id +=1
        my_dicts.append(chunk)
    
            
    
# print(my_dicts)
df  = pd.DataFrame.from_records(my_dicts)
print(df)