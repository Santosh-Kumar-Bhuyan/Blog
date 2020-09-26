from django.shortcuts import render, HttpResponse
from datetime import datetime
from myblog.models import Contact
from myblog.models import Post
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
   # return HttpResponse("This is Home")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        contact = Contact(name=name, email=email, msg=msg, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')
    #return HttpResponse("This is Contact")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is About")

def post(request):
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request, 'post.html', context)
    #return HttpResponse("This is Post")
def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post' : post}
    return render(request, 'blogpost.html', context)