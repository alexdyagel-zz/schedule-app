from django.contrib import admin

from main_app.models import BusFlight, TrainFlight

admin.site.register(BusFlight)
admin.site.register(TrainFlight)
