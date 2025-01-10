from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "balance",
            "is_active",
            "date_joined",
            "last_login",
        ]
        read_only_fields = ["id", "balance", "is_active", "date_joined", "last_login"]


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone_number", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            password=validated_data["password"],
        )
        return user



class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating user details.
    Allows partial updates with proper validation.
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "required": False, "min_length": 8},
        }

    def validate_password(self, value):
        """
        Validate password length and other rules if needed.
        """
        if value and len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def update(self, instance, validated_data):
        """
        Update user details and handle password changes securely.
        """
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # Set password securely

        instance.save()
        return instance



    
