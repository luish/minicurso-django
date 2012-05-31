from django.contrib import admin
from agenda.models import ItemAgenda

#class ItemAgendaAdmin(admin.ModelAdmin):
#	fields = ['data', 'titulo']

#admin.site.register(ItemAgenda, ItemAgendaAdmin)
admin.site.register(ItemAgenda)
