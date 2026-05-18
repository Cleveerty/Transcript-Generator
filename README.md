# Transcribe Video (faster-whisper)

This repository contains simple Python scripts to transcribe an MP4 video using `faster-whisper`.

Files
- `transcribe_fast.py`: Fast transcription using the `tiny.en` model (writes `transcript.txt`).
- `transcribe_video.py`: Full-model transcription (may download larger models).

Requirements
- Python 3.8+ (Python 3.14 used during development)
- See `requirements.txt` for Python packages

Quick start (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Run the fast transcription (produces `transcript.txt`):

```powershell
python transcribe_fast.py
```

Notes
- The scripts download models from Hugging Face; setting `HF_TOKEN` speeds up downloads and increases rate limits.
- If you want higher accuracy, run `transcribe_video.py` with a larger model (e.g. `small.en`, `medium.en`), but this will download more data and take longer.

Video file

- The original MP4 is large and has been removed from this repository to keep the repo small.
- To run the scripts, download the video and place it in the repository root with the exact filename:

```powershell
# example: download with PowerShell (replace <URL> with the real link)
Invoke-WebRequest -Uri "<VIDEO_URL>" -OutFile "THE SPIRIT AND THE BRIDE SAY COME   Day 1 Missions Crusade Night Service  May 17, 2026-640x360-avc1-mp4a.mp4"
```

- Alternatively, place any MP4 in the repo root and update the `video_path` variable in the scripts if the filename differs.

License

This project is provided as-is; see `LICENSE`.
