# Generated by Django 3.2.19 on 2023-06-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_pdfs'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfs',
            name='extra_field',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
