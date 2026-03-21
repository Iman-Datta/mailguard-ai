import pickle
import os
from django.shortcuts import render, redirect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR = os.path.dirname(BASE_DIR)

model_path = os.path.join(ROOT_DIR, 'Model', 'model.pkl')
vectorizer_path = os.path.join(ROOT_DIR, 'Model', 'vectorizer.pkl')

model = pickle.load(open(model_path, 'rb'))
vectorizer = pickle.load(open(vectorizer_path, 'rb'))

def home(request):
    return render(request, 'index.html')


def predict(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        msg_vec = vectorizer.transform([message])
        result = model.predict(msg_vec)[0]

        prediction = "Spam" if result == 1 else "Not Spam"

        return render(request, 'index.html', {
            'prediction': prediction,
            'message': message
        })

    return redirect('home')