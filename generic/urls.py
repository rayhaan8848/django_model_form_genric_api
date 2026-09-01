from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path("create/",CreateDataView.as_view(),name='create' ),
    path('update/<pk>',UpdateDetailView.as_view(),name='update'),
    path('delete/<pk>',DeleteDataView.as_view(),name='delete')
]