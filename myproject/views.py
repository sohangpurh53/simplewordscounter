from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render (request, 'index.html')

def counter(request):
 words = request.POST['words']
 total_word = len(words.split())
 return render(request, 'counter.html', {'Amount':total_word})