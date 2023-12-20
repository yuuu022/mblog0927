from django.shortcuts import render, redirect
from mytext.models import Post, Mood     #mysite這個資料夾中匯入先前已設好的東西
from mytext.forms import ContactForm

# Create your views here.
def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    print(moods)
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
    
def delpost(pid): #delpost() got multiple values for argument 'pid'
    if pid:
        try:
            post = Post.objects.get(id=pid)
            post.delete()
        except:
            print('刪除錯誤!! pid=',pid)
            pass
    return redirect('/')

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
