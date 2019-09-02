from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home1.html')

def contact(request):
    return HttpResponse('<h1>This is your contact page')

def count(request):
    data = request.GET['txt']
    listlen = len(data)
    word_lst = data.split()
    ln = len(word_lst)
    worddictionary = {}

    for i in word_lst:
        if i in worddictionary:
            worddictionary[i] +=1
        else:
            worddictionary[i] = 1

    sorted_list = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'text': data, 'ln': ln, 'll': sorted_list, 'lln': listlen})

def about(request):
    return render(request, 'about.html')