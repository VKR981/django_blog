# Generated by Django 3.1.1 on 2020-10-11 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app01', '0003_auto_20201011_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.course', to_field='slug'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
