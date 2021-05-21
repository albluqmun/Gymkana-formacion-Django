from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('v1/allnews', views.noticiasV1, name='list_all_newsV1'),
    path('v1/news/create', views.createV1, name='create_newsV1'),
    path('v1/<int:new_id>/', views.detalle_noticiaV1, name='detailsV1'),
    path('v1/<int:new_id>/delete', views.borrar_noticiaV1, name='deletenewV1'),
    #-------------------------V2------------------
    path('v2/allnews', views.noticiasV2.as_view(), name='list_all_newsV2'),
    path('v2/<int:pk>/', views.detalle_noticiaV2.as_view(), name='detailsV2')]
