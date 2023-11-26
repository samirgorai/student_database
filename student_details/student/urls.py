from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('form/',views.form,name='form'),
    path('form/submit/',views.submit,name='submit'),
    path('Query/',views.query,name='Query'),
    path('Query/QueryResult/',views.querystudent,name='Query_result'),
    path('update/',views.update,name='update'),
    path('update/updateResultGet/',views.update_action_read,name='update_action_get'),
    path('update/updateResultPost/',views.update_action_update,name='update_action_post')   
]
