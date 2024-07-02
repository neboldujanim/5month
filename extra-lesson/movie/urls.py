from django.urls import path
from .views import (MovieView, ReviewView, Directorview)
from .const import RETRIEVE_UPDATE_DESTROY, LIST_CREATE

urlpatterns = [
   path('', MovieView.as_view(LIST_CREATE)),
   path('<int:pk>/', MovieView.as_view(RETRIEVE_UPDATE_DESTROY)),
   path('reviews/', ReviewView.as_view(LIST_CREATE)),
   path('reviews/<int:pk>/', ReviewView.as_view(RETRIEVE_UPDATE_DESTROY)),
   path('directors/', Directorview.as_view(LIST_CREATE)),
   path('directors/<int:pk>/', Directorview.as_view(RETRIEVE_UPDATE_DESTROY)) ,
]

