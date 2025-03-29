from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Post, Comment
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError


class CommentUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test(self):
        return self.request.user == Post.comment.author
    
    def no_perm(self):
        return HttpResponse('Only comment owner is allow to perform this operation')

# def comment_create_view(request, post):
#     if request.method == 'POST':
#         post = Post.objects.get(id=post.id)
#         form = forms.CommentCreateForm(request.POST, post)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy('posts'))
#     form = forms.CommentCreateForm()
#     return render(request, 'blog/comment_create.html', {'form': form})




class CommentCreateView(CreateView):
    model  = Comment
    template_name = 'blog/comment_create.html'
    form_class = forms.CommentForm
    success_url = reverse_lazy('posts')

def all_post_comment(request):
    comment = Comment.objects.all()
    return render(request, 'blog/post_comment.html', {'comment': comment})
    

# def comment_update_view(request, pk):
#     comment = Comment.objects.get(id=pk)
#     if request.method == 'POST':
#         form = forms.CommentUpdateForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy('post_comment'))
#     form = forms.CommentUpdateForm(instance=comment)
#     return render(request, 'blog/', {'form': form})

class CommentUpdateView(CommentUserMixin,UpdateView):
    model = Comment
    template_name = 'blog/comment_update.html'
    form_class = forms.CommentUpdateForm
    success_url = reverse_lazy('posts')


class CommentDeleteView(CommentUserMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'



# def login_view(request):
#     if request.method == 'POST':
#         login(request, user=request.user)
#         return redirect(reverse_lazy('posts'))
#     return render(request, 'blog/login.html')


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'blog/logout.html')
    return render(request, 'blog/login.html')

# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     context_object_name = 'all_post'
#     ordering = '-published_date'
    

def post_list_view(request):
    all_post = Post.objects.all()

    return render(request, 'blog/post_list.html', {'all_post': all_post})



# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post'


def post_detail_view(request, pk):
    post_id = Post.objects.get(id=pk)
    if post_id:
        all_comments = Comment.objects.all()
        if all_comments:
            return render(request, 'blog/post_detail.html', {'post': post_id, 'all_comments': all_comments})
        return render(request, 'blog/post_detail.html', {'post': post_id})
    return HttpResponse('Post doesn\'t exist')



# class PostCreateView(CreateView):
#     model = Post
#     template_name = 'blog/post_create.html'
#     form_class = CreateViewForm

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

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



class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = forms.PostUpdateForm


def update_post_view(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('posts'))
        
    form = forms.PostUpdateForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form, 'post_id': pk})

# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'blog/post_delete.html'
    

def delete_post_view(request, pk):
    post = Post.objects.get(id=pk)
    if post:
        post.delete()
    return redirect(reverse_lazy('posts'))


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


class ProfileView(DetailView):
    model = Profile
    
@login_required(login_url='login')
def profile_view(request):
    if request.method == 'POST':
        ...
    return render(request, 'blog/profile.html')


# @login_required(login_url='login_view')
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         form1 = UpdateProfileForm(request.POST, instance=request.user.profile)
#         if form.is_valid or form1.is_valid:
#             form.save()
#             form1.save()
#             return redirect('profile')
#     else:
#         form = EditProfileForm(instance=request.user)
#         form1 = UpdateProfileForm(instance=request.user.profile)
#         forms = {
#           'form': form,
#           'form1': form1
#           }
#         return render(request, 'blog/profile_edit.html', forms)
    
