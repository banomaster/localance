from django.contrib import admin
from freelancers.photographers.models import ListPhotographerSkills, ListPhotographerClients, Photographer

admin.site.register(ListPhotographerClients)
admin.site.register(ListPhotographerSkills)
admin.site.register(Photographer)