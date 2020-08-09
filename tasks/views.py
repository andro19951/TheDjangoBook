from django.shortcuts import render
from django import forms
# Create your views here.
tasks = ["foo","bar","bas"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    return render(request, "tasks/index.html",{
        "tasks" : tasks
        
        })
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task= form.cleaned_data["task"]
            tasks.append(task)
    return render(request, "tasks/add.html", {
        'form': NewTaskForm()
        })
