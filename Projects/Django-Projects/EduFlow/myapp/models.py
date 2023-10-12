from django.db import models

# Create your models here.

class Class(models.Model):
    class_id = models.CharField(max_length=10)
    class_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.class_name)

class Subject(models.Model):
    subject_id = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.subject_name)

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10,null=True,blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    phone_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=50)
    salary = models.CharField(max_length=7)
    hire_date = models.DateField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True) # subject Nam
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE,null=True,blank=True)
    email = models.CharField(max_length=30)

    def __str__(self):
        return str(self.first_name)
    

class Parent(models.Model):
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)

    def __str__(self):
        return str(self.father_name)


class Student(models.Model):
    addmission_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    addmission_date = models.DateField(auto_now_add=True,null=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE,null=True,blank=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.addmission_no)


class Grade(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score_no = models.CharField(max_length=10)
    exam_date = models.DateField()
    exam_type = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.student_id.addmission_no+"+"+self.subject_id.subject_name)

class Fee(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_amount = models.CharField(max_length=10)
    fee_type = models.CharField(max_length=100)
    payment_date = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.student_id.addmission_no)