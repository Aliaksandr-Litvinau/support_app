from rest_framework import serializers

from user.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_support', 'password')
        extra_kwargs = {
            'is_support': {'read_only': True},
            'is_staff': {'read_only': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    # def validate_password(self, value: str) -> str:
    #     """
    #         Hash value passed by user.
    #         :param value: password of a user
    #         :return: a hashed version of the password
    #     """
    #     return make_password(value)
