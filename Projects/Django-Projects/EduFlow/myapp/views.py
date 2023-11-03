from django.shortcuts import render,redirect
import json
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .models import Class, Teacher, Subject,Student,Parent,Fee,Grade


# Create your views here.

def index(request):
    return render(request,'index.html')

def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        class_id = request.POST.get('classroom')
        class_code = Class.objects.filter(class_id=class_id).first()
        stud = Student.objects.create(first_name=first_name,last_name=last_name,gender=gender,dob=dob,class_id=class_code)
        stud.save()
        stud.addmission_no = stud.id
        stud.save()
        redirect_url = reverse('parent_add')+f'?data={stud.id}'
        return HttpResponseRedirect(redirect_url)
    classes = Class.objects.all()
    context={
        'classes':classes
    }
    return render(request,'student.html',context)

def parent_add(request):
    data = request.GET.get('data')
    if request.method == "POST":
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('motherName')
        address = request.POST.get('address')
        phone_number = request.POST.get('fatherPhone')
        email = request.POST.get('email')
        student_id = request.POST.get('id')
        par = Parent.objects.create(father_name=father_name,mother_name=mother_name,address=address,phone_number=phone_number,email=email)
        par.save()
        stud = Student.objects.filter(pk=student_id)
        for i in stud:
            i.parent_id=par
            i.save()
        return redirect('index')
    return render(request,'parent.html',{"data":data})

def teacher(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        salary = request.POST.get('salary')
        hire_date = request.POST.get('hire_date')
        email = request.POST.get('email')
        # subject_id = request.POST.get('subject_id')
        # # Extracting Subject Info
        # sub_info = subject_id.split("-")
        teacher = Teacher.objects.create(
            first_name = first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            phone_no=phone_no,
            address=address,
            salary=salary,
            hire_date=hire_date,
            # subject_id=sub_info[0],
            # class_id=cls,kjsjdflak
            email=email
        )
        teacher.save()
        teacher.teacher_id = teacher.pk
        teacher.save()
        return redirect('show_student')

    try:
        classes = Class.objects.all()
    except classes.DoesNotExist:
        raise Http404('No class found to assign the teacher to')
    context = {"classes" : classes}
    return render(request,'teacher.html', context)

def show_student(request):
    if request.GET.get('q')!=None and request.GET.get('q')!='':
        q = request.GET.get('q')
        students = Student.objects.filter(addmission_no=q)
    else:
        students = Student.objects.all()
    context = {
        "students":students,
    }
    return render(request,'show_data_student.html',context)

def show_teacher(request):
    if request.GET.get('q')!=None and request.GET.get('q')!='':
        q = request.GET.get('q')
        teachers = Teacher.objects.filter(id=q)
    else:
        teachers = Teacher.objects.all()
    context = {
        "teachers":teachers,
    }
    return render(request,"show_data_teacher.html",context)

def edit_student(request,pk):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        pk = request.POST.get('id')
        classroom = request.POST.get('classroom')
        stud_id = Class.objects.filter(class_id=classroom).first()
        stud = Student.objects.filter(id=pk)
        for s in stud:
            s.first_name = first_name
            s.last_name = last_name
            s.gender = gender
            s.dob = dob
            s.class_id=stud_id
            s.save()
        return redirect('show_student')
    student = Student.objects.filter(id=pk)
    classes = Class.objects.all()
    context = {
        "students":student,
        "classes":classes
    }
    return render(request,'edit_student.html',context)

def edit_teacher(request,pk):
    if request.method == "POST":
        teacher_id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        phone_no = request.POST.get('phone_no')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        salary = request.POST.get('salary')
        hire_date = request.POST.get('hire_date')
        subject_id = request.POST.get('subject_id')
        email = request.POST.get('email')
        pk = request.POST.get('id')
        teach = Teacher.objects.filter(id=pk)
        for t in teach:
            t.teacher_id = teacher_id
            t.first_name = first_name
            t.last_name = last_name
            t.dob = dob
            t.phone_no = phone_no
            t.gender = gender
            t.address = address
            t.salary = salary
            t.hire_date = hire_date
            t.subject_id = subject_id
            t.email = email
            t.save()
        return redirect('show')
    teacher = Teacher.objects.filter(id=pk)
    context = {
        "teacher":teacher
    }
    return render(request,'edit_teacher.html',context)

def fees(request):
    if request.GET.get('q')!=None and request.GET.get('q')!='':
        q=request.GET.get('q')
        stud = Student.objects.filter(addmission_no__icontains=q)
    else:
        stud = Student.objects.all()
    context = {
        'students':stud,
    }
    return render(request, 'fees.html',context)

def fee_details(request,pk):
    if request.method == 'POST':
        fee_amount = request.POST.get('fee_amount')
        fee_type = request.POST.get('fee_type')
        student_id = request.POST.get('student_id')
        stud = Student.objects.filter(id=student_id).first()
        fee = Fee.objects.create(fee_amount=fee_amount,fee_type=fee_type,student_id=stud)
        fee.save()
        return redirect('fees')
    stud = Student.objects.filter(id=pk)
    context = {
        'students':stud
    }
    return render(request,'fee_details.html',context)

def marks_enter(request,sub,std):
    subject = Subject.objects.filter(subject_id=sub).first()
    student = Student.objects.filter(addmission_no=std).first()
    if request.method == "POST":
        date = request.POST.get('date')
        sub = request.POST.get('sub')
        subject = Subject.objects.filter(subject_id=sub).first()
        stud = request.POST.get('stud')
        student = Student.objects.filter(addmission_no=stud).first()
        marks = request.POST.get('marks')
        exam_type = request.POST.get('exam_type')
        grade = Grade.objects.create(score_no=marks,exam_date=date,student_id=student,subject_id=subject,exam_type=exam_type)
        grade.save()
        url = reverse('student_grade') + f'?id={subject.subject_id}'
        return redirect(url)
    context = {
        'subject':subject,
        'student':student
    }
    return render(request,'enter_marks.html',context)


from django.urls import reverse

def class_grades(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        class_id = request.POST.get('class_id')
        redirect_url = reverse('student_grade')+f'?id={id}&class_id={class_id}'
        return HttpResponseRedirect(redirect_url)
    chosen_class = request.GET.get('class')
    class_obj = Class.objects.filter(id=chosen_class).first()
    teacher = Teacher.objects.filter(class_id=class_obj)
    subs = []
    for teach in teacher:
        subs.extend(Subject.objects.filter(teacher=teach))
    classes = Class.objects.filter(class_id=chosen_class).first()
    context = {
        'class':classes,
        'subs': subs,
    }
    return render(request, 'class_grades.html', context)

def student_grade(request):
    if request.GET.get('q')!=None and request.GET.get('q')!='':
        q=request.GET.get('q')
        students = Student.objects.filter(addmission_no__icontains=q)
    else:
        students = Student.objects.all()
    sub_id = request.GET.get('id')
    class_id = request.GET.get('class_id')
    sub = Subject.objects.filter(subject_id=sub_id).first()
    classes = Class.objects.filter(class_id=class_id).first()
    print
    context = {
        'subject':sub,
        'students':students,
        'classes':classes
    }
    return render(request, 'student_grade.html',context)

def show_grades(request):
    if request.method == 'POST':
        chosen_class = request.POST.get('classroom')
        redirect_url = reverse('class_grades')+f'?class={chosen_class}'
        return HttpResponseRedirect(redirect_url)

    classes = Class.objects.all()
    context = {
        "classes": classes
    }
    return render(request, 'grades.html', context)

def view_student(request,pk):
    student = Student.objects.filter(addmission_no=pk).first()
    grades = Grade.objects.filter(student_id=pk)
    fees = Fee.objects.filter(student_id=pk)
    context={
        'student':student,
        'grades':grades,
        'fees':fees
    }
    return render(request,'view_student.html',context)

def show_classes(request):
    classes = Class.objects.all()
    context = {
        'classes':classes
    }
    return render(request,'classes.html',context)

def add_class(request):
    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        class_name = request.POST.get('class_name')
        if Class.objects.filter(class_id=class_id).exists():
            messages.error(request,"Id already exists!")
            return redirect('add_class')
        new_class = Class.objects.create(class_id=class_id,class_name=class_name)
        new_class.save()
        return redirect('show_classes')
    return render(request,'add_class.html')

def delete_student(request,pk):
    stud = Student.objects.filter(addmission_no=pk)
    stud.delete()
    return redirect('show_student')

def delete_teacher(request,pk):
    teach = Teacher.objects.filter(teacher_id=pk)
    teach.delete()
    return redirect('show_teacher')