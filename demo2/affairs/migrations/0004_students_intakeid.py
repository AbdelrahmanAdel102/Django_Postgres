# Generated by Django 4.0.1 on 2022-02-06 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0003_intake'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='intakeid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='affairs.intake'),
            preserve_default=False,
        ),
    ]
