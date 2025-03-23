from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfileForm, UpdateProfileForm, CreateViewForm, UpdateViewForm
from django.contrib.auth import authenticate, login
from .models import Profile, Post
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = CreateViewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = UpdateViewForm

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login_view')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form })


class ProfileView(DetailView):
    model = Profile
    
@login_required(login_url='login_view')
def profile_view(request):
    if request.method == 'POST':
        ...
    return render(request, 'blog/profile.html')


@login_required(login_url='login_view')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form1 = UpdateProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid or form1.is_valid:
            form.save()
            form1.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        form1 = UpdateProfileForm(instance=request.user.profile)
        forms = {
          'form': form,
          'form1': form1
          }
        return render(request, 'blog/profile_edit.html', forms)
    
