# Generated by Django 4.2.2 on 2023-07-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0009_alter_house_details_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics1')),
                ('bedroom', models.CharField(max_length=50)),
                ('bathroom', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('house_img1', models.ImageField(upload_to='pics1')),
                ('house_img2', models.ImageField(upload_to='pics1')),
                ('house_img3', models.ImageField(upload_to='pics1')),
            ],
        ),
        migrations.DeleteModel(
            name='House_Details',
        ),
    ]
