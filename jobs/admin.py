from django.contrib import admin
from .models import Job

#need to register the model to have it appear on the admin site
admin.site.register(Job)
