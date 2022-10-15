from django.urls import path, re_path
from . import views

urlpatterns = [
    
    path('submitted_complaints/', views.submitted_complaints, name='submitted_complaints'),
    path('report/', views.report, name='report'),
    path('post/',views.post,name='post' ),
    
]