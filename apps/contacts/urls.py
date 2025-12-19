from django.urls import path
from .views import ContactCreateAPIView, ContactUpdateDestroyAPIView, TagsCreateAPIView, TagsDestroyAPIView, TagsListAPIView, SearchContactAPIView, ContactListAPIView


urlpatterns = [
    path('', ContactCreateAPIView.as_view(), name='contact-create'),
    path('update-delete/<int:pk>/', ContactUpdateDestroyAPIView.as_view(), name='contact-update-destroy'),
    path('tags/', TagsListAPIView.as_view(), name='tag-list'),
    path('tags/create/', TagsCreateAPIView.as_view(), name='tag-create'),
    path('tags/delete/<int:pk>/', TagsDestroyAPIView.as_view(), name='tag-destroy'),
    path('search/', SearchContactAPIView.as_view(), name='contact-search'),
    path('list/', ContactListAPIView.as_view(), name='contact-list'),
]