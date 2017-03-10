from django.conf.urls import url, include
from mateupsite import views
urlpatterns = [

    url(r'^register/', views.RegisterPageView.as_view(), name='register'),
    url(r'^/', views.IndexPageView.as_view(), name='index'),
]