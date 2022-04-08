from django.shortcuts import render,redirect
from .models import Webapp
from .forms import WebappForm

def index(request):
    webs = Webapp.objects.all()
    return render(request,'main/index.html',{'title': 'Главная страница сайта','webs':webs})
def about(request):
    return render(request,'main/about.html')
def create(request):
    error = ''
    if request.method == 'POST':
        form = WebappForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Форма была неверной'

    form = WebappForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'main/create.html',context)