from rest_framework import serializers
from .models import Vendor
from django.utils import timezone



class BaseVendorSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    service_type = serializers.CharField(required=False)
    description = serializers.CharField(required=False)


class VendorsListSerializer(BaseVendorSerializer):
    id = serializers.SerializerMethodField()
    def get_id(self, obj):
        return obj.key.id()


class VendorCreateSerializer(BaseVendorSerializer):
    created_on = serializers.DateField(required=False)
    created_by = serializers.CharField(required=False)
    address = serializers.CharField(required=False)



class VendorDetailSerializer(VendorsListSerializer,VendorCreateSerializer):
    pass


class VendorUpdateSerializer(VendorCreateSerializer):
    updated_on = serializers.DateField(required=False)
    updated_by = serializers.CharField(required=False)



