from django.urls import path
from . import views


urlpatterns = [
  path('', views.index), #/root, /r/view
  path('new', views.new)

]