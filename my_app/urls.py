from django.urls import path
from .views import HomePageView, CreateRowView, UpdateRowView, DeleteRowView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_'),
    path('create/', CreateRowView.as_view(), name='create_'),
    path('<int:pk>/update/', UpdateRowView.as_view(), name='update_'),
    path('<int:pk>/delete/', DeleteRowView.as_view(), name='delete_'),
]
