from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'index_text': "Welcome to Index page"
    }
    return render(request, 'index.html', context)
   # return HttpResponse("shreya here")
def about(request):
    context = {
        'about_text': "Welcome to About page"
    }
    return render(request, 'about.html', context)   