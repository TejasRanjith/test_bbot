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

initial_prompt=""
try:
    if st.query_params["qno"] == "1":
        initial_prompt = "in the image or the code snippet, your job is to identify if there are any mistakes and must be ablle to score it based on, for each error, reduce 0.5 points.score it out of 10.only and only return the final score alone.only final score as integer has to be outputted"
    elif st.query_params["qno"] == "2":
        initial_prompt = "in the image or code snippet, your job is to identify if there are any mistakes and must be ablle to score it based on, for each error, reduce 5 points.score it out of 100.only and only return the final score alone.only final score as integer has to be outputted"        
    else:
        initial_prompt = ""
except:
    initial_prompt = ""


if st.button("Generate Brief"):
    if not uploaded_file and not case_text:
        st.warning("Please upload a file or enter case text.")
    else:
        genai.configure(api_key="AIzaSyA9b9YZBLkxBOhRd1wDahGYbZkUI4YU9Qk")
        model = genai.GenerativeModel('gemini-2.0-flash')
        inputs = []
        if uploaded_file:
            img = Image.open(uploaded_file)
            inputs.append(img)
        if initial_prompt:
            inputs.append(initial_prompt)
        if case_text:
            inputs.append(case_text)
        response = model.generate_content(inputs)
        st.markdown("**Generated Brief:**")
        st.write(response.text)
