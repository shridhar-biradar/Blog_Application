from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Blog
from django.contrib.auth import get_user_model
from .serializers import BlogSerializer, UserSerializer
from django.http import JsonResponse
from django.core.paginator import Paginator
import json

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(author=request.user).order_by('-created_at')
        message = "No blogs yet. Please create one." if not blogs.exists() else ""
    else:
        blogs = Blog.objects.all().order_by('-created_at')
        message = "Please register and create your blog." if not blogs.exists() else ""
    paginator = Paginator(blogs, 5)  # Paginate with 5 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'blogs': blogs,'page_obj': page_obj,'message': message,
        'blogs_exist': blogs.exists()})

def signup_view(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')

@login_required
def create_blog_view(request):
    return render(request, 'create_blog.html')

def blog_detail_view(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'blog_detail.html', {'blog': blog})


@login_required
def edit_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if blog.author != request.user:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    if request.method == 'POST':
        data = json.loads(request.body)
        blog.title = data.get('title')
        blog.content = data.get('content')
        blog.save()
        return JsonResponse({'message': 'Blog updated successfully'})

    return render(request, 'edit_blog.html', {'blog': blog})

@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if blog.author != request.user:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    blog.delete()
    return redirect('index')


@api_view(['POST'])
def register_user(request):
    data = request.data
    if User.objects.filter(username=data['username']).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    
    return Response({'message': 'User registered successfully'})


@api_view(['POST'])
def api_login_user(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    try:
        user_obj = User.objects.get(email=email)
        user = authenticate(username=user_obj.username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=400)


@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response({'message': 'Blog created successfully'})
    return Response(serializer.errors, status=400)

