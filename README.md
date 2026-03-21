# MailGuard AI

> Intelligent spam detection — built with Naive Bayes, served with Django.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat-square&logo=django&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-96%25-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## What is MailGuard AI?

MailGuard AI is a machine learning web application that classifies any text message or email as **spam** or **legitimate (ham)** in real time. You paste a message — the model gives you a verdict, instantly.

Under the hood it uses a **Multinomial Naive Bayes** classifier trained on the [SMS Spam Collection dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) from Kaggle — 5,500+ real-world messages — achieving **96% accuracy** on the test set.

The model is served through a clean Django web interface, keeping everything in one place: training notebook, saved model, and live prediction UI.

---

## Demo

| Input | Result |
|---|---|
| *"Congratulations! You've won a $1,000 Walmart gift card. Click now!"* | 🚨 **Spam** |
| *"Hey, are we still on for lunch tomorrow?"* | ✅ **Legitimate** |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| ML / Training | scikit-learn, pandas, numpy, Jupyter |
| Classifier | Multinomial Naive Bayes |
| Vectorization | TF-IDF (via `TfidfVectorizer`) |
| Web Framework | Django |
| Frontend | HTML · CSS |
| Dataset | [Kaggle — SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) |

---

## Project Structure

```
mailguard-ai/
│
├── data/                    # Raw dataset (CSV)
│
├── notebook/                # Jupyter notebook — EDA, training, evaluation
│
├── mailguard_web/           # Django application
│   ├── templates/           # HTML templates
│   ├── static/              # CSS
│   ├── views.py             # Prediction logic
│   └── ...
│
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Iman-Datta/mailguard-ai.git
cd mailguard-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Django server

```bash
cd mailguard_web
python manage.py migrate
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## How It Works

1. **Data** — The SMS Spam Collection dataset (sourced from Kaggle) contains 5,574 labelled messages: 4,827 ham and 747 spam.
2. **Preprocessing** — Text is lowercased, punctuation stripped, and transformed into TF-IDF feature vectors.
3. **Training** — A Multinomial Naive Bayes model is fit on the training split. Full training details are in `notebook/`.
4. **Serving** — The trained model is serialised with `joblib` and loaded by Django's view layer. Each POST request runs the message through the same TF-IDF pipeline and returns a prediction.

---

## Model Performance

| Metric | Score |
|---|---|
| Accuracy | **96%** |
| Algorithm | Multinomial Naive Bayes |
| Train / Test Split | 80 / 20 |
| Dataset Size | 5,574 messages |

Full confusion matrix, precision, recall, and F1 scores are available in the training notebook.

---

## Author

**Iman Datta**
[GitHub →](https://github.com/Iman-Datta)

---

## Dataset Credit

SMS Spam Collection Dataset — available on [Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset), originally compiled by the UCI Machine Learning Repository.

---

## License

This project is released under the [MIT License](LICENSE).
