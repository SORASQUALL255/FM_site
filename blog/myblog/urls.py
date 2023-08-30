from django.urls import path
from . import views
from .views import MainView, ContactsView, FMVView, BazaView, SignUpView


urlpatterns = [
    path('', MainView.as_view(), name='bootstraptest'),
    path('Contacts/', ContactsView.as_view(), name='Contacts'),
    path('FMV/', FMVView.as_view(), name='FMV'),
    path('Baza/', BazaView.as_view(), name='Baza'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

