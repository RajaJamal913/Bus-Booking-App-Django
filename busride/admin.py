from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)

from django.contrib import admin
from django.contrib import admin
from .models import Ride

class RideAdmin(admin.ModelAdmin):
    list_display = ('pickup', 'destination', 'date', 'time', 'user')  # Display these fields in the admin list view
    list_filter = ('pickup', 'destination', 'date')  # Filters for the admin list view
    search_fields = ('pickup', 'destination', 'user__username')  # Allow search by these fields
    ordering = ('-date',)  # Order by date descending
    date_hierarchy = 'date'  # Enables a date hierarchy filter on the right side

    fieldsets = (
        (None, {
            'fields': ('pickup', 'destination', 'date', 'time', 'user')
        }),
    )

admin.site.register(Ride, RideAdmin)

