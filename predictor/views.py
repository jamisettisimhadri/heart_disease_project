from django.shortcuts import render
from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


def home(request):
    prediction = None

    if request.method == "POST":
        age = float(request.POST["age"])
        blood_pressure = float(request.POST["blood_pressure"])
        cholesterol = float(request.POST["cholesterol"])

        result = model.predict([
            [age, blood_pressure, cholesterol]
        ])[0]

        prediction = (
            "Heart Disease: Yes"
            if result == 1
            else "Heart Disease: No"
        )

    return render(request, "index.html", {
        "prediction": prediction
    })
