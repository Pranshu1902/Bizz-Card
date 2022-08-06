from cards.models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'name', 'title', 'description', 'email', 'phone', 'location', 'color']
        read_only_fields = ['user']
    
    # automatically assign the user to the card
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['id', 'link', 'name', 'icon', 'card']
        read_only_fields = ['user']
    
    # automatically assign the user to the link
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    # sign up new user
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinkSerializer

    def get_queryset(self):
        return Links.objects.filter(user=self.request.user)

class APIUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# get logged in user's details
class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

