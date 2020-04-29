from django.urls import path
from .views import complaint_detail,ComplaintCreateView,ComplaintUpdateView,ComplaintDeleteView, status_change

urlpatterns = [
    path('new/', ComplaintCreateView.as_view(), name='complaint-create'),
    path('<int:pk>/', complaint_detail, name='complaint-detail'),
    path('<int:pk>/update/', ComplaintUpdateView.as_view(), name='complaint-update'),
    path('<int:pk>/delete/', ComplaintDeleteView.as_view(), name='complaint-delete'),
    path('<int:pk>/status_change/', status_change, name='status-change'),
]