from django.views.generic import ListView
from categories.models import Category

class CategoriesInCityList(ListView):
	#queryset = Category.objects.all()
	queryset = Category.objects.filter(cities__name='Copenhagen')
	context_object_name = 'categories'	


