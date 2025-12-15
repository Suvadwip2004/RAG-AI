import whisper
import os
import json
model = whisper.load_model("small")
audios = os.listdir("audios")
for audio_one in audios:
   
    
    number  = audio_one.split("mp4")[0]
    title  = audio_one.split("mp4_")[1][:-4]
    print(number,title)
    # result = model.transcribe(audio="output.mp3",language = "hi",task  = "translate",word_timestamps=False)
    result = model.transcribe(audio=f"audios/{audio_one}",language = "hi",task  = "translate",word_timestamps=False)
   
    chunks  = []
    for segment in result["segments"] :
        chunks.append({
            "number":number,
            "title" : title,
            "start":segment["start"],
            "end":segment["end"],
            "text":segment["text"]
        })

    chunks_with_metadata  = {"chunks" :chunks,"text": result["text"]}
    with open(f"jsons/{audio_one}.json","w") as f:
        json.dump(chunks_with_metadata,f)