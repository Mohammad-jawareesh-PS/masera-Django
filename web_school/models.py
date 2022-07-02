
from django.db import models
class Class(models.Model):
     
     category = [
         ('basic stage','basic stage' ),
         ('eleventh grade','eleventh grade'),
         ('Twelfth grade','Twelfth grade')
     ] 
     name_class = models.CharField(max_length=250)
     category = models.CharField(max_length=50,choices=category)
     def __str__(self):
         return self.name_class
        

class Content(models.Model):
    name_content = models.CharField(max_length=250)
    img_content = models.ImageField(upload_to ="duty_Summary",null=True, blank=True)
    file = models.FileField(upload_to ="duty_file",null=True, blank=True)
    clas = models.ForeignKey(Class,models.SET_NULL,null=True, blank=True)
    def __str__(self):

        return f"{self.name_content}, {self.clas}"


# class Unit(models.Model):
#     name_unit = models.CharField(max_length=250)
#     category = models.ForeignKey(Content,models.SET_NULL,related_name="units",null=True, blank=True)
#     def __str__(self):
#          return self.name_unit   


class Duty(models.Model):
    name_duty = models.CharField(max_length=250)
    file = models.FileField(upload_to ="duty_file",null=True, blank=True)
    category = models.ForeignKey(Content, on_delete=models.SET_NULL,related_name='dutys',null=True, blank=True)
    def __str__(self):
         return self.name_duty


class Explain(models.Model):
    name_explain = models.CharField(max_length=250)
    file = models.FileField(upload_to ="Explain_file",null=True, blank=True)
    category = models.ForeignKey(Content, on_delete=models.SET_NULL,related_name='explains',null=True, blank=True)
    def __str__(self):
         return self.name_explain


class Exam(models.Model):
    name_exam= models.CharField(max_length=250)
    file = models.FileField(upload_to ="Exam_file",null=True, blank=True)
    category = models.ForeignKey(Content, on_delete=models.SET_NULL,related_name="exams",null=True, blank=True)
    def __str__(self):
         return self.name_exam


class Summary(models.Model):
    name_summary = models.CharField(max_length=250)
    file = models.FileField(upload_to ="Summary_file",null=True, blank=True)
    category = models.ForeignKey(Content, on_delete=models.SET_NULL,related_name='summarys',null=True, blank=True)
    def __str__(self):
         return self.name_summary 


class Chat(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=300,null=True, blank=True)
    Subject=models.CharField(max_length=150,null=True, blank=True)
    message = models.TextField(max_length=4000,null=True, blank=True)  
    def __str__(self):
        return self.name

        
# class ClassPivotContent(models.Model):
#     clas = models.ForeignKey(Class,models.SET_NULL,null=True, blank=True)
#     cont = models.ForeignKey(Content,models.SET_NULL,null=True, blank=True)


class User(models.Model):
    email=models.EmailField(max_length=300,unique=True)
    username =models.CharField(max_length=250,unique=True)
    password= models.CharField(max_length=100)
    def __str__(self):
        return self.username
             
  


               

    
