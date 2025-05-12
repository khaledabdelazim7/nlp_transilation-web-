# Translation App

## 📌 Overview

The **Translation App** is a web-based interface developed using **Streamlit** that allows users to translate text between **Arabic and English**. The application utilizes **fine-tuned transformer models** for both translation directions:

* Arabic → English
* English → Arabic

---

## ⚙️ Project Structure

```plaintext
.
├── app.py                             # Main Streamlit application file
├── my_finetuned_model_egy_en/        # Fine-tuned model directory for Arabic to English
└── my_finetuned_model_en_to_ar/      # Fine-tuned model directory for English to Arabic
```

---

## 🧰 Requirements

### Python Packages:

* `streamlit`
* `transformers`
* `torch`

### Installation:

```bash
pip install streamlit transformers torch
```

---

## 🚀 How to Run

1. Make sure the fine-tuned model directories (`my_finetuned_model_egy_en` and `my_finetuned_model_en_to_ar`) are present in the project directory.
2. Run the Streamlit app using:

   ```bash
   streamlit run newapp.py
   ```
3. The app will launch in your browser. Choose a translation direction, input text, and click **"Translate"**.

---

## 💡 Features

* **Direction Toggle**: Select between *Arabic to English* or *English to Arabic*.
* **Model Loading**: Loads corresponding fine-tuned transformer model based on selected direction.
* **User Input**: Accepts user input in a text area.
* **Translation Output**: Displays the translated result in another text area.
* **Error Handling**: Basic exception handling for model loading and translation generation.

---

## 📦 Model Details

* The models are expected to be **fine-tuned versions of seq2seq models** like `mBART`, `MarianMT`, or `T5`.

* Tokenizer and model are loaded using:

  ```python
  AutoTokenizer.from_pretrained(model_checkpoint)
  AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
  ```

* Translation logic uses:

  ```python
  inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True).to("cpu")
  outputs = model.generate(**inputs)
  ```

---

## ✅ Example Usage

* **Input (Arabic)**: "أنا أحب البرمجة."
* **Output (English)**: "I love programming."

---

## 🧪 Notes and Recommendations

* Make sure your models are compatible with `AutoModelForSeq2SeqLM`.
* If using GPU for inference, replace `torch.device("cpu")` with appropriate CUDA settings.
* Consider adding support for longer inputs and batch processing for more robust use.
* You can deploy the app via **Streamlit Cloud**, **Docker**, or a cloud VM (e.g., AWS/GCP).

---

## 📁 Related Files

* `fine-tunning.ipynb`: Jupyter Notebook that likely contains the training/fine-tuning code for the models.
