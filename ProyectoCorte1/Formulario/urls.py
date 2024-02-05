from django.urls import path
from . import views

urlpatterns = [
    path('formulario/',views.fomulario,name="Formulario"),
    path('',views.subir,name='subir')
]