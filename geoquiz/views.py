import random
import requests
from django.shortcuts import render

response = requests.get('https://countriesnow.space/api/v0.1/countries/capital')


def index(request):
    i = random.randint(0, len(response.json()['data']))
    name = response.json()['data'][i]['name']
    return render(request, 'index.html', {'name': name, 'i': i})


def word(request):
    search = request.GET.get('search')
    i = int(request.GET.get('i'))
    name = response.json()['data'][i]['name']
    capital = response.json()['data'][i]['capital']
    if search is None or search == "":
        search = "Type in your guess :)"
        capital = ""
    elif search == capital:
        search = "Perfect! Your guess was correct!"
        capital = ""
    else:
        search = "Your guess was incorrect"
        capital = f"The capital of {name} is {capital}"

    context = {
        'search': search,
        'name': name,
        'capital': capital
    }
    return render(request, 'word.html', context)
