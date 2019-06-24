from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects #쿼리셋 (전달받은 객체) #메소드
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 2)#2개의 객체를 하나의 페이지로 삼겠다
    page = request.GET.get('page')#get으로 얻어낸 
    posts = paginator.get_page(page)
    return render(request, 'home.html',{'blogs': blogs, 'posts':posts})

def detail(request, blog_id):#detail은 두개의 인자를 받는다
    #pk란 데이터들을 구분시켜주는 수단
    blog_detail = get_object_or_404(Blog, pk = blog_id) 
    #blog_id번째 블로그 객체 detail함수에는 특정번호의 객체를 담을 수 있어야한다
    return render(request, 'detail.html',{'blog':blog_detail})

def new(request):#new.html 띄워
    return render(request, 'new.html')

def create(request):#입력받은 함수를 데이터베이스에 넣어준당
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))#다처리한 후 url로 넘기세요 ,url은 항상 str

