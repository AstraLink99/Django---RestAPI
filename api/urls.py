from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("students/", views.StudentListView.as_view()),
    path("students/<int:pk>", views.StudentDetailsView.as_view()),
    path("studentdelete/<int:pk>", views.StudentDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]  



    