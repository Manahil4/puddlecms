# Generated by Django 3.2.25 on 2024-07-10 18:10

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
            name='DesignerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('previous_work', models.TextField()),
                ('education', models.TextField()),
                ('experience', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('portfolio_image', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
