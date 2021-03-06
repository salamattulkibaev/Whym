# Generated by Django 2.0.3 on 2018-03-26 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='Мобильный номер')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('verification_code', models.DecimalField(decimal_places=0, max_digits=4, null=True, verbose_name='Код подтверждения номера')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                ('full_address', models.CharField(blank=True, max_length=255, verbose_name='Адресс')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
