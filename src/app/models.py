from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from cryptography.fernet import Fernet
import os

# Create your models here.


class CustomUser(AbstractUser):
    is_superuser = models.BooleanField(default=True)  
    tel = models.CharField(max_length=20, null=True, blank=True) 
    email = models.EmailField(unique=True)  
    nom_complet = models.CharField(max_length=245, null=True, blank=True)

    class Meta:
      verbose_name = _('user')
      verbose_name_plural = _('users')

    def save(self, *args, **kwargs):
        # hachage mot de passe
        if self._state.adding:  
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Patients(models.Model):
    nom_complet = models.CharField(max_length=200)
    sexe = models.CharField(max_length=200)
    date_naiss = models.CharField(max_length=200)
    poid= models.IntegerField()
    observation = models.TextField()
    derniere_cons = models.TextField()
    medecin = models.ForeignKey('CustomUser', on_delete=models.CASCADE, db_column='medecin_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'patients'

    def __str__(self):
        return self.nom_complet

# class Patients(models.Model):
#     nom_complet = models.CharField(max_length=200)
#     sexe = models.CharField(max_length=200)
#     date_naiss = models.CharField(max_length=200)
#     poid = models.CharField(max_length=200)  # Changer en CharField pour le hachage
#     observation = models.TextField()
#     derniere_cons = models.TextField()
#     medecin = models.ForeignKey('CustomUser', on_delete=models.CASCADE, db_column='medecin_id')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'patients'

#     def __str__(self):
#         return self.nom_complet

#     def save(self, *args, **kwargs):
#         key = os.getenv('SECRET_KEY').encode()
#         cipher_suite = Fernet(key)

#         # Chiffrement des champs
#         self.date_naiss = cipher_suite.encrypt(self.date_naiss.encode()).decode()
#         self.poid = cipher_suite.encrypt(str(self.poid).encode()).decode()
#         self.observation = cipher_suite.encrypt(self.observation.encode()).decode()
#         self.derniere_cons = cipher_suite.encrypt(self.derniere_cons.encode()).decode()

#         super(Patients, self).save(*args, **kwargs)

#     def decrypt_fields(self):
#         key = os.getenv('SECRET_KEY').encode()
#         cipher_suite = Fernet(key)

#         # Déchiffrement des champs
#         self.date_naiss = cipher_suite.decrypt(self.date_naiss.encode()).decode()
#         self.poid = cipher_suite.decrypt(self.poid.encode()).decode()
#         self.observation = cipher_suite.decrypt(self.observation.encode()).decode()
#         self.derniere_cons = cipher_suite.decrypt(self.derniere_cons.encode()).decode()



