from django import forms
from django.forms import ModelForm

from contact.models import Contact
from django.utils.translation import gettext_lazy as _

from django.core.exceptions import NON_FIELD_ERRORS

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['user', 'phone', 'message']
        labels = {
            'user': 'Имя',
            'phone': 'Телефон',
            'message': 'Сообщуние',
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'required': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

        # widgets = {
        #     'user': forms.TextInput(attrs={
        #         'required': True,
        #         'placeholder': 'Say something...',
        #         'name': 'My name',
        #
        #     }),
        # }
