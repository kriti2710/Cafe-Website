# Importing the admin module from Django
from django.contrib import admin

# Importing the models (Feedback, Registration, Menu) from the home app
from home.models import Feedback, Registration, Menu

# Registering the Feedback model with the admin interface
admin.site.register(Feedback)

# Registering the Registration model with the admin interface
admin.site.register(Registration)

# Registering the Menu model with the admin interface
admin.site.register(Menu)
