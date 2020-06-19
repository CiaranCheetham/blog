from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, CVForm
from .models import Post, Comment, CVSection


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
        .order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def cv_view(request):  # Will need to add pk later on?
    exp_obj = get_object_or_404(CVSection, pk='exp')
    profile_obj = get_object_or_404(CVSection, pk='profile')
    education_obj = get_object_or_404(CVSection, pk='education')
    projects_obj = get_object_or_404(CVSection, pk='projects')
    interests_obj = get_object_or_404(CVSection, pk='interests')

    return render(request, 'cvtemplates/cv_view.html',
                  {'exp': exp_obj,
                   'profile': profile_obj,
                   'education': education_obj,
                   'projects': projects_obj,
                   'interests': interests_obj})


def cv_edit(request, pk):
    section = get_object_or_404(CVSection, pk=pk)
    if request.method == "POST":
        form = CVForm(request.POST, instance=section)
        if form.is_valid():
            new_section = form.save(commit=False)
            new_section.save()
            return redirect('cv_view')
    else:
        form = CVForm(instance=section)
    return render(request, 'cvtemplates/cv_edit.html', {'form': form})

