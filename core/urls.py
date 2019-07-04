from django.urls import path

from . import views

urlpatterns = [
    path('myownview/', views.MyOwnView.as_view(), name='myownview'),
    path('testcommentview/', views.TestCommentViewSet.as_view({'get': 'list'}), name='testcommentview'),
]
