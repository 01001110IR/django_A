from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'age', 'email', 'password', 'is_active', 'profile_picture', 'bio', 'rating']

        widgets = {
            'password': forms.PasswordInput(),  # מאפשר הצפנת הסיסמה
        }
