from django import forms
from django.contrib.auth.models import User

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'contacts']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        # Set required fields
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True
        self.fields['email'].required = True
        # Set optional fields (remove 'required' attribute)
        self.fields['phone'].required = False
        self.fields['address'].required = False


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, *kwargs)

        self.fields['username'].required = True
        self.fields['password'].required = True
        self.fields['last_name'].required = False
        self.fields['email'].required = False

