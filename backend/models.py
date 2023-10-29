from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.username
