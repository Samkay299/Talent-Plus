from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls={
       'List': '/task-list/', #(to do objects we can use)
	   'Detail View': '/task-list/<str:pk>/',#(allows us to see one object based on id passed in)
	   'Create': '/task-create/',
	   'Update': '/task-update/<str:pk>/',
	   'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Post.objects.all().order_by('-id')
    serializer = PostSerializer(tasks, many=True)

    return Response(serializer.data)
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Post.objects.get(id=pk)
    serializer = PostSerializer(tasks, many=False)
    return Response(serializer.data)  

@api_view(['POST'])
def taskCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)   

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)   

# @api_view(['POST'])
# def taskUpdate(request, pk):
#     task = Post.objects.get(id=pk)
#     serializer = PostSerializer(instance=task, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data) 

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Post.objects.get(id=pk)
    task.delete()
    return Response('item successfully deleted!') 