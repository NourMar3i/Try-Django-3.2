# Generated by Django 3.2.19 on 2023-06-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20230620_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfs',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]