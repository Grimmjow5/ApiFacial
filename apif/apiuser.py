from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from .models import Employee
from .forms import EmployeeForm, UploadFileForm


def addUser(request):
    try:

        videos = request.FILES.getlist('video')
        print(videos)
        nuevo = EmployeeForm(request.POST)
        new_employee = nuevo.save(commit=False)
        new_employee.employee = request.POST
        new_employee.save()

        return redirect('/control/')

    except InterruptedError:
        return HttpResponse('Error')



from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return redirect("/control/")
    else:
        form = UploadFileForm()
    return redirect("/control/")

def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)