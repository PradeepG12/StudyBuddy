from django.contrib import admin
from django.apps import apps

def register_all_apps():
    models = apps.get_models()
    for model in models:
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass

register_all_apps()