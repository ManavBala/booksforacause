# Generated by Django 3.0.8 on 2020-07-30 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('book_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('book_auth', models.CharField(max_length=300)),
                ('book_pub', models.CharField(max_length=300)),
                ('book_cond', models.CharField(max_length=1)),
                ('book_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
