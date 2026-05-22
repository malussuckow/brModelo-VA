from django.urls import path 
from corretor.views import Comparar_xml

urlpatterns = [
    path('', Comparar_xml, name='corretor')
]


