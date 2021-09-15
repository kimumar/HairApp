from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Setting, BookingMessage, BookingForm, CommentMessage, CommentForm, Post, PostForm
from user.decorators import unauthenticated_user, allowed_users

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for booking with us.")
            return redirect('/')
    
    setting = Setting.objects.get(pk=1)
    form = BookingForm

    context = {
        'form': form,
        'setting': setting,
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')



def blog(request):
    posts = Post.objects.all()
    setting = Setting.objects.get(pk=1)

    context = {
        'posts':posts,
        'setting': setting,
    }

    return render(request, 'blog.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def create(request):
    post = PostForm()
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES)
        if post.is_valid():
            post.save()
        return redirect('/blog')

    context = {
        'post':post,
    }
    return render(request, 'create.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def update(request, pk):

    blog = Post.objects.get(id=pk)
    post = PostForm(instance=blog)

    if request.method == 'POST':
        post = PostForm(request.POST, instance=blog)
        if post.is_valid():
            post.save
        return redirect('/blog')


    

    context = {
        'post':post,
        
    }
    return render(request, 'create.html', context)

@login_required
def updates(request, pk):
    blogs = CommentMessage.objects.get(id=pk)
    comment = CommentForm(instance=blogs)

    if request.method == 'POST':
        comment = CommentForm(request.POST, instance=blogs)
        if comment.is_valid():
           comment.save
        

    context = {
        'comment':comment,
        
    }
    return render(request, 'comment-update.html', context)

# @login_required
# def blogs(request, pk):
#     post = Post.objects.get(id=pk)
#     comments = CommentMessage.objects.all()
#     setting = Setting.objects.get(pk=1)

#     comment = CommentForm()
#     if request.method == 'POST':
#         comment = CommentForm(request.POST)
#         if comment.is_valid():
#             comment.save()
        
    


#     context = {
#         'post':post,
#         'comments':comments,
#         'comment':comment,
#         'setting': setting,
#     }

#     return render(request, 'blog-single.html', context)

@login_required
def blogs(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.filter(active=True)
    setting = Setting.objects.get(pk=1)
    comment = None
    # Comment posted
    if request.method == 'POST':
        comment= CommentForm(data=request.POST)
        if comment.is_valid():

            # Create Comment object but don't save to database yet
            comment = comment.save(commit=False)
            # Assign the current post to the comment
            comment.post = post
            # Save the comment to the database
            comment.save()
    else:
        comment = CommentForm()


    context = {
        'post':post,
        'comments':comments,
        'comment':comment,
        'setting': setting,
    }

    return render(request, 'blog-single.html', context)



@login_required
def deleteco(request, pk):
    comments = CommentMessage.objects.get(id=pk)

    if request.method == "POST":
        comments.delete()
        return redirect('blog')


    context = {
        'comments':comments,
    }

    return render(request, 'confirm_delete.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def delete(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "POST":
        post.delete()
        return redirect('/blog')


    context = {
        'post':post,
    }

    return render(request, 'confirm_delete.html', context)



def gallery(request):
    setting = Setting.objects.get(pk=1)

    context = {
        'setting':setting,
    }
    return render(request, 'gallery.html', context)

def services(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for booking with us.")
            return redirect('/services')
    
    form = BookingForm

    context = {
        'form': form,
    }
    return render(request, 'services.html', context)


