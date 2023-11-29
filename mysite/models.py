from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200) #標題 字元長度
    slug = models.CharField(max_length = 200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)#日期 auto_now=True自動取得現在時間
    
    class Meta:
        ordering = ('-pub_date',) #要跟上面變數名稱一樣 從大排到小
    
    def __str__(self) -> str: #__XX__ 是python 內建物建
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
class Product(models.Model):
    SIZES=(
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    )
    
    suk=models.CharField(max_length=5)
    name=models.CharField(max_length=20)
    price=models.PositiveIntegerField()
    size=models.CharField(max_length=1,choices=SIZES)
    
    