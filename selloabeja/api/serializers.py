
from rest_framework import serializers, validators
#from django.contrib.auth.hashers import make_password
from .models import Address, Client, Commune, Region, User

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('')

class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = ('name', 'region')

class AddressSerializer(serializers.ModelSerializer):
    commune = CommuneSerializer(required=True)
    class Meta:
        model = Address
        fields = ('commune', 'street_name', 'street_number')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
                'username',
                'password',
                'email',
                'first_name',
                'last_name',
                'is_client',
                'is_admin',
                'is_tech'
                )

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

class ClientSerializer(serializers.ModelSerializer):
    client = UserSerializer(required=True)
    class Meta:
        model = Client
        fields = ('client', 'rut', 'phone',)

    def create(self, validated_data):

        client_data = validated_data.pop('client')
        client = UserSerializer.create(UserSerializer(), validated_data=client_data)
        student, created = Client.objects.update_or_create(
            client=client, rut=validated_data.pop('rut'),
            phone=validated_data.pop('phone')
        )
        return student
