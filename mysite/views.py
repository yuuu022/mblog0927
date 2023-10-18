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
