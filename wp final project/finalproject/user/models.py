from django.db import models

# Create your models here.
class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True) #id
    cus_nname = models.CharField(max_length=50, null=True, blank=False, default=None) #ชื่อเล่น ลูกค้า
    cus_fname = models.CharField(max_length=50, null=True, blank=False, default=None) #ชื่อจริง ลูกค้า
    cus_lname = models.CharField(max_length=50, null=True, blank=False, default=None) #นามสกุล ลูกค้า
    cus_type = models.CharField(max_length=50) #ประเภท รายวัน หรือ รายเดือน
    cus_phone = models.CharField(max_length=10) #เบอร์โทร

class Service_rate(models.Model):
    rate_id = models.AutoField(primary_key=True) #id
    cloth_type = models.CharField(max_length=50) #ประเภทเสื้อผ้า
    customer_type = models.CharField(max_length=50) #'รายเดือน','รายวัน'
    service_type = models.CharField(max_length=50) #'ซักอบ','ซักอบรีด','รีด','อบ'
    unit_price = models.IntegerField() #ราคาสุทธิ
    employee_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)