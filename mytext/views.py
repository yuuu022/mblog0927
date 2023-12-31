from django.shortcuts import render, redirect
from mytext.models import Post, Mood, Profile     #mysite這個資料夾中匯入先前已設好的東西
from mytext.forms import ContactForm,  \
                         PostForm, \
                         UserRegisterform,  \
                         LoginForm, \
                         ProfileForm

# Create your views here.
def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    if request.user.is_authenticated:
        user_name= request.user.username
    else:
        user_name = '未登入'
    
    if request.method == 'GET':
        return render(request, 'myform.html', locals())
    elif request.method == 'POST':
        try:
            user_id = request.POST['user_id']
            user_pass = request.POST['user_pass']
            user_post = request.POST['user_post']
            user_mood = request.POST['mood']
            mood = Mood.objects.get(status=user_mood)
            post = Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
            post.save()
            message = f'成功儲存！請記得你的編輯密碼[{user_pass}]!，訊息需經審查後才會顯示。'
            return render(request, 'myform.html', locals())
        except Exception as e:
            message = '出現錯誤'
            return render(request, 'myform.html', locals())
    else:
        message = 'post/get 出現錯誤'
        return render(request, 'myform.html', locals())
    
def delpost(request, pid): #delpost() got multiple values for argument 'pid'
    if pid:
        try:
            post = Post.objects.get(id=pid)
            post.delete()
        except:
            print('刪除錯誤!! pid=',pid)
            pass
    return redirect('/test')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'myContact.html', locals())
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_vlaid():
            user_name = form.cleaned_data['user_name']
            print('user_name:', user_name)
        return render(request, 'myContact.html', locals())    
    else:
        message = "ERROR"
        return render(request, 'myContact.html', locals())

def post2db(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'post2db.html', locals())
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_vlaid():
            form.save()
            form = PostForm()
            message = f'成功儲存!請記得你的編輯密碼，訊息需經審查後才會顯示。'
        return render(request, 'myPost2DB.html', locals())    
    else:
        message = "ERROR"
        return render(request, 'myPost2DB.html', locals())

from django.contrib.auth.models import User

def register(request):
    if request.method == 'GET':
        form = UserRegisterform()
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            user_password_confirm = form.cleaned_data['user_password_confirm']
            if user_password == user_password_confirm:
                user = User.objects.create_user(user_name, user_email, user_password)
                message = f'註冊成功!'
            else:
                message='兩次密碼不一致！' 
        return render(request, 'register.html', locals())    
    else:
        message = "ERROR"
        return render(request, 'register.html', locals()) 

from django.contrib.auth import authenticate
from django.contrib import auth

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_password = form.cleaned_data['user_password']
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print("success")
                    message = '成功登入了'
                    return redirect('/')
                else:
                    message = '帳號尚未啟用'
            else:
                message = '登入失敗'

        return render(request, 'login.html', locals())
    else:
        message = "ERROR"
        return render(request, 'login.html', locals())

from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/') 
def profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.username
            try:
                user = User.objects.get(username=username)
                userinfo = Profile.objects.get(user=user)
                form = ProfileForm(userinfo)
            except:
                form = ProfileForm()
        return render(request, 'userinfo.html', locals())
    elif request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProfileForm()
            message = f'成功儲存！請記得你的編輯密碼!，訊息需經審查後才會顯示。'
        return render(request, 'userinfo.html', locals())
    else:
        message = "ERROR"
        print('出錯回首頁')
        redirect("/")
    