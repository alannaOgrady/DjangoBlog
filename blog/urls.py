from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),    # name can be referring to the view/url name
]