from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import StudentForm
from django.views import View
from .models import Student
import socket


class StudentView(View):
    
    def get(self, request):
        try:
            HOSTNAME = socket.gethostname()
        except:
            HOSTNAME = 'localhost'

        pt = StudentForm
        inf = Student.objects.all()
        return render(request, "student/student.html", {'pt': pt,'inf': inf, 'hostname': HOSTNAME})

    def post(self, request):
        try:
            HOSTNAME = socket.gethostname()
        except:
            HOSTNAME = 'localhost'

        pt = StudentForm
        if request.method == "POST":
            cf = StudentForm(request.POST)
            if request.POST['submit_button'] == 'Add':
                if cf.is_valid():
                    saveCF = Student(studentid = cf.cleaned_data['studentid'],
                                        name = cf.cleaned_data['name'],
                                        email = cf.cleaned_data['email'],
                                        phone = cf.cleaned_data['phone'],
                                        address = cf.cleaned_data['address']
                                        )

                    saveCF.save()
                    inf = Student.objects.all()
                    return render(request, "student/student.html", {'pt': pt,'inf': inf, 'hostname': HOSTNAME})
                else:
                    noti = "add data Fail"
                    inf = Student.objects.all()
                    return render(request, "student/student.html", {'pt': pt,'inf': inf,'noti': noti, 'hostname': HOSTNAME})

            if request.POST['submit_button'] == 'Delete':

                id = request.POST.get('studentid')
                Student.objects.filter(studentid = id).delete()

                inf = Student.objects.all()
                return render(request, "student/student.html", {'pt': pt,'inf': inf, 'hostname': HOSTNAME})

            
            if request.POST['submit_button'] == 'Update':
                try:
                    id = request.POST.get('studentid')
                    student = Student.objects.get(studentid = id)

                    if request.POST.get('name'):
                        student.name = request.POST.get('name')

                    if request.POST.get('email'):
                        student.email = request.POST.get('email')
                    
                    if request.POST.get('phone'):
                        student.phone = request.POST.get('phone')
                    
                    if request.POST.get('address'):
                        student.address = request.POST.get('address')
                    student.save()

                    inf = Student.objects.all()
                    return render(request, "student/student.html", {'pt': pt,'inf': inf, 'hostname': HOSTNAME})
                except Exception as e:
                    noti = str(e)
                    inf = Student.objects.all()
                    return render(request, "student/student.html", {'pt': pt,'inf': inf,'noti': noti, 'hostname': HOSTNAME})
