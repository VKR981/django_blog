# Generated by Django 3.1.1 on 2020-10-11 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20201011_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.course', to_field='slug'),
        ),
    ]
