# Generated by Django 4.1.1 on 2022-09-16 22:23

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_client', models.BooleanField(default=False, verbose_name='Cliente')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_tech', models.BooleanField(default=False, verbose_name='Tecnico')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=100, verbose_name='Calle')),
                ('street_number', models.CharField(max_length=100, verbose_name='Numeracion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Beehive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.CharField(max_length=150, verbose_name='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
            ],
            options={
                'verbose_name': 'beehive',
                'verbose_name_plural': 'beehives',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, verbose_name='RUT')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefono')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
                ('beehive', models.ManyToManyField(to='api.beehive')),
                ('tech', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'tech',
                'verbose_name_plural': 'techs',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_report', models.DateTimeField(verbose_name='Fecha de reporte')),
                ('report', models.CharField(max_length=200, verbose_name='Reporte')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tech')),
            ],
            options={
                'verbose_name': 'visit',
                'verbose_name_plural': 'visits',
            },
        ),
        migrations.CreateModel(
            name='Suscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Fecha de inicio suscripcion')),
                ('end_time', models.DateTimeField(verbose_name='Fecha de fin suscripcion')),
                ('active', models.BooleanField(default=False, verbose_name='Activo')),
                ('quantity_beehive', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('num_stars', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=128, verbose_name='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
                ('tags', models.ManyToManyField(to='api.tag')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.region')),
            ],
            options={
                'verbose_name': 'commune',
                'verbose_name_plural': 'communes',
            },
        ),
        migrations.AddField(
            model_name='beehive',
            name='suscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.suscription'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha eliminacion')),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'admin',
                'verbose_name_plural': 'admins',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='commune',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.commune'),
        ),
    ]
