from django.urls import path

from .views import index, by_rubric, rubrics ,BbCreateView, BbDetailView, BbEditView

app_name = 'bboard'

urlpatterns = [
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    path('edit/rubrics/', rubrics, name='edit_rubrics'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail')
    
]
