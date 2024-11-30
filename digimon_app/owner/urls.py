from django.urls import path
from . import views
urlpatterns = [
    path('owner_list/', views.owner_list, name='owner_list'),

    path('owner_detail/<int:id_owner>', views.owner_detail, name='owner_detail'),

    path('owner_search/', views.owner_search, name='owner_search'),

    path('owner_create/', views.owner_create, name='owner_create'),

    path('owner_details/', views.owner_details, name='owner_details'),

    path('owner_delete/<int:id_owner>', views.owner_delete, name='owner_delete'),

    path('owner_edit/<int:id_owner>', views.owner_edit, name='owner_edit'),
]