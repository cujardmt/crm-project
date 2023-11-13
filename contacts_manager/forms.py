from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        # Set required fields
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True
        self.fields['email'].required = True
        # Set optional fields (remove 'required' attribute)
        self.fields['phone'].required = False
