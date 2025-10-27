

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializers import UserRegistrationSerializer, UserSerializer, UserLoginSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])  # Anyone can access (no login required)
def signup_view(request): 
    serializer = UserRegistrationSerializer(data=request.data)
   
    if serializer.is_valid():
        
        user = serializer.save()  
        
       
        login(request, user)
        
       
        return Response({
            'user': UserSerializer(user).data,
            'message': 'User registered successfully'
        }, status=status.HTTP_201_CREATED)  
    
    
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST 
    )

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    serializer=UserLoginSerializer(data=request.data)
    
    if serializer.is_valid():
        email=serializer._validated_data["email"]
        password=serializer.validated_data["password"]
        
        user=authenticate(request,username=email,password=password)
        
        if user is not None:
            
            if user.is_active:
                login(request,user)
                
                return Response({
                    'user': UserSerializer(user).data,
                    'message': 'Login successful'
                }, status=status.HTTP_200_OK)
                
            else:
                return Response({
                    'error': 'Account is deactivated'
                }, status=status.HTTP_403_FORBIDDEN)
    
    else:
            return Response({
                'error': 'Invalid email or password'
            }, status=status.HTTP_401_UNAUTHORIZED)
            
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )      
    
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def logout_view(request):
    
   
    logout(request)
    
    return Response({
        'message': 'Logout successful'
    }, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):

    serializer = UserSerializer(request.user)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
            

