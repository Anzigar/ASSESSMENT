# Generated by Django 3.2.9 on 2022-01-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssessmentSystem', '0006_plan_plan_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='plan_name',
        ),
        migrations.AlterField(
            model_name='plan',
            name='plans',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
