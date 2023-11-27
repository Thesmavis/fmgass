from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *
from django.db.models import Avg
# Create your views here.

class vendorview_GET(APIView):
    def get(self, request, id = None):

        if id:
            try:
                get_data=vendor_details.objects.get(id=id)
                data1= vendor_ser(get_data)
                return Response(data1.data)
            except:
                get_data=vendor_details.objects.all()
                data1= vendor_ser(get_data,many=True)
                return Response(data1.data)
        else:
            get_data=vendor_details.objects.all()
            data1= vendor_ser(get_data,many=True)
            return Response(data1.data)

class vendorview_POST(APIView):
    def post(self,request):
        serializer= vendor_ser(data=request.data)
        if vendor_details.objects.filter(**request.data).exists():
           raise serializers.ValidationError('This data already exists')
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            serializer.errors
            return Response(status=status.HTTP_404_NOT_FOUND)

class vendorview_PATCH(APIView):
    def patch(self,request,id=None):
        if id:
            data2=vendor_details.objects.get(id=id)
            serializer= vendor_ser(data2,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                serializer.errors
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class vendorview_DELETE(APIView):
    def delete(self,request,id=None):
        try:
                get_data=vendor_details.objects.get(id=id)
                get_data.delete()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class poview_GET(APIView):
    def get(self, request, id = None):

        if id:
            try:
                get_data=po_details.objects.get(id=id)
                data1=po_ser1(get_data)
                return Response(data1.data)
            except:
                get_data=po_details.objects.all()
                data1=po_ser1(get_data,many=True)
                return Response(data1.data)
        else:
            get_data=po_details.objects.all()
            data1=po_ser1(get_data,many=True)
            return Response(data1.data)
class poview_POST(APIView):
    def post(self,request):
        serializer=po_ser(data=request.data)
        if po_details.objects.filter(**request.data).exists():
           raise serializers.ValidationError('This data already exists')
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            serializer.errors
            return Response(status=status.HTTP_404_NOT_FOUND)
class poview_PATCH(APIView):
    def patch(self,request,id=None):
        if id:
            data2=po_details.objects.get(id=id)
            serializer=po_ser(data2,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                serializer.errors
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
class poview_DELETE(APIView):
    def delete(self,request,id=None):
        try:
                get_data=po_details.objects.get(id=id)
                get_data.delete()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class performance_calculation1(APIView):
    def patch(self,request,id=None):
        if id:
            t_del_on_time=0
            t_del_not_on_time=0
            t_comp_po=0
            t_d1=0
            data2=po_details.objects.get(id=id)
            serializer=po_ser(data2,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                if data2.status==5:
                    s=po_details.objects.filter(status=5,vendor=data2.vendor)
                    for i in s:
                        
                        t_comp_po= t_comp_po+1
                        if i.act_delivery_date<=i.ex_delivery_date:
                            t_del_on_time=t_del_on_time+1
                        else:
                            t_del_not_on_time=t_del_not_on_time+1
                    on_ti_de_rt=(t_del_on_time/t_comp_po)*100
                   
                    qc_agg=po_details.objects.filter(status=5,vendor=data2.vendor).aggregate(Avg('quality_rating'))
                    
                    time_diff= po_details.objects.filter(status=5,vendor=data2.vendor).exclude(issue_date=None,acknowledgment_date=None).exists()
                    
                    if time_diff==True:

                        time_diff1= po_details.objects.filter(status=5,vendor=data2.vendor).exclude(issue_date=None,acknowledgment_date=None)
                    
                        for j in time_diff1:
                            d0=j.acknowledgment_date
                            d1=j.issue_date
                            delta=d0-d1
                            t_d1=t_d1+delta.days
                        
                        t_d2=t_d1/len(time_diff1)
                    

                        iss= po_details.objects.filter(status=5,vendor=data2.vendor).exclude(issue_date=None)
                        iss_t=(len(s)/len(iss))
                    
                     
                        per=performance(vendor=data2.vendor,on_time_delivery_rate=on_ti_de_rt,quality_rating_avg=qc_agg['quality_rating__avg'],average_response_time=t_d2,fulfillment_rate=iss_t)
                        per.save()
                        
                        vendor_details.objects.filter(id=data2.vendor_id).update(on_time_delivery_rate=on_ti_de_rt,quality_rating_avg=qc_agg['quality_rating__avg'],average_response_time=t_d2,fulfillment_rate=iss_t)

                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class perform_get(APIView):
    def get(self, request, id = None):

        if id:
            try:
                get_data=performance.objects.filter(vendor_id=id)
                data1=per_ser1(get_data,many=True)
                return Response(data1.data)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
           
        else:
          return Response(status=status.HTTP_404_NOT_FOUND)