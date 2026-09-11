from django.shortcuts import render
import pickle


def home(request):

    prediction = None

    if request.method == "POST":

        age = float(request.POST["age"])
        blood_pressure = float(request.POST["blood_pressure"])
        cholesterol = float(request.POST["cholesterol"])

        with open("model.pkl", "rb") as file:
            model = pickle.load(file)

        result = model.predict([
            [age, blood_pressure, cholesterol]
        ])[0]

        if result == 1:
            prediction = "Heart Disease: Yes"
        else:
            prediction = "Heart Disease: No"

    return render(request, "index.html", {
        "prediction": prediction
    })