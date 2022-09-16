from django.urls import path
from .views import ClientListView, ClientDetailView

urlpatterns = [
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client')
]