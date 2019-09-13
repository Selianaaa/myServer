from django.urls import path

from . import views


urlpatterns = [
    path('items/create', views.create),
    path('items/<str:id>/add_vector', views.add_vector),
    path('items/<str:id>/information', views.information),
    path('items/show', views.show),
    path('items/<str:id>/download_image', views.download_image),
    path('items/<str:id>/remove', views.remove),
]
