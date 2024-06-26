# Generated by Django 4.2.9 on 2024-03-19 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0002_delete_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50, null=True)),
                ('aadharno', models.CharField(max_length=50, null=True)),
                ('clgname', models.CharField(max_length=50, null=True)),
                ('reference', models.CharField(max_length=50, null=True)),
                ('enrl_status', models.CharField(default='NO', max_length=50)),
                ('course', models.CharField(default='Not Enroll Yet', max_length=50)),
            ],
            options={
                'db_table': 'enquiry',
            },
        ),
    ]
