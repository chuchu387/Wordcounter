from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def counter(request):
    text = request.GET['text']
    words_counter = len(text.split())
    return render(request, 'counter.html', {'total_words': words_counter})
