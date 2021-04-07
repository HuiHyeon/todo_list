from rest_framework import viewsets
from .serializers import TodoSerializer, CommentSerializer
from .models import Todo, Comment
from rest_framework.filters import SearchFilter
# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    filter_backends = [SearchFilter]
    search_fields = ['is_completed']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from todos.models import Todo, Comment
# from todos.serializers import TodoSerializer, CommentSerializer


# @api_view(['GET', 'POST'])
# def todo_list(request):
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def todo_detail(request, pk):
#     try:
#         todos = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TodoSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TodoSerializer(todos, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         todos.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def comment_list(request):
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def comment_detail(request, pk, comment):
#     try:
#         comments = Comment.objects.get(pk=comment)
#     except Comment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CommentSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CommentSerializer(comments, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         comments.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
