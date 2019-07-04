from django.urls import path

from core import views

urlpatterns = [
    path('myownview/', views.MyOwnView.as_view(), name='myownview'),
    path('testcommentview/', views.TestCommentViewSet.as_view({'get': 'list'}), name='testcommentview'),
    path('launchpadview/', views.LaunchpadViewSet.as_view({'get': 'list'}), name='launchpadview'),
]
