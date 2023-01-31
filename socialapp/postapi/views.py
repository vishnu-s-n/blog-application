from multiprocessing import context
from urllib import response
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from postapi.models import UserProfile,Posts
from postapi.serializers import UserProfileSerializer, UserSerializer,PostSerializer,CommentSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.decorators import action

# Create your views here.

class UserRegistrationView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserProfileView(ModelViewSet):
    serializer_class=UserProfileSerializer
    permission_classes=[permissions.IsAuthenticated]
    queryset=UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=UserProfileSerializer(data=request.data,context={"user":request.user})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["post"],detail=True)
    def follow(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        add_to_follow=User.objects.get(id=id)
        profile=UserProfile.objects.get(user=request.user)
        profile.followings.add(add_to_follow)
        return Response({"msg":"ok"})


    @action(methods=["get"],detail=False)
    def my_following(self,request,*args,**kwargs):
        user=request.user
        user_profile=UserProfile.objects.get(user=user)
        followings=user_profile.followings.all()
        # followings=request.user.following.all()
        serializer=UserSerializer(followings,many=True)
        return Response(data=serializer.data)

        
    

class PostView(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Posts.objects.all()
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=["post"],detail=True)
    def add_comment(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        user=request.user
        serializer=CommentSerializer(data=request.data,context={"user":user,"post":post})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return response(data=serializer.errors)

    @action(methods=["get"],detail=True)
    def get_comment(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        comment=post.comments_set.all()
        serializer=CommentSerializer(comment,many=True)
        return Response(data=serializer.data)


    @action(methods=["post"],detail=True)
    def add_like(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        post.liked_by.add(request.user)
        return Response({"msg":"ok"})


    