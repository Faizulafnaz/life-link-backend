from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializer import UserRegister, VarifyAccountSerializer
from .emails import sent_email_via_otp
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token'
        'api/token/refresh'
    ]
    return Response(routes)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['is_varified'] = user.is_varified
        token['email'] = user.email
        token['date_of_birth'] = user.date_of_birth
  

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class Register(APIView):

    def post(self, request, format=None):
        serializer = UserRegister(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        else:
            data=serializer.errors
        return Response(data)
    
    @permission_classes([IsAuthenticated])
    def patch(self, request, user_id):
       
        data = request.data
        user = get_object_or_404(CustomUser, pk=user_id)
    
        if 'profile_img' in request.FILES:
            user.profile_picture = request.FILES['profile_img']
            user.save()
         
        serializer = UserRegister(instance=user, data=data, partial=True)
        if serializer.is_valid():      
            serializer.save()
            print(serializer.data)


            return Response(serializer.data)
        return Response(serializer.errors) 
    
class VarifyOTP(APIView):
    def patch(self, request):
        data = request.data
        serializer = VarifyAccountSerializer(data = data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
