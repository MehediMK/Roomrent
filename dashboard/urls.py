from django.urls import path
from .views import index,post_filter

urlpatterns = [
    path('',index,name='index'),
    path('orderby/',post_filter,name='orderby'),
]