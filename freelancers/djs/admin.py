from django.contrib import admin
from freelancers.djs.models import ListDJOccasions, ListDJGenres, DJ

admin.site.register(ListDJOccasions)
admin.site.register(ListDJGenres)
admin.site.register(DJ)