from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home, name='home'),
	path('get_location_names/', views.get_locations, name='get_locations'),
	# path('predict_home_price/', views.predict_home_price, name='predict_home_price'),
]