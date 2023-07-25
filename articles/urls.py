from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ArticleDD

router = DefaultRouter()
router.register(r'artlist', ArticleDD,basename="artlist")


urlpatterns = [
    # path('location/', LocationList.as_view()),
    # path('location/<int:pk>/', LocationDetail.as_view()),
    # path('item/', ItemList.as_view()),
    # path('item/<int:pk>/', ItemDetail.as_view()),
    # path('art-list/',ArticleList.as_view()),
    # path('art-list/<int:pk>/',ArticleDetail.as_view()),
    path('',include(router.urls)),
]