from distutils import core
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
##########################################


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404.html', data)


def check(username, email):

    checkusername = User.objects.filter(username=username).count()
    checkemail = User.objects.filter(email=email).count()
    if checkusername > 0 or checkemail > 0:

        return True
    else:
        return False


def clas(request):
    cla = Class.objects.all()
    context = {
        'cla': cla,
    }
    return render(request, 'class.html', context)


@csrf_exempt
def chat(request):
    if request.method == 'POST':
        subject = request.POST['Subject']
        message = request.POST['message']
        sender = request.POST['email']
        send_mail(
            subject, f"الرسالة: {message}\n,المرسل: {sender}", f'{sender}+', ['zakreaemad999@gmail.com', 'basilmarof010@gmail.com', 'mohammadjawareesh059@gmail.com'], fail_silently=True,
        )
        return redirect('/')
    context = {
        'form': ChatForm
    }
    return render(request, 'chat.html', context)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST['email']
        if check(username, email) == True:
            messages.error(request, 'هذا الحساب موجود بلفعل')
        else:
            new_username = UserForm(request.POST)
            if new_username.is_valid():
                new_username.save()
                messages.success(request, 'تم انشاء حساب جديد بنجاح')
                return redirect('/')
    context = {
        'user': UserForm,
    }

    return render(request, 'signup.html', context)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cc = User.objects.all()

        for i in cc:
            if i.username == username and i.password == password:
                request.session['member_id'] = i.id

                return redirect('/')
        else:

            messages.error(request, 'خطأ في اسم المستخدم او كلمة المرور')

    context = {
        'user': UserForm,
    }
    return render(request, 'login.html', context)


def index(request):

    return render(request, "index.html", {})


def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return redirect('/')


def books(request, id):
    try:

        contents = Content.objects.filter(clas_id=id)
        categories = []
        categories1 = []
        exam = []
        explain = []
        for content in contents:
            categories_ = Explain.objects.filter(category=content)
            if categories_ not in categories and len(categories_) != 0:
                categories.append(categories_)
        for i in range(len(categories[0])):
            explain.append(categories[0][i])

        for content in contents:
            categories_ = Exam.objects.filter(category=content)
            if categories_ not in categories and len(categories_) != 0:
                categories1.append(categories_)
        for i in range(len(categories1[0])):
            exam.append(categories1[0][i])

        print("#")
        print(categories)
        print("#")
    except:
        return redirect('/')

    context = {
        'corce': contents,
        'explain': explain,
        'exam': exam,


    }
    return render(request, 'books.html', context)

    # for i in corce:
    #     explain=Explain.objects.filter(category=Content.objects.get(id=i.id))
    # for n in corce:
    #     exam=Exam.objects.filter(category=Content.objects.get(id=n.id))


#     with connection.cursor() as cursor:
#         check = cursor.execute(
#             f"select count(*) from web_school_signup where username='{username}'")
#   # get a single line from the result
#         row = cursor.fetchone()
#     # get the value in the first column of the result (the only column)
#         count_value = row[0]
#         print(count_value)
#     print('****************************************************************************')
#     print(check)
#     print(type(username))
#     print('****************************************************************************')

    # check=User.objects.raw(f'select count(username) from web_school_user where username={username}')
    # if check>0:
    #     return False
    # else:
    #     return True

    # 'unit':unit,
    # 'duty':duty,
    # 'explain':explain,
    # 'exam':exam,
    # 'summary':summary,

    # unit=Unit.objects.filter(category_id=id)
    # duty=Duty.objects.filter(category_id=id)
    # explain=Explain.objects.filter(category_id=id)
    # exam=Exam.objects.filter(category_id=id)
    # summary=Summary.objects.filter(category_id=id)

    # def corce(request,id):
    # data = ClassPivotContent.objects.filter(clas=Class.objects.get(id=id))
    # corce = []
    # for i in data:
    #     corce.append(Content.objects.get(pk=i.cont_id))
    # context = {
    #     'corce':corce,
    # }
    # return render(request,'corce.html',context)
