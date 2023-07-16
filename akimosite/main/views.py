from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['#Akimo', '#coolbot', '#host'],
        'obj': {
            'car': 'Lamborghini',
            'age': 16,
            'hobby': 'Programming, discord, sport'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')