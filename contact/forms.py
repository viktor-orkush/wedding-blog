from django.forms import ModelForm
from contact.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['user', 'phone', 'message']
        labels = {
            'user': 'Имя',
            'phone': 'Телефон',
            'message': 'Сообщение',
        }
