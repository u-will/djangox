from django.urls import path
from .views import DjangoxListView, DjangoxDetailView, DjangoxUpdateView, DjangoxDeleteView, DjangoxCreateView
# , DjangoxListAPI, DjangoxDetailAPI

urlpatterns = [
    path('', DjangoxListView.as_view(), name='djangox_list'),
    path('<int:pk>/', DjangoxDetailView.as_view(), name='djangox_detail'),
    path('<int:pk>/update/', DjangoxUpdateView.as_view(), name='djangox_update'),
    path('<int:pk>/delete/', DjangoxDeleteView.as_view(), name='djangox_delete'),
    path('create/', DjangoxCreateView.as_view(), name='djangox_create'),
]