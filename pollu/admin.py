from django.contrib import admin

from .models import Question, Choice

# changing Admin title and heading in our backend
admin.site.site_header = "Poll Admin"
admin.site.site_title = "Poll Admin Area"
admin.site.index_title = "Welcome to Poll Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
# Register your models here.

admin.site.register(Question, QuestionAdmin)
