from rest_framework import serializers
from . models import *

class vendor_ser(serializers.ModelSerializer) :
    class Meta :
        model = vendor_details
        fields='__all__'
class po_ser(serializers.ModelSerializer) :
    class Meta :
        model = po_details
        fields='__all__'
class per_ser(serializers.ModelSerializer) :
    class Meta :
        model = performance
        fields='__all__'

class po_ser1(serializers.ModelSerializer) :
    vendor=vendor_ser()
    class Meta :
        model = po_details
        fields='__all__'

class per_ser1(serializers.ModelSerializer) :
    vendor=vendor_ser()
    class Meta :
        model = performance
        fields='__all__'