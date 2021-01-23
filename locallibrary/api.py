from rest_framework.response import Response
from .serailizers import UserSerializer
from .serailizers import PublicacionSerializer
from .serailizers import reaccionSerializer
from .serailizers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.views import ListAPIView
from rest_framework import status


class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReaccionAPI(APIView):
    def post(self, request):
        serializer = reaccionSerializer(data=request.data)
        if serializer.is_valid():
            reaccion = serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentAPI(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            Comment = serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicacionAPI(APIView):
    def post(self, request):
        serializer = PublicacionSerializer(data=request.data)
        if serializer.is_valid():
            pub = serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
