
from rest_framework import serializers, validators
#from django.contrib.auth.hashers import make_password
from .models import Address, Client, User

class RegisterClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'validators': {
                    validators.UniqueValidator(
                        User.objects.all(), 'Ya existe un cliente con el email ingresado'
                    )
                }
            }
        }


    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        user = User.objects.create(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        return user