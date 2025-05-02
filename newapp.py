import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_checkpoint_ar_en = "./my_finetuned_model_egy_en"       # Arabic → English
model_checkpoint_en_to_ar = "./my_finetuned_model_en_to_ar"  # English → Arabic

st.title("Translation App")
st.markdown("Choose translation direction and enter the text:")

direction = st.selectbox("Select translation direction", ["Arabic to English", "English to Arabic"])

if direction == "Arabic to English":
    model_checkpoint = model_checkpoint_ar_en
    st.markdown("Translation Direction: Arabic to English")
else:
    model_checkpoint = model_checkpoint_en_to_ar
    st.markdown("Translation Direction: English to Arabic")

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

try:
    model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
    model.to(torch.device("cpu"))  
    model.eval()
except Exception as e:
    st.error(f"Error during model initialization: {e}")
    st.stop()

user_input = st.text_area("Enter text to translate:", height=100)

if st.button("Translate"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        with st.spinner("Translating..."):
            try:
                inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True).to("cpu")
                outputs = model.generate(**inputs)
                translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
                st.success("Translation:")
                st.text_area("Translated Text", value=translated_text, height=100)
            except Exception as e:
                st.error(f"Error during translation: {e}")
