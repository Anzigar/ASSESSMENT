# Generated by Django 3.2.9 on 2021-12-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssessmentSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='manageproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.IntegerField()),
                ('Nameofitem', models.CharField(max_length=200)),
                ('Quantity', models.CharField(max_length=200)),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]