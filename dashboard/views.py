from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SocialMediaPlatformCredentials, SocialMedia
from services.instaServices import getUserInfo,getInstaPost
from django.shortcuts import render, get_object_or_404
import pdb


def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    user = request.user
    social_media_profile = get_object_or_404(SocialMediaPlatformCredentials, id=1, user=request.user)
    posts=getInstaPost(social_media_profile.access_token)
    print(posts['data'])
    return render(request, 'dashboard.html',{'insta_post': len(posts['data'])})

@login_required
def analytics(request):
    return render(request, 'dashboard/analytics.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validate passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'auth/register.html')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return render(request, 'auth/register.html')

        # Create user
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login') 
    return render(request, 'auth/register.html')


def password_reset(request):
    if request.method == "POST":
        pass
    return render(request, 'password_reset.html')


def create_social_media_platform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        access_tokens=request.POST.get('access_tokens')
        if access_tokens:
            instaData=getUserInfo(access_tokens)            
        else:
            messages.success(request, 'Please Enter your access token for now.')
            return redirect('dashboard')
        
        social_media_id = request.POST.get('social_media')
        if username and password and social_media_id:
            social_media = SocialMedia.objects.get(id=social_media_id)
            SocialMediaPlatformCredentials.objects.create(
                user=request.user,  
                social_media=social_media,
                username=instaData['username'],
                inst_uid=instaData['instaUid'],
                password=password, 
                access_token=access_tokens,
                inst_progile_img=instaData['instProfileImg']
            )
            messages.success(request, 'Platform added successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill out all fields.')
    social_media_list = SocialMedia.objects.all()
    return render(request, 'create_social_media_platform.html', {
        'social_media_list': social_media_list
    })

@login_required
def SocialMediaProfile(request, id):
    social_media_profile = get_object_or_404(SocialMediaPlatformCredentials, id=id, user=request.user)
    return render(request, 'social_media/profile.html', {'social_media_profile': social_media_profile})

@login_required
def insta_posts(request, id):
    social_media_profile = get_object_or_404(SocialMediaPlatformCredentials, id=id, user=request.user)
    posts=getInstaPost(social_media_profile.access_token)
    print(posts)
    return render(request, 'social_media/instaPost.html', {'posts': posts,'social_media_profile': social_media_profile})