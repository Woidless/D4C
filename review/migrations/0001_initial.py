# Generated by Django 4.2.1 on 2023-05-05 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('highway', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewHighway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('rating', models.IntegerField()),
                ('problem', models.CharField(choices=[('Global', 'all street'), ('Local', 'piece of street')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('way', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='highway.highway')),
            ],
        ),
    ]
