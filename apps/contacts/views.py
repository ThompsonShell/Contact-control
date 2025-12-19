from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import ContactSerializer, TagSerializer
from .models import Tag, Contact


class ContactCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContactUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    
    
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
    

class ContactListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer


    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class TagsCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagsDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagsListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer


    def get_queryset(self):
        return Tag.objects.filter(
            contacts__user=self.request.user
        )


class SearchContactAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'company_name']
    filterset_fields = ['tags']
    
    
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)