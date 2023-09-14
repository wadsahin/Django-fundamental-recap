from django.shortcuts import render
from django.http import HttpResponse
from .forms import userForm, modelForm
from .models import userModel

# Create your views here.
def helloWorld(request):
    return render(request, 'home.html');

def bikeFun(request):
    return render(request, 'index.html');

def formShow(request):
    formData = userForm();
    return render(request, 'form.html', {'fm':formData});

def modelShow(request):
    modelData = userModel.objects.all()
    return render(request, 'model.html', {'dt': modelData})

def modelFormShow(request):
    if request.method == 'POST':
        fm = modelForm(request.POST)
        if fm.is_valid():
            uid = fm.cleaned_data['uid']
            fn = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            em = fm.cleaned_data['email']
    else:
        fm = modelForm()
    return render(request, 'model-form.html', {'form':fm})

