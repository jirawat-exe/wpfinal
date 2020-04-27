# Generated by Django 3.0.5 on 2020-04-25 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cus_id', models.AutoField(primary_key=True, serialize=False)),
                ('cus_nname', models.CharField(max_length=50)),
                ('cus_fname', models.CharField(max_length=50)),
                ('cus_lname', models.CharField(max_length=50)),
                ('cus_type', models.CharField(max_length=50)),
                ('cus_phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_nname', models.CharField(max_length=50)),
                ('emp_fname', models.CharField(max_length=50)),
                ('emp_lname', models.CharField(max_length=50)),
                ('emp_address', models.TextField()),
                ('emp_phone', models.CharField(max_length=10)),
                ('emp_birth', models.DateField()),
                ('emp_age', models.IntegerField()),
                ('hire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_type', models.CharField(max_length=50)),
                ('appointment_date', models.DateField()),
                ('check_id_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('total_amount', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('return_status', models.CharField(max_length=50)),
                ('return_date', models.DateField()),
                ('customer_cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Customer')),
                ('employee_verify_emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('pro_id', models.AutoField(primary_key=True, serialize=False)),
                ('pro_name', models.CharField(max_length=50)),
                ('discount', models.FloatField()),
                ('pro_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service_rate',
            fields=[
                ('rate_id', models.AutoField(primary_key=True, serialize=False)),
                ('cloth_type', models.CharField(max_length=50)),
                ('customer_type', models.CharField(max_length=50)),
                ('service_type', models.CharField(max_length=50)),
                ('unit_price', models.IntegerField()),
                ('employee_emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Service_list',
            fields=[
                ('line_no', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('order_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Order')),
                ('service_rate_rate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Service_rate')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('pos_id', models.AutoField(primary_key=True, serialize=False)),
                ('pos_status', models.CharField(max_length=50)),
                ('order_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('packet_name', models.AutoField(primary_key=True, serialize=False)),
                ('customer_cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='promotion_pro_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.Promotion'),
        ),
    ]
