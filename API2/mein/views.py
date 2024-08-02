from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from .serializers import UserSerializers
from .models import User



class UserCreateListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'id'

