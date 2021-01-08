from django.urls import path,include
from .views import HomePage,DetailsPage,CreatePage,UpdatePage,DeletePage

urlpatterns = [
    path('', HomePage.as_view(), name ='home'),
    path('<int:pk>/', DetailsPage.as_view(), name ='details'),
    path('new/', CreatePage.as_view(), name='create_sample'),
    path('<int:pk>/edit/', UpdatePage.as_view(), name='update_sample'),
    path('<int:pk>/delete/', DeletePage.as_view(), name='delete_sample')
]