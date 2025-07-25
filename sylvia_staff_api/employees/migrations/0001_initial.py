# Generated by Django 5.2.3 on 2025-06-28 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('staffbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employees.staffbase')),
                ('department', models.CharField(max_length=100)),
                ('has_company_card', models.BooleanField(default=True)),
            ],
            bases=('employees.staffbase',),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street1_address', models.CharField(max_length=255)),
                ('street2_address', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('emplooye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.staffbase')),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('staffbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employees.staffbase')),
                ('internship_end_date', models.DateField()),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interns', to='employees.manager')),
            ],
            bases=('employees.staffbase',),
        ),
    ]
