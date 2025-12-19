from rest_framework import serializers
from apps.contacts.models import Contact, Tag


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Contact
        fields = ['id', 'user', 'name', 'phone_number', 'company_name', 'job_title',]    
        read_only_fields = ['user']

    def get_user(self, obj):
        return obj.user.username if obj.user else None


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
