from django.urls import path
from xml_upload import views

urlpatterns = [
    path('', views.Upload_xml, name='upload_aluno'),
    path('professor/', views.Upload_xml_professor, name='upload_professor'),

]