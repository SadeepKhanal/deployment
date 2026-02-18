from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
urlpatterns=[
    path("token/",TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('dashboard/', views.DashboardAPIView.as_view(), name='dashboard'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]