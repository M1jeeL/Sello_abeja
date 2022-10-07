
#from django.contrib.auth.hashers import make_password
from rest_framework import serializers, validators
from .models import Address, Client, Commune, Region, User
import re

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('name')

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
        
    def validate_password(self, password):
        if password == '':
            raise serializers.ValidationError('La contraseña no puede estar en blanco')

        if len(password) < 7:
            raise serializers.ValidationError('La contraseña debe ser mayor a 7')

        if password.isnumeric():
            raise serializers.ValidationError('La contraseña no puede ser solo numerica')

        return password

    def validate_email(self, email):
        regex = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

        if (not re.match(regex, email)):
            raise serializers.ValidationError('El formato del email no es válido')

        if email == '':
            raise serializers.ValidationError('El email no puede estar en blanco')

        return email

    def validate_first_name(self, first_name):
        if (not re.fullmatch(r"[A-Za-z ]{1,20}", first_name)):
            raise serializers.ValidationError('El nombre solo puede contener letras')

        if first_name == '':
            raise serializers.ValidationError('El nombre no puede estar en blanco')

        return first_name
        
    def validate_last_name(self, last_name):
        if (not re.fullmatch(r"[A-Za-z ]{1,20}", last_name)):
            raise serializers.ValidationError('El apellido solo puede contener letras')

        if last_name == '':
            raise serializers.ValidationError('El apellido no puede estar en blanco')

        return last_name

    def validate(self, data):
        if data['username'] == data['password']:
            raise serializers.ValidationError('La contraseña no puede ser igual al username')

        return data

        
class ClientSerializer(serializers.ModelSerializer):
    client = UserSerializer(required=True)
    class Meta:
        model = Client
        fields = ('client', 'rut', 'phone')

        extra_kwargs = {
            'rut': {
                'required': True,
                'validators': {
                    validators.UniqueValidator(
                        Client.objects.all(), 'Ya existe un cliente con el rut ingresado'
                    ) 
                }
            }
        }

    def create(self, validated_data):
        validated_data['client']['is_client'] = True
        client_data = validated_data.pop('client')
        client = UserSerializer.create(UserSerializer(), validated_data=client_data)
        student, created = Client.objects.update_or_create(
            client=client,
            rut=validated_data.pop('rut'),
            phone=validated_data.pop('phone')
        )

        return student


