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
        # data = {}
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            sent_email_via_otp(data['email'])
            # data['response'] = 'registered'
            # data['username'] = account.username
            # data['email'] = account.email
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
    def post(self, request):
        try:
            data = request.data
            serializer = VarifyAccountSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                try:
                    user = CustomUser.objects.get(email = email)
       
                    if user.otp != otp:
                        return Response({
                            'status' : 400,
                            'message': 'something went wrong',
                            'data':'wrong otp'
                        })
                    else:
                        user.is_varified = True
                        user.save()
                        return Response({
                            'status' : 200,
                            'message': 'account varified',
                            'data': {}
                        })
                except:
                    return Response({
                            'status' : 400,
                            'message': 'something went wrong',
                            'data':'invalid email id'
                        })
        except Exception as e:
            print(e)

