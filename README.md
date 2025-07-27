# 🎓 Lecture Notes Summarizer

An AI-powered web app that generates summarized lecture notes from a video by combining **audio transcription** and **visual text extraction**. It captures screenshots from key moments in the video, performs OCR, aligns it with the transcript, and generates a structured **PDF summary**.

---

## 📌 Features

- 🔊 Extracts and transcribes audio using OpenAI's Whisper model.
- 📸 Captures non-redundant, non-blurry video screenshots using OpenCV.
- 🧠 Uses OCR via Tesseract to extract text from video frames.
- 📄 Generates a clean, structured PDF combining text and screenshots.
- 🌐 User-friendly web interface using **Streamlit**.
- ☁️ Deployed on **Render** with support for `ffmpeg` and `tesseract`.

---

## 🚀 Live Demo

> https://lecturenotes-8vbq.onrender.com

---

## 🛠️ Tech Stack

| Component         | Tool/Library               |  
|------------------|----------------------------|  
| Frontend         | Streamlit                  |  
| Audio Transcription | Whisper (OpenAI)          |  
| Video Processing | OpenCV, ffmpeg             |  
| OCR              | Tesseract OCR via pytesseract |  
| PDF Generation   | ReportLab                  |  
| Hosting          | Render                     |  

---

## 📦 Installation

### 🔧 Requirements
- Python 3.9+
- ffmpeg
- tesseract

### 📥 Clone the repo

```bash
git clone https://github.com/yourusername/lecturenotes-app.git
cd lecturenotes-app
🧪 Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
▶️ Run locally
bash
Copy
Edit
streamlit run app.py
🗃️ Directory Structure
php
Copy
Edit
.
├── app.py                    # Streamlit UI
├── final.py                  # Core processing logic
├── requirements.txt
├── render.yaml               # Render deployment config
├── uploaded_video.mp4        # Sample uploaded video
├── screenshots/              # Extracted frames from video
├── transcription.txt         # Generated transcript
└── video_summary.pdf         # Final output PDF
🧠 How It Works
Upload Video
Uploads a .mp4 lecture recording.

Audio Transcription
Uses Whisper to transcribe speech into text.

Screenshot Capture
OpenCV extracts key video frames every few seconds (skips blurry or repetitive ones).

OCR on Screenshots
Tesseract extracts visible text from each frame.

Merge Timeline
Combines transcript + screenshot data into a timeline.

PDF Generation
Formats everything into a downloadable PDF using ReportLab.

🧪 Example Output
A 2-minute sample lecture results in a video_summary.pdf that includes:

Timestamped transcript

5+ clean lecture board screenshots

Clean layout with readable fonts

📤 Deployment on Render
Make sure your render.yaml contains:

yaml
Copy
Edit
services:
  - type: web
    name: lecturenotes-app
    runtime: python
    buildCommand: |
      apt-get update && \
      apt-get install -y ffmpeg tesseract-ocr && \
      pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port=10000 --server.enableCORS=false
    envVars:
      - key: PYTHONUNBUFFERED
        value: "true"
    plan: free
🤖 Powered By
Whisper by OpenAI

Streamlit

Tesseract OCR

ReportLab

🙋‍♀️ Author
Pavani Punuru
