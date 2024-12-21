from django.shortcuts import render
from django.http import JsonResponse
import math

def calculate(request):
    if request.method == "POST":
        expression = request.POST.get("expression")
        try:
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    return render(request, "home.html")

def home(request):
    return render(request, 'home.html')