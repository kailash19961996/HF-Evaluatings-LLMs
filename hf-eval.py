import streamlit as st
import requests

st.markdown("""
<div style='text-align: center;'>
<h1> Hugging Face - free models Evaluation <h1>     
</div>
""", unsafe_allow_html=True)

model_id = ["meta-llama/Meta-Llama-3-8B-Instruct", "mistralai/Mixtral-8x7B-Instruct-v0.1", "openai-community/gpt2", "google/gemma-7b", "bigcode/starcoder"]

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
</div>
""", unsafe_allow_html=True)
    

def query(payload, model_id, api_key):
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


api_key = st.text_input("Enter your Hugging Face API Key", type ="password")
st.write("If you don't have one handy, use this API Key: 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")
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