from models import Bill
from serializers import BillListSerializer, BillCreateSerializer, BillDetailSerializer, BillPaymentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route
from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request, 'index.html', {})

class BillViews(viewsets.ViewSet):

    def list(self, request):

        queryset = Bill.query().fetch()
        serializer = BillListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, ID):

        queryset = Bill.get_by_id(int(ID))
        serializer = BillDetailSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):

        print request.data
        serializer = BillCreateSerializer(data=request.data)
        if serializer.is_valid():
            Bill(vendor=serializer.validated_data.get('vendor'),
                 bill_date=serializer.validated_data.get('bill_date'),
                 amount=serializer.validated_data.get('amount'),
                 due_date=serializer.validated_data.get('due_date'),
                 line_items=serializer.validated_data.get('line_items'),
                 company=serializer.validated_data.get('company'),
                 branch=serializer.validated_data.get('branch'),
                 status=serializer.validated_data.get('status'),
                 date_of_payment=serializer.validated_data.get('date_of_payment'),
                 notes=serializer.validated_data.get('notes'),).put()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, ID):

        bill = Bill.get_by_id(int(ID))
        serializer = BillCreateSerializer(data=request.data)
        if serializer.is_valid():
            bill.vendor = serializer.validated_data.get('vendor')
            bill.bill_date = serializer.validated_data.get('bill_date')
            bill.amount = serializer.validated_data.get('amount')
            bill.due_date = serializer.validated_data.get('due_date')
            bill.line_items = serializer.validated_data.get('line_items')
            bill.company = serializer.validated_data.get('company')
            bill.branch = serializer.validated_data.get('branch')
            bill.status = serializer.validated_data.get('status')
            bill.date_of_payment = serializer.validated_data.get('date_of_payment')
            bill.notes = serializer.validated_data.get('notes')
            bill.put()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, ID):

        bill = Bill.get_by_id(int(ID))
        if bill:
            bill.key.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    @detail_route()
    def payment(self, request, ID):

        bill = Bill.get_by_id(int(ID))
        serializer = BillPaymentSerializer(request.data)
        if serializer.is_valid():
            bill.status = serializer.validated_data.get('status')
            bill.date_of_payment = serializer.validated_data.get('date_of_payment')
            bill.notes = serializer.validated_data.get('notes')
            bill.put()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
