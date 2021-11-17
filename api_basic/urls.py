from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import  ArticleViewSet#,GenericAPIView#,ArticleAPIView,ArticleDetails#,article_list,article_detail

router = DefaultRouter()
router.register('article',ArticleViewSet,basename='article')


urlpatterns  =[
    #url for functions,decorator view
    # path('article/',article_list),
    # path('detail/<int:pk>/',article_detail)

    # url for class base view
    # path('article/',ArticleAPIView.as_view()),
    # path('detail/<int:id>/',ArticleDetails.as_view())

    #urls for generic
    # path('generic/article/',GenericAPIView.as_view()),
    # path('generic/article/<int:id>/',GenericAPIView.as_view()),

    # for viewswt # generic viewset
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls))



]