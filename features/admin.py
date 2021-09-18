from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    pass

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : {
            'widget':TinyMCE()
        },
    }

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : {
            'widget':TinyMCE()
        },
    }

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(gallery)
class galleryAdmin(admin.ModelAdmin):
    pass

@admin.register(events)
class eventsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : {
            'widget':TinyMCE()
        },
    }
