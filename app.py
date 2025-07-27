import streamlit as st
import os
from final import (
    extract_audio_from_video,
    transcribe_audio_to_segments,
    extract_screenshots,
    merge_timeline,
    generate_pdf_summary
)

st.title("🎥 Video Summary Generator")

video_file = st.file_uploader("Upload a video file", type=["mp4"])
if video_file:
    with open("uploaded_video.mp4", "wb") as f:
        f.write(video_file.read())

    st.success("✅ Video uploaded. Starting processing...")

    try:
        extract_audio_from_video("uploaded_video.mp4", "audio.wav")
        st.info("🔊 Audio extracted...")

        transcript_segments = transcribe_audio_to_segments("audio.wav")
        st.info("📝 Transcription completed...")

        screenshot_data = extract_screenshots("uploaded_video.mp4", output_dir="screenshots", interval=2)
        st.info("📸 Screenshots captured...")

        timeline = merge_timeline(transcript_segments, screenshot_data)
        generate_pdf_summary(timeline, "summary.pdf")

        with open("summary.pdf", "rb") as pdf_file:
            st.download_button("📥 Download Summary PDF", pdf_file, file_name="video_summary.pdf")

    except Exception as e:
        st.error(f"❌ Error: {e}")
