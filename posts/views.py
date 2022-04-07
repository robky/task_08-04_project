from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class APIPostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class APIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


'''
Напишите на основе дженериков два view-класса: APIPostList и APIPostDetail.
Опишите два эндпоинта:
api/v1/posts/,
api/v1/posts/<pk>/.

Через эти эндпоинты должны быть доступны любые операции с моделью Post:
POST-запрос на api/v1/posts/ создаст новую запись.
Запросы PUT, PATCH или DELETE к адресу api/v1/posts/<pk>/ удалят или изменят 
существующую запись.
GET-запрос на те же адреса вернёт список объектов или один объект.
'''


'''
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class APIPost(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIPostDetail(APIView):
    """Извлекает, обновляет или удаляет экземпляр Post."""
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

"""
Опишите код класса APIPostDetail(), наследующегося от APIView.
Этот класс должен обрабатывать запросы GET, PUT, PATCH и DELETE: возвращать, 
изменять или удалять отдельный объект модели Post.

В файл urls.py добавьте эндпоинт api/v1/posts/<int:pk>/, который будет 
вызывать view-класс APIPostDetail().
"""


"""
Напишите view-класс APIPost(), унаследовав его от APIView.

Он будет работать с queryset, содержащим все объекты модели Post. При 
POST-запросе этот класс должен создавать новый объект модели Post и возвращать 
его, а по GET-запросу должен возвращаться сериализованный список всех объектов 
модели Post.
"""