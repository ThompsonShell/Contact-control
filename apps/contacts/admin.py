from django.contrib import admin
from apps.contacts.models import Contact, Tag


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'user')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('user',)
admin.site.register(Contact, ContactAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts')
    search_fields = ('name',)
admin.site.register(Tag, TagAdmin)