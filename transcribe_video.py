from pathlib import Path
from faster_whisper import WhisperModel

video_path = Path("THE SPIRIT AND THE BRIDE SAY COME   Day 1 Missions Crusade Night Service  May 17, 2026-640x360-avc1-mp4a.mp4")
output_path = Path("transcript.txt")

model_size = "small.en"
print("Loading model", model_size)
model = WhisperModel(model_size, device="cpu", compute_type="int8")

print("Transcribing video", video_path)
segments, info = model.transcribe(str(video_path), beam_size=5, vad_filter=True)
print(f"Detected language: {info.language}, duration: {info.duration}")

with output_path.open("w", encoding="utf-8") as out:
    for segment in segments:
        start = segment.start
        end = segment.end
        text = segment.text.strip()
        if text:
            line = f"[{start:.2f} --> {end:.2f}] {text}"
            out.write(line + "\n")
            print(line)

print("Transcript saved to", output_path)
