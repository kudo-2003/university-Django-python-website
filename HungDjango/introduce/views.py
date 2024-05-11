from django.shortcuts import render

def introduce(request):
    return render(request, 'home.html')

