from django.db import models
from django.contrib.auth.models import User

class SocialMedia(models.Model):
    social_media_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = 'social_media_list_table'  

    def __str__(self):
        return self.social_media_name

class SocialMediaPlatformCredentials(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)  
    username = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True) 
    access_token=models.TextField(blank=True,null=True)
    inst_uid=models.CharField(max_length=255,blank=True,null=True)
    inst_progile_img=models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'social_media_credentials_table'  

    def __str__(self):
        return f"{self.username} on {self.social_media.social_media_name}"
