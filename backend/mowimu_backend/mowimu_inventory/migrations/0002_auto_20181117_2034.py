# Generated by Django 2.1.3 on 2018-11-17 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mowimu_inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('inside_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contains_place', to='mowimu_inventory.Place')),
            ],
        ),
        migrations.AddField(
            model_name='thing',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contains_thing', to='mowimu_inventory.Place'),
        ),
    ]
