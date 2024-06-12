from django.contrib import admin
from .models import Note, Author, Colour

# Register your models here.

# Note model.
admin.site.register(Note)

# Author model.
admin.site.register(Author)

# Colour model.
admin.site.register(Colour)
