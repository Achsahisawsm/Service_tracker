
from django.http import HttpResponse
from models import Vendor
from rest_framework.response import Response
from rest_framework import viewsets
from serializers import VendorCreateSerializer,VendorsListSerializer,VendorDetailSerializer,VendorUpdateSerializer
from rest_framework import status

def index(request):
    return HttpResponse('comeon')

class VendorViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Vendor.query().fetch()
        serializer=VendorsListSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,ID):
        queryset =Vendor.get_by_id(int(ID))
        serializer = VendorUpdateSerializer(queryset)
        return Response(serializer.data)

    def create(self,request):
        serializer = VendorCreateSerializer(data=request.data)
        if serializer.is_valid():
            vendor = Vendor(name = serializer.validated_data.get('name'),
                            service_type=serializer.validated_data.get('service_type'),
                            address = serializer.validated_data.get('address'),
                            contact_no_1 = serializer.validated_data.get('contact_no_1'),
                            contact_no_2=serializer.validated_data.get('contact_no_2'),
                            description = serializer.validated_data.get('description'),
                            created_by =serializer.validated_data.get('created_by'),
                            created_on=serializer.validated_data.get('created_on'),
                            )

            vendor.put()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,ID):
        vendor= Vendor.get_by_id(int(ID))
        serializer = VendorUpdateSerializer(data=request.data)
        if serializer.is_valid():
            vendor.name=serializer.validated_data.get('name')
            vendor.service_type = serializer.validated_data.get('service_type')
            vendor.address = serializer.validated_data.get('address')
            vendor.contact_no_1 = serializer.validated_data.get('contact_no_1')
            vendor.contact_no_2 = serializer.validated_data.get('contact_no_2')
            vendor.put()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,ID):
        vendor =Vendor.get_by_id(int(ID))
        print vendor
        vendor.key.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





