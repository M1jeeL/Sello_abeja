from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Atributos
    is_client = models.BooleanField(default=False, verbose_name="Cliente")
    is_admin = models.BooleanField(default=False, verbose_name="Admin")
    is_tech = models.BooleanField(default=False, verbose_name="Tecnico")


    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")

    class Meta:
        verbose_name = "region"
        verbose_name_plural = "regions"

class Commune(models.Model):

    name = models.CharField(max_length=50, verbose_name="Nombre")
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
     # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion", blank=True, null=True)
    
    class Meta:
        verbose_name = "commune"
        verbose_name_plural = "communes"

class Address(models.Model):
    commune = models.OneToOneField(Commune, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=100, verbose_name="Calle")
    street_number = models.CharField(max_length=100, verbose_name="Numeracion")

     # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion", blank=True, null=True)
    
    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"


class Client(models.Model):
    # Hereda los campos de tabla user
    client= models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
 
    # Atributos
    rut = models.CharField(max_length=12, verbose_name="RUT")
    phone = models.CharField(max_length=15, verbose_name="Telefono")

    # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion", blank=True, null=True)

    class Meta:
        verbose_name = "client"
        verbose_name_plural = "clients"

    def __str__(self):
        return self.client.username


class Admin(models.Model):
    # Hereda los campos de tabla user
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion", blank=True, null=True)
    
    class Meta:
        verbose_name = "admin"
        verbose_name_plural = "admins"
    
    def __str__(self):
      return self.admin.username

class Suscriptor(models.Model):
    # Hereda los campos de tabla user
    suscriptor: models.OneToOneField(User, on_delete=models.CASCADE)

     # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion", blank=True, null=True)
    
    class Meta:
        verbose_name = "suscriptor"
        verbose_name_plural = "suscriptors"
    
    def __str__(self):
      return self.suscriptor.username


class Suscription(models.Model):
    # Atributos
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=False, verbose_name="Fecha de inicio suscripcion")
    end_time = models.DateTimeField(auto_now=False, verbose_name="Fecha de fin suscripcion")
    active = models.BooleanField(default=False, verbose_name="Activo")
    quantity_beehive = models.IntegerField()
 
    # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion", blank=True, null=True)


class Beehive(models.Model):

    suscription = models.ForeignKey(Suscription, on_delete=models.CASCADE)

    # Atributos
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=150, verbose_name="Descripcion")

    # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion", blank=True, null=True)

    class Meta:
        verbose_name = "beehive"
        verbose_name_plural = "beehives"


class Tech(models.Model):
    # Atributos
    tech = models.OneToOneField(User, on_delete=models.CASCADE)
    beehive = models.ManyToManyField(Beehive)

    # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion",blank=True, null=True)

    class Meta:
        verbose_name = "tech"
        verbose_name_plural = "techs"
    
    def __str__(self):
      return self.tech.username

class Visit(models.Model):
    # Atributos
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
    date_report = models.DateTimeField(auto_now=False, verbose_name="Fecha de reporte")
    report = models.CharField(max_length=200, verbose_name="Reporte")

    # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion",blank=True, null=True)

    class Meta:
        verbose_name = "visit"
        verbose_name_plural = "visits"
    

class Tag(models.Model):
    # Atributos
    name = models.CharField(max_length=25, verbose_name="Nombre")

    # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion",blank=True, null=True)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

class Products(models.Model):
    # Atributos
    name = models.CharField(max_length=50)
    num_stars = models.IntegerField()
    stock = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=128, verbose_name="Descripcion")
    tags = models.ManyToManyField(Tag)
    
    # Info del registro
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    deleted_at =  models.DateTimeField(auto_now=False, verbose_name="Fecha eliminacion", blank=True, null=True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"


