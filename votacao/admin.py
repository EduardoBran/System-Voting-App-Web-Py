from django.contrib import admin

from .models import *

# admin.site.site_header = 'Admin de Projeto Votacao Private'
# admin.site.site_title = 'Projeto Votacao Area'
# admin.site.index_title = 'Welcome to the Projeto Votacao Admin Area'

@admin.action(description='Mostrar todas as enquetes de votação')
def mostrar_todos(modeladmin, requeust, queryset):
    queryset.update(show=True)

@admin.action(description='Não mostrar todas as enquetes de votação')
def nao_mostrar_todos(modeladmin, requeust, queryset):
    queryset.update(show=False)


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), (None, {'fields': ['show']})]
    inlines = [ChoiceInLine]

    list_display = [
        'question_text',
        'pub_date',
        'show'
    ]


    search_fields = [
        'question_text',   
    ]

    list_editable = [
        'show'
    ]

    list_filter = [
        'show'
    ]

    actions = [
        mostrar_todos,
        nao_mostrar_todos
    ]

admin.site.register(Question, QuestionAdmin)
