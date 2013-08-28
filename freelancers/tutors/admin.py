from django.contrib import admin
from freelancers.tutors.models import ListTutorSkills, ListTutorClients, Tutor

admin.site.register(ListTutorSkills)
admin.site.register(ListTutorClients)
admin.site.register(Tutor)