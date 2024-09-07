import streamlit as st
import requests
import os
import streamlit.components.v1 as components

# App header
def spline_component(url, width=150, height=90):
    components.iframe(url, width=width, height=height)

col1, col2 = st.columns([1, 3])
with col1:
    spline_component("https://lottie.host/embed/c723a9ba-2211-4763-8577-5ef32f97a869/yNF4aB95zv.json")

with col2:
    st.title("Hugging Face - free models Evaluation")
    
st.markdown("""
<div style='text-align: center;'>
     <i>"An app that evaluates free Hugging Face language models by generating text responses based on user queries."<i>
     <h4>90-second Demo</h4>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center;'>
<i> Available models for evaluation: </i> 
            \n ---------------------------
            \n meta/Meta-Llama-3-8B-Instruct 
            \n mistralai/Mixtral-8x7B-Instruct-v0.1 
            \n openai/gpt2 
            \n google/gemma-7b 
            \n bigcode/starcoder
            \n ---------------------------
""", unsafe_allow_html=True)

model_id = ["meta-llama/Meta-Llama-3-8B-Instruct", "mistralai/Mixtral-8x7B-Instruct-v0.1", "openai-community/gpt2", "google/gemma-7b", "bigcode/starcoder"]

linkedin = "https://raw.githubusercontent.com/kailash19961996/icons-and-images/main/linkedin.gif"
github =   "https://raw.githubusercontent.com/kailash19961996/icons-and-images/main/gitcolor.gif"
Youtube =  "https://raw.githubusercontent.com/kailash19961996/icons-and-images/main/371907120_YOUTUBE_ICON_TRANSPARENT_1080.gif"
email =    "https://raw.githubusercontent.com/kailash19961996/icons-and-images/main/emails33.gif"
website =  "https://raw.githubusercontent.com/kailash19961996/icons-and-images/main/www.gif"


def query(payload, model_id, api_key):
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


api_key = st.text_input("Enter your Hugging Face API Key", type ="password")
st.write("If you don't have it handy, use this API Key: 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")
user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    if api_key and user_input:
        for i in range(len(model_id)):
            model = model_id[i]
            payload = {"inputs": user_input}
            try:
                result = query(payload, model, api_key)
                # st.write(result[0])
                if isinstance(result, list) and len(result) > 0:
                    generated_text = result[0].get('generated_text', 'No text generated')
                    st.write("Model:", model_id[i])
                    st.write("Generated Text:", generated_text)
                    st.write("-------------------------------------------------------")
                else:
                    st.error(f"Unexpected response format: {result}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter both the API key and a prompt.")

st.markdown("""
<div style='text-align: center;'>
    Built by <a href="https://kailashsubramaniyam.com/">Kai</a>. Like this? <a href="https://kailashsubramaniyam.com/contact">Hire me!</a>
</div>
""", unsafe_allow_html=True)

coll1,coll2,coll3 = st.columns(3)
with coll2:
    st.write(
        f"""
            <div style='display: flex; align-items: center;'>
            <a href = 'https://kailashsubramaniyam.com/'><img src='{website}' style='width: 35px; height: 35px; margin-right: 25px;'></a>
            <a href = 'https://www.youtube.com/@kailashbalasubramaniyam2449/videos'><img src='{Youtube}' style='width: 28px; height: 28px; margin-right: 25px;'></a>
            <a href = 'https://www.linkedin.com/in/kailash-kumar-balasubramaniyam-62b075184'><img src='{linkedin}' style='width: 35px; height: 35px; margin-right: 25px;'></a>
            <a href = 'https://github.com/kailash19961996'><img src='{github}' style='width: 30px; height: 30px; margin-right: 25px;'></a>
            <a href = 'mailto:kailash.balasubramaniyam@gmail.com''><img src='{email}' style='width: 31px; height: 31px; margin-right: 25px;'></a>
        </div>""", unsafe_allow_html=True,)
