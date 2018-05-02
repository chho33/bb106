from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.http import Http404

me = get_user_model().objects.get(username='admin')

# Create your views here.
def post_list(request):
    posts =   Post.objects.all().order_by('-created_date')
    post_form = PostForm()
    #return render(request,'blog/post_list.html',{'posts':posts,'post_form':post_form})
    return render(request,'blog/post_list.html',locals())

def add_record(request):
    if request.POST:
        title = request.POST['title']
        text = request.POST['text']
        newpost = Post.objects.create(author=me, title=title, text=text)
    return post_list(request)
    return redirect('/blog')

def add_record(request):
    if request.method == 'POST':
        posted_data = request.POST
        form = PostForm(posted_data)
        #form.save()
        post_form = form.save(commit=False)
        post_form.author = me
        post_form.save()
        #return redirect('/blog')
        return post_list(request)
    else:
        raise Http404("Abnormal behaviour detected!")

def post_record(request,id):
	post = Post.objects.get(id = id)
	return render(request, 'blog/post_record.html', locals())

def post_record(request,id):
    posts = Post.objects.filter(id__lte=id).order_by('-id')[:2]
    post = posts[0]
    next_post = posts[1] if len(posts) > 1 else None
    return render(request, 'blog/post_record.html', locals())
