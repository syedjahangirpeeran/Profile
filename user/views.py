from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from .models import Post,Comment
from .serializers import PostSerializer
# Create your views here.

def PostList(request):
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return JsonResponse(serializer.data, safe=False)
	
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PostSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

def index(request):
	try:
		all_post = Post.objects.all()[len(Post.objects.all())-10::1][::-1]
	except:
		all_post = Post.objects.all()[::-1]
	return render(request,'index.html',{'all_post':all_post})