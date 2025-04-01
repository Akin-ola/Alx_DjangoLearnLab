from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Post, Comment
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class CommentUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test(self):
        return self.request.user == Post.comment.author
    
    def no_perm(self):
        return HttpResponse('Only comment owner is allow to perform this operation')


def all_post_comment(request):
    comment = Comment.objects.all()
    return render(request, 'blog/post_comment.html', {'comment': comment})
    

def update_comment_view(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.CommentUpdateForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('post_detail'))
    form = forms.CommentUpdateForm(instance=comment)
    return render(request, 'blog/comment_update.html', {'form': form, 'comment_id': pk})


def delete_comment_view(request, pk):
    comment = Comment.objects.get(id=pk)
    if comment:
        comment.delete()
    return redirect(reverse_lazy('post_detail'))


@login_required(login_url='login')
def post_create_view(request):
    if request.method == 'POST':
        form = forms.PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user != post.author:
                raise ValidationError('Logged in user must be the author of the post.')
            Post.objects.create(title=post.title, content=post.content, author=post.author)
            return redirect(reverse_lazy('posts'))
    form = forms.PostCreateForm()
    return render(request, 'blog/post_create.html', {'form': form})


def post_list_view(request):
    all_post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'all_post': all_post,})


def post_detail_view(request, pk):
    post_id = Post.objects.get(id=pk)
    if post_id:
        all_comments = Comment.objects.filter(post=post_id).order_by('-created_at')
        print(all_comments.count())
        form = forms.CommentForm()
        return render(request, 'blog/post_detail.html', {'post': post_id, 'all_comments': all_comments, 'form': form})
    return HttpResponse('Post doesn\'t exist')


def update_post_view(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('posts'))
    form = forms.PostUpdateForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form, 'post_id': pk})


def delete_post_view(request, pk):
    post = Post.objects.get(id=pk)
    if post:
        post.delete()
    return redirect(reverse_lazy('posts'))


class CommentCreateView(CreateView):
    model  = Comment
    template_name = 'blog/post_detail.html'
    form_class = forms.CommentForm
    success_url = reverse_lazy('post_detail')

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            print(kwargs)
            content = form.cleaned_data.get('content')
            current_user = User.objects.get(id=request.user.id)
            post_id = Post.objects.get(id=kwargs.get('pk'))
            print(content)
            print(current_user)
            print(post_id)
            
            Comment.objects.create(content=content, author=current_user, post=post_id)
        return redirect(reverse_lazy('post_detail', kwargs={'pk': post_id.id})) 


# class CommentUpdateView(CommentUserMixin,UpdateView):
#     model = Comment
#     template_name = 'blog/comment_update.html'
#     form_class = forms.CommentUpdateForm
#     success_url = reverse_lazy('posts')


# class CommentDeleteView(CommentUserMixin, DeleteView):
#     model = Comment
#     template_name = 'blog/comment_delete.html'


# class PostCreateView(CreateView):
#     model = Post
#     template_name = 'blog/post_create.html'
#     form_class = forms.PostCreateForm

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
    

# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     context_object_name = 'all_post'
#     ordering = '-published_date'
    

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post_id = context['object'].id
#         context['all_comments'] = Comment.objects.filter(post=post_id)
#         context['form'] = forms.CommentForm()
#         return context 


# class PostUpdateView(UpdateView):
#     model = Post
#     template_name = 'blog/post_update.html'
#     form_class = forms.PostUpdateForm


# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'blog/post_delete.html'


# class ProfileView(DetailView):
    # model = Profile


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect(reverse_lazy('posts'))
#     form = AuthenticationForm()
#     return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'blog/logout.html')
    return render(request, 'blog/login.html')


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse_lazy('posts'))
    else:
        form = forms.RegisterForm()
    return render(request, 'blog/register.html', {'form': form })


@login_required(login_url='login')
def profile_view(request):
    profile_id = Profile.objects.get(user=request.user)
    return render(request, 'blog/profile.html', {'profile_id': profile_id})


@login_required(login_url='login_view')
def edit_profile(request):
    if request.method == 'POST':
        form = forms.ProfileEditForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('profile'))
    else:
        form = forms.ProfileEditForm(instance=request.user.profile)
        return render(request, 'blog/profile_edit.html', {'form': form})
    
