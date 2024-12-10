from django.contrib import admin
from .models import SocialMedia, SocialMediaPlatformCredentials

# Register the SocialMedia model
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('social_media_name', 'created_at', 'updated_at')
    search_fields = ('social_media_name',)
    ordering = ('-created_at',)


# Register the SocialMediaPlatformCredentials model
@admin.register(SocialMediaPlatformCredentials)
class SocialMediaPlatformCredentialsAdmin(admin.ModelAdmin):
    list_display = ('user', 'social_media', 'username', 'created_at', 'updated_at')
    search_fields = ('username', 'social_media__social_media_name', 'user__username')
    ordering = ('-created_at',)
    list_filter = ('social_media', 'created_at')
