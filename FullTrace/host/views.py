from django.shortcuts import render
from host import forms
from host import models

# Create your views here.
def add_host(request):
    form = forms.host_ModelForm()
    if request.method == "POST":
        form = forms.host_ModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            host_obj = models.host.objects.all()
            return render(request, 'host/ssh_crack.html', {
                'host_obj': host_obj
            })
        else:
            print(form.errors)
    return render(request, 'host/add_host.html', {
        'host_form': form
    })