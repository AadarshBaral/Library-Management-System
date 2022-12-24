from django.contrib import admin
from .models import Book,Category,Issued

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    readonly_fields = ["first_added"]

@admin.register(Issued)
class IssuedAdmin(admin.ModelAdmin):
    list_display = ('taker','book_name')

admin.site.register(Category)
