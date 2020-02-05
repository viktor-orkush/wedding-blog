from django.urls import path

from contact import views

app_name = "contact"

urlpatterns = [
    # path('', views.contact_form, name='contact_form')
    path('', views.CustomerAddContact.as_view(), name='contact_form')
]