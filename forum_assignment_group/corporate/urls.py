from django.urls import path
from .views import(
    HomeView,AboutView,
    ExpertiseView,ContactView,
)
app_name="home"
urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('our-expertise/', ExpertiseView.as_view(), name='expertise'),
]