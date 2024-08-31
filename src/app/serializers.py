from rest_framework import  serializers
from .models import CustomUser,Patients

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



class PatientSerializer(serializers.ModelSerializer):
    medecin = UtilisateurSerializer(read_only=True)
    class Meta:
        model = Patients
        fields = ['id', 'nom_complet', 'sexe', 'date_naiss', 'poid','observation','derniere_cons','medecin','created_at', 'updated_at']

class PatientSerializer2(serializers.ModelSerializer):
    medecin = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Patients
        fields = ['id', 'nom_complet', 'sexe', 'date_naiss', 'poid', 'observation', 'derniere_cons', 'medecin', 'created_at', 'updated_at']

# class PatientSerializer(serializers.ModelSerializer):
#     medecin = UtilisateurSerializer(read_only=True)
#     class Meta:
#         model = Patients
#         fields = '__all__'

#     def to_representation(self, instance):
#         instance.decrypt_fields()
#         return super().to_representation(instance)