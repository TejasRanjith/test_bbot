import streamlit as st
from PIL import Image
import google.generativeai as genai

st.set_page_config(page_title="LLM Prompt Window", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #111;
        color: #fff;
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        background-color: #222;
        color: #fff;
        border: none;
        border-radius: 4px;
        padding: 10px;
        max-height: 200px;
    }
    .stFileUploader>div>button {
        background-color: #555;
        color: #fff;
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
    }
    .stButton>button {
        background-color: #2196F3;
        color: #fff;
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
    }
    .or-divider {
        text-align: center;
        margin: 20px 0;
        color: #666;
    }
    .stFileUploader>div>div {
        max-height: 200px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;font-size: 90px;'>BBot</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload File", type=["jpg", "jpeg", "png"])

st.markdown('<div class="or-divider">OR</div>', unsafe_allow_html=True)

case_text = st.text_area("Paste case text here", height=200, max_chars=None)

if st.button("Generate Brief"):
    if uploaded_file is not None and case_text.strip() != "":
        img = Image.open(uploaded_file)
        genai.configure(api_key="AIzaSyA9b9YZBLkxBOhRd1wDahGYbZkUI4YU9Qk")
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content([img, case_text])
        st.markdown("**Generated Brief:**")
        st.write(response.text)
    else:
        st.warning("Please upload a file and enter case text.")
