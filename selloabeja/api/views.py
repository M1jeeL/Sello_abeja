from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import status
from knox.auth import AuthToken
from .serializers import ClientSerializer
from .models import User

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'token': token
    })

@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
        })
    
    return Response({'error': 'Not authenticated'}, status=400)

@api_view(['POST'])
def register_client(request):
    serializer = ClientSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=ValueError):
        serializer.create(validated_data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages,
                    status=status.HTTP_400_BAD_REQUEST)
