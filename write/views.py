from django.shortcuts import render, redirect, get_object_or_404
from .models import Word
from urllib import parse
# Create your views here.


def home(req):
    word = Word.objects
    return render(req, 'home.html', {'word': word})


def word(req, word):
    data = get_object_or_404(Word, word=word)
    print(data.meaning)
    return render(req, 'word.html', {'data': data})


def new(req):
    return render(req, 'new.html')


def edit(req, word):
    pass


def delete(req, word):
    pass


def create(req):
    if(req.method == 'POST'):
        word = Word()
        word.word = req.POST['word']
        word.author = req.POST['author']
        word.meaning = req.POST['meaning']
        word.save()
        return redirect('/word/' + word.word)
    return redirect('home')


def modify(req):
    pass
