from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerialzer(serializers.ModelSerializer):
    """
    Serializer to show user info
    """

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "email"]


class SignupSerializer(serializers.ModelSerializer):
    """
    Serializer used in user signup functionality.
    """

    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def validate_email(self, email):
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for manage login functionality
    """

    username = serializers.CharField()
    password = serializers.CharField()

    def save(self):
        user = User.objects.filter(
            Q(username=self.validated_data["username"])
            | Q(email__iexact=self.validated_data["username"])
        ).first()
        if not user:
            raise serializers.ValidationError({"error": "User not found"})
        if not user.check_password(self.validated_data["password"]):
            raise serializers.ValidationError({"error": "Invalid credentials"})
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token
        return {"access": str(access_token), "refresh": str(refresh_token)}
