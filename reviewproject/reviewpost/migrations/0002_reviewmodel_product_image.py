# Generated by Django 3.1.13 on 2021-10-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewpost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='product_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]