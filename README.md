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

🙋‍♀️ Author
Pavani Punuru
