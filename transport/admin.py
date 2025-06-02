from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, TransportOrganizer, Vehicle, Booking, TransportOption

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "role")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "role")

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "role", "is_staff", "is_active"]
    list_filter = ["role", "is_staff", "is_active"]
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "role", "password1", "password2"),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TransportOrganizer)
admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(TransportOption)
