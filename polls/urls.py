from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    #idpoll
    path('<int:question_id>/', views.detail, name = 'detail' ),
    #results depois da poll
    path( '<int:question_id>/results/', views.results, name = 'results' ),
    #vote depois da poll
    path( '<int:question_id>/vote/', views.vote, name = 'vote' ),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
]