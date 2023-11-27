from django.db import models

# Create your models here.

class vendor_details(models.Model):
    name=models.CharField(max_length=500,blank=True,null=True)
    contact_details=models.TextField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    vendor_code=models.CharField(max_length=500,blank=True,null=True,unique=True)
    on_time_delivery_rate=models.FloatField(blank=True,null=True)
    quality_rating_avg=models.FloatField(blank=True,null=True)
    average_response_time=models.FloatField(blank=True,null=True)
    fulfillment_rate=models.FloatField(blank=True,null=True)

class po_details(models.Model):
    class st(models.IntegerChoices):
        # GENERATED=1,
        ACCEPTED=2,
        PENDING=3,
        CANCELLED=4,
        COMPLETED=5,
    po_number=models.CharField(max_length=500,blank=True,null=True,unique=True)
    vendor=models.ForeignKey(vendor_details, on_delete=models.DO_NOTHING,  blank=True, null=True)
    order_date=models.DateTimeField( blank=True, null=True)
    ex_delivery_date=models.DateTimeField( blank=True, null=True)
    act_delivery_date=models.DateTimeField( blank=True, null=True)
    items=models.JSONField(blank=True,null=True)
    quantity=models.IntegerField(blank=True,null=True)
    status=models.IntegerField(default=2,choices=st.choices)
    quality_rating=models.FloatField(blank=True,null=True)
    issue_date=models.DateTimeField( blank=True, null=True)
    acknowledgment_date=models.DateTimeField( blank=True, null=True)

class performance(models.Model):
    vendor=models.ForeignKey(vendor_details, on_delete=models.DO_NOTHING,  blank=True, null=True)
    date=models.DateTimeField( blank=True, null=True)
    on_time_delivery_rate=models.FloatField(blank=True,null=True)
    quality_rating_avg=models.FloatField(blank=True,null=True)
    average_response_time=models.FloatField(blank=True,null=True)
    fulfillment_rate=models.FloatField(blank=True,null=True)
