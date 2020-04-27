from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True) #id
    cus_nname = models.CharField(max_length=50, null=True, blank=False, default=None) #ชื่อเล่น ลูกค้า
    cus_fname = models.CharField(max_length=50, null=True, blank=False, default=None) #ชื่อจริง ลูกค้า
    cus_lname = models.CharField(max_length=50, null=True, blank=False, default=None) #นามสกุล ลูกค้า
    cus_type = models.CharField(max_length=50) #ประเภท รายวัน หรือ รายเดือน
    cus_phone = models.CharField(max_length=10) #เบอร์โทร

class Packet(models.Model):
    packet_name = models.AutoField(primary_key=True) #id
    customer_cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True) #id
    emp_nname = models.CharField(max_length=50) #ชื่อเล่น พนักงาน
    emp_fname = models.CharField(max_length=50) #ชื่อจริง พนักงาน
    emp_lname = models.CharField(max_length=50) #นามสกุล พนักงาน
    emp_address = models.TextField() #ที่อยู่พนักงาน
    emp_phone = models.CharField(max_length=10) #เบอร์โทร
    emp_birth = models.DateField() #วันเกิด
    emp_age = models.IntegerField() #อายุ
    hire_date = models.DateField() #วันที่จ้าง

class Promotion(models.Model):
    pro_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=50)
    discount = models.FloatField()
    pro_status = models.CharField(max_length=50) #'ใช้ได้','ใช้ไม่ได้'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True) #id
    sort_cus_phone = models.CharField(max_length=10) #เบอร์ลูกค้า เอาไว้หาว่าของใคร
    service_type = models.CharField(max_length=50) #'ซักอบ','ซักอบรีด','รีด','อบ'
    appointment_date = models.DateField() #วันนัดรับ
    check_in_date = models.DateField() #
    status = models.CharField(max_length=50) #'กำลังดำเนินการ','เสร็จแล้ว'
    total_amount = models.IntegerField() #จำนวนเสื้อผ้า
    total_price = models.FloatField() #ราคา
    return_status = models.CharField(max_length=50) #'มารับไปแล้ว','ยังไม่ได้มารับ'
    return_date = models.DateField() #วันที่มารับไปแล้ว
    customer_cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    promotion_pro_id = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    employee_verify_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Position(models.Model): #ตำแหน่งวางเสื้อผ้า
    pos_id = models.AutoField(primary_key=True) #id
    pos_status = models.CharField(max_length=50) #'ว่าง','ไม่ว่าง'
    order_order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

class Service_rate(models.Model):
    rate_id = models.AutoField(primary_key=True) #id
    cloth_type = models.CharField(max_length=50) #ประเภทเสื้อผ้า
    customer_type = models.CharField(max_length=50) #'รายเดือน','รายวัน'
    service_type = models.CharField(max_length=50) #'ซักอบ','ซักอบรีด','รีด','อบ'
    unit_price = models.IntegerField() #ราคาสุทธิ
    employee_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Service_list(models.Model):
    line_no = models.AutoField(primary_key=True) #id
    amount = models.IntegerField()
    total_price = models.FloatField()
    order_order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    service_rate_rate_id = models.ForeignKey(Service_rate, on_delete=models.CASCADE)



