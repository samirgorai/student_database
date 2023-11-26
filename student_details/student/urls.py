from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('form/',views.form,name='form'),
    path('submit/',views.submit,name='submit'),
]
