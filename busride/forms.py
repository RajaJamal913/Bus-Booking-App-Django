# forms.py

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Ensure the password is hashed
        if commit:
            user.save()
            UserProfile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
        return user
