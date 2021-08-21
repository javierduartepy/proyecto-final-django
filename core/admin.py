from django.contrib import admin
from .models import Quiz

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Quiz, QuizAdmin)