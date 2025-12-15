import whisper
import json

# Load model
model = whisper.load_model("large-v2")

# Transcribe + translate
result = model.transcribe(
    audio="WhatsApp Audio 2025-11-24 at 11.44.32_3c407d1c.mp3",
    language="hi",
    task="translate",
    word_timestamps=False
)

# Create segment list
chunks = []
for segment in result["segments"]:
    chunks.append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
    })

# Print chunks
print(chunks)

# Save output
with open("output11.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=4)