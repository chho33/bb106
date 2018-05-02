from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_record, name='post_record'),
    path('add_record', views.add_record, name='add_record')
]
