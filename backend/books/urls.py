from cgitb import lookup
from urllib.parse import urlparse

from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('api/books',views.BooksViewSet)


# books_router = routers.NestedDefaultRouter(router, 'api/books', lookup='book')
# books_router.register('images', views.BooksViewSet, basename='book-images')



urlpatterns = router.urls 
# + books_router.urls 
