from django.contrib import admin
from .models import CustomUser, Party, Gift, Guest


@admin.register(CustomUser)
class AdminUser(admin.ModelAdmin):
    pass


@admin.register(Party)
class AdminParty(admin.ModelAdmin):
    readonly_fields = ('id',)


@admin.register(Gift)
class AdminGift(admin.ModelAdmin):
    readonly_fields = ('id',)


@admin.register(Guest)
class AdminGuest(admin.ModelAdmin):
    readonly_fields = ('id',)
