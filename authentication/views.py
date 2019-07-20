# from django.shortcuts import render
# from rest_framework import generics
# from django.contrib.auth.models import User
# from rest_framework.response import Response
#
# class Userlist(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class CurrentUser(generics.RetrieveAPIView):
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)
