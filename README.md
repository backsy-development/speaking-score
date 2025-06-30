# 🎧 Pronunciation Scoring API – Powered by Transformers

This repository provides a simple yet powerful **Flask-based REST API** for evaluating English speech pronunciation, using pre-trained models from Hugging Face. The API supports two scoring endpoints: **pronunciation completeness** and **fluency**.

## 🚀 Features

- `/junbro1016/pronunciation-scoring-completeness`  
  → Scores how *complete* the user's pronunciation is.

- `/junbro1016/pronunciation-scoring-fluency`  
  → Scores the *fluency* of spoken audio.

- Built with **Python**, **Flask**, and **Hugging Face Transformers**
- Accepts raw audio in `POST` requests
- Returns model inference results in structured JSON
- Easy to integrate into web or mobile apps for language learning

## 🔧 How It Works

The system uses two pre-trained audio classification models:

- `junbro1016/pronunciation-scoring-completeness`
- `junbro1016/pronunciation-scoring-fluency`

Both are loaded via Hugging Face’s `pipeline()` method and are designed to analyze raw audio buffers sent via HTTP.

### Sample Code (Core Logic)

```python
from flask import Blueprint, request
from transformers import pipeline

junbro1016 = Blueprint('junbro1016', __name__)

completenessPipe = pipeline("audio-classification", model="junbro1016/pronunciation-scoring-completeness")
fluencyPipe = pipeline("audio-classification", model="junbro1016/pronunciation-scoring-fluency")

@junbro1016.route('/junbro1016/pronunciation-scoring-completeness', methods=['POST'])
def getPronounceScore():
    try:
        audio_buffer = request.data
        result = completenessPipe(audio_buffer)
        return result
    except Exception as e:
        print(e)
        return { "message": "serverError" }, 500

@junbro1016.route('/junbro1016/pronunciation-scoring-fluency', methods=['POST'])
def getFluencyScore():
    try:
        audio_buffer = request.data
        result = fluencyPipe(audio_buffer)
        return result
    except Exception as e:
        print(e)
        return { "message": "serverError" }, 500
````

### 🧪 Example CURL Request

```bash
curl -X POST http://localhost:4102/junbro1016/pronunciation-scoring-completeness \
     --data-binary @sample.wav \
     -H "Content-Type: application/octet-stream"
```

## 📂 File Structure

```bash
├── config/
│   └── config.py          # App configuration
├── app.py                 # Main Flask application
├── junbro1016_api.py      # Pronunciation scoring endpoints
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 🧠 Ideal For

* Language learning apps
* English pronunciation scoring
* AI voice-based assessment
* EdTech platforms
* Automated speaking tests (e.g. IELTS, TOEFL practice)

---

## 🌍 Related Project: [Backsy.io](https://backsy.io)

Looking for a way to **streamline returns and boost retention** on your Shopify store?

✨ [**Backsy**](https://backsy.io) is an all-in-one post-purchase return & exchange solution that helps Shopify merchants reduce refunds, increase re-purchases, and build customer loyalty.

> 👉 Check it out at [https://backsy.io](https://backsy.io)

---

## 📦 Installation

```bash
git clone https://github.com/your-repo/pronunciation-scoring-api.git
cd pronunciation-scoring-api
pip install -r requirements.txt
python app.py
```

---

## 📜 License

MIT License. Use it freely in your projects.

---

## 🙌 Credits

Developed by the team behind [Backsy](https://backsy.io), combining the power of AI with practical applications in both eCommerce and EdTech.
