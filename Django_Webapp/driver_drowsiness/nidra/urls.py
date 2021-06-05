from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('developer', views.developer, name='developer'),
    path('api', views.detection_api, name='detection_api'),
    path('model', views.detection_model, name='detection_model'),
    path('video_feed_api', views.video_feed_api, name='video_feed_api'),
    path('video_feed_model', views.video_feed_model, name='video_feed_model')
]