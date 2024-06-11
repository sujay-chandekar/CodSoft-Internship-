from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import task
from django.contrib import messages
# Create your views here.
def add_task(request):
    Data = task.objects.all()
    if request.method == "POST":
        data =  request.POST
        name = data.get("name")
        if name:
            add = task(task_name = name)
            add.save()
            messages.success(request, "Task saved successfully!")
            return redirect('/')
        else :
            messages.error(request, "All fields are required.")
            print("Invalid form data")
    context = {'tasks':Data}
    return render(request, 'taskAdd.html',context)

def updatetask(request,id):
    Data = get_object_or_404(task, id=id)
    if request.method == "POST":
        data = request.POST
        Data.task_name = data.get("name")
        Data.save()
        return redirect('/')
    context = {'task': Data}
    return render(request,'updateTask.html',context)

def deletetask(request , id):
    taskData = get_object_or_404(task, id=id)
    taskData.delete()
    return redirect('/')