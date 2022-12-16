from django.urls import path
from .views import mho,lo,Registr

urlpatterns = [
    path('mho/',mho),
    path('lo/',lo),
    path('registr/',Registr.as_view(),name="Registr")
]
