from django import forms

class add_order_form(forms.Form):
    sort_cus_phone = forms.CharField(max_length=10, required=True, label='เบอร์ลูกค้า') #เบอร์ลูกค้า เอาไว้หาว่าของใคร
    total_amount = forms.IntegerField(required=True, label='จำนวนเสื้อผ้า') #จำนวนเสื้อผ้า
    service_type = forms.CharField(max_length=50, required=True, label='ประเภท') #'ซักอบ','ซักอบรีด','รีด','อบ'
    appointment_date = forms.DateField(required=True, label='วันนัดรับ') #วันนัดรับ
    check_in_date = forms.DateField(required=True, label='วันที่มาส่งซัก') #วันที่มาส่งซัก
    total_price = forms.FloatField(required=True, label='ราคา') #ราคา
    status = forms.CharField(max_length=50, required=False, label='สถานะ') #'กำลังดำเนินการ','เสร็จแล้ว'

