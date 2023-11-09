from django.shortcuts import render

# Create your views here.

def homepage(request):
    data = {
        'title' : 'Homepage'
    }
    return render(request, 'index.html', data)

def about_me(request):
    data = {
        'title' : 'About me'
    }
    return render(request, 'about.html', data)

# def handelling_404(request, exception):
#     data = {
#         'title' : '404 Error not found'
#     }
#     return render(request, '404.html', data)