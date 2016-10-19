from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice
from .models import Survey

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['survey','question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Choice)
