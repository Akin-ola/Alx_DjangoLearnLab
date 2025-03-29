from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    profile_picture = models.ImageField()

    def __str__(self):
        return f"Profile for {self.user.username}"
    
    class Meta:
        verbose_name= 'Profile'
        verbose_name_plural= 'Profiles'

@receiver(post_save, sender=User)
def update_or_create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)