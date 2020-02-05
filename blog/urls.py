from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.all_post, name='all_post'),
    path('<slug>/', views.post, name='post'),
]
