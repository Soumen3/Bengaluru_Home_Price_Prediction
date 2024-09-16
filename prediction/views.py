from django.shortcuts import render
from .form import PredictionForm
from .model import artifacts
from django.http import JsonResponse

artifacts.load_model()


# Create your views here.
def home(request):
	context ={}
	if request.method == 'POST':
		location = request.POST.get('location')
		sqft = request.POST.get('sqft_living')
		bhk = request.POST.get('bedrooms')
		bath = request.POST.get('bathrooms')
		print(location, sqft, bhk, bath)
		price = artifacts.predict_price(location, sqft, bhk, bath)
		print(price)
		return JsonResponse({'price': price})
	context['form'] = PredictionForm()
	return render(request, 'home.html', context)

def get_locations(request):
	locations = artifacts.get_location_name()
	return JsonResponse({'locations': locations})


# def predict_home_price(request):
# 	print(request.GET)
# 	location = request.GET.get('location')

# 	return JsonResponse ({'price': 100})