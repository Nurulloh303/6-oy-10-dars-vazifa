from django.urls import path
from .views import (
    home, news_by_category, news_detail,
    save_comment, save_news, delete_news
)

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', news_by_category, name="news_by_category"),
    path('news/add/', save_news, name='add_news'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('news/comments/add/<int:news_id>/', save_comment, name='add_comment'),
    path('news/delete/<int:pk>/', delete_news, name='delete_news'),
]
