from django.urls import path
from .views import *


app_name = 'note'

urlpatterns = [
        path(r'', index, name='index'),
        path(r'search/', search, name='search'),
        path(r'bookmarked/', bookmarked, name='bookmarked'),
        path(r'<str:id>/bookmark/', bookmark, name='bookmark'),
        path(r'create/', create, name='create'),
        path(r'<str:id>/delete/', delete, name='delete'),
        path(r'logout/', logout, name='logout')
]
