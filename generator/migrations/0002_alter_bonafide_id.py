# Generated by Django 4.1.3 on 2022-12-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonafide',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
