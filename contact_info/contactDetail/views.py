from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from .models import *
# Create your views here.
def addcontact(request):
    alldata =  contactInfo.objects.all()
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        phoneNumber = data.get("phone")
        email = data.get("mail")
        address = data.get("address")

        if name and phoneNumber and email and address:
            query = contactInfo.objects.create(
                name  = name,
                phoneNumber = phoneNumber,
                email = email,
                address = address
            )
            query.save()
            messages.success(request, "Contact saved successfully!")
            return redirect('/')
        else:
            messages.error(request, "All fields are required.")
            return redirect('/')
    context = {'contacts' : alldata}
    return render(request , 'contactAdd.html' ,context)

#delete contact
def deletecontact(request,id):
    obj = get_object_or_404(contactInfo,id=id)
    obj.delete()
    return redirect('/')

#Update contact

def updatecontact(request,id):
    obj = get_object_or_404(contactInfo,id=id)
    if request.method == "POST":
        data = request.POST
        obj.name = data.get("name")
        obj.phoneNumber = data.get("phone")
        obj.email = data.get("mail")
        obj.address = data.get("address")
        obj.save()
        messages.success(request, "Contact updated successfully!")
        return redirect('/')
    context = {'contacts':obj}
    return render(request,'updatecontact.html',context)
