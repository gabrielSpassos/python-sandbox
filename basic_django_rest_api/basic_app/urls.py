from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='Music API')

urlpatterns = [
    path('swagger/', schema_view),

    path('musics/', views.MusicList.as_view(), name='music-list'),
    path('musics/<int:pk>/', views.MusicDetail.as_view(), name='music-detail'),

    path('albums/', views.AlbumList.as_view()),
    path('albums/<int:pk>/', views.AlbumDetail.as_view()),

    path('bands/', views.BandList.as_view()),
    path('bands/<int:pk>/', views.BandDetail.as_view()),

    path('members/', views.MemberList.as_view()),
    path('members/<int:pk>/', views.MemberDetail.as_view()),
]
