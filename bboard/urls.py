from django.urls import path

from .views import index, by_rubric, BbCreateView, BbDetailView, BbEditView

urlpatterns = [
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail')
    
]
