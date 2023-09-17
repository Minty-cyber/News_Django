#### NEWS APP ####
from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/edit/", NewsUpdateView.as_view(), name="news_edit"),
    path("<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
    path("<int:pk>/delete/", NewsDeleteView.as_view(), name="news_delete"),
    path("new/", NewsCreateView.as_view(), name="news_create"),
    path('', NewsListView.as_view(), name = 'news_list'),
    
]
