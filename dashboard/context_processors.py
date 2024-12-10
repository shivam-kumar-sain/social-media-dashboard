from .models import SocialMediaPlatformCredentials,SocialMedia

def sidebar_data(request):
    if request.user.is_authenticated:
        user_platforms = [
            {
                "social_media_name": "Facebook",
                "username": "test_facebook_user",
            },
            {
                "social_media_name": "Twitter",
                "username": "test_twitter_user",
            },
        ]
        user_platforms = SocialMediaPlatformCredentials.objects.filter(user=request.user)

    else:
        user_platforms = None

    return {
        'user_platforms': user_platforms,  # This will be accessible in all templates
    }

def social_media_list(request):
    social_media_list = SocialMedia.objects.all()
    return {
        'social_media_list': social_media_list,  # Pass the list to the context
    }
