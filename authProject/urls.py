from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('preinscription/', views.preinscriptionView.as_view()),
    path('preinscriptionRead/', views.PreinscriptionReadListView.as_view()),
    path('results/', views.MatchesResultListView.as_view()),
    path('teamsread/', views.TeamsListView.as_view()),
    path('user/teamswrite/<int:pk>/', views.TeamsWriteView.as_view()),
]