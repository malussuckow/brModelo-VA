from django.urls import path
from xml_upload import views

urlpatterns = [
    path('', views.upload_xml, name='upload_aluno'),
    path('professor/', views.upload_xml_professor, name='upload_professor'),

]