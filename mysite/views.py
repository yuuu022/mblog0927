from django.shortcuts import render
from mysite.models import Post #mysite這個資料夾中匯入先前已設好的東西
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")
    except:
        return redirect("/")
import random
def about(request, num=-1):
    quotes=['今日事，今日畢',
            '要怎麼收穫，先那麼栽',
            '知識就是力量',
            '一個人的個性就是他的命運']    
    if num==-1 or num>4:
        quote = random.choice(quotes)
    else:
        quote = quotes[num]
    return render(request, 'about.html', locals())
    
    mhtml = f'''
<html>
<body>
<h1>I</h1>
<h3>am in NTUB</h3>
<h2>{num}</h2>
</body></html>
'''
    return HttpResponse(mhtml)
'''
def showpost(request, slug):
    post = Post.objects.get(slug=slug) 
    #select * from post where slug=%slug
    return render(request, 'post.html', locals())
'''    


'''
def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter,post in enumerate(posts):
        post_lists.append(f'No. {counter} {post} <br>') #Ff都可 格式化字串 <br>換行
    return HttpResponse(post_lists)
'''
