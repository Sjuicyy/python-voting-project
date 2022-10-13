from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index')
    path('<int:question_id>',views.detail,name='detail')
    path('<int:question_id/r>',views.results,name='results')
    path('',views.vote,name='vote')
]
