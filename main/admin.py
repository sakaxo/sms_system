from django.contrib import admin
from .models import Visitor,Member


# admin.site.unregister(Visitor)


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ("full_name","mobile","palce_of_resident","wish_to_be_a_member", "date_of_first_visit","current_place_of_fellowship")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("full_name","mobile","email","is_baptized","marital_status","occupation","palce_of_resident","wheer_to_serve")


