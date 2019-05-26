from django.urls import path

from . import views


urlpatterns = [
    path('items/create', views.create),  # 1
    path('items/<str:id>/add_vector', views.add_vector),  # 2
    path('items/<str:id>/information', views.information),  # 3
    path('items/show', views.show),  # 4
    path('items/<str:id>/download_image', views.download_image),  # 5
    path('items/<str:id>/remove', views.remove),  # 6
]
