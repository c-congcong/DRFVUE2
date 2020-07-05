from django.urls import path

from user import views

urlpatterns = [
    path("user/", views.UserAPIView.as_view()),
    path("login/", views.UserAPIView.as_view()),
    path("emp/", views.Empview.as_view()),
    path("user/<str:pk>/", views.UserAPIView.as_view()),
    path("login/<str:pk>/", views.UserAPIView.as_view()),
    path("emp/<str:pk>/", views.Empview.as_view()),

]
