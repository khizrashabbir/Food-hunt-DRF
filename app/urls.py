from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "foodhuntapis"

router = routers.DefaultRouter()
router.register('api/v1/gallery', views.MenuView,)
# router.register('api/v1/book-table', views.BookTableView,)
router.register('api/v1/blog', views.BlogView,)
router.register('api/v1/reviews', views.Review,)


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/book-table/', views.BookTableView.as_view())

]