from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser,Patients
from .serializers import UtilisateurSerializer,PatientSerializer,PatientSerializer2
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# Create your views here.
class UtilisateurList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [AllowAny]  # Permet l'accès à tous, même non authentifiés

class UtilisateurLogin(generics.CreateAPIView):
    permission_classes = [AllowAny]  

    def post(self, request, *args, **kwargs):
        # Valider les données de connexion
        username = request.data.get('username')
        password = request.data.get('password')

        print(f"Username: {username}")
        print(f"Password: {password}")
        print(get_user_model())

        if not username or not password:
            return Response({"message": "Veuillez fournir le nom d'utilisateur et le mot de passe."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            utilisateur = get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return Response({"message": "Nom d'utilisateur invalide."}, status=status.HTTP_401_UNAUTHORIZED)

        if utilisateur.check_password(password):
            # Générer le token JWT
            refresh = RefreshToken.for_user(utilisateur)
            # Récupérer les données de l'utilisateur
            user_data = {
                "id": utilisateur.id,
                "refresh": f"{settings.BEARER_PREFIX} {str(refresh)}",
                "access": f"{settings.BEARER_PREFIX} {str(refresh.access_token)}",
            }
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Mot de passe invalide."}, status=status.HTTP_401_UNAUTHORIZED)
        

class UtilisateurDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticated]


class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(medecin=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]


class TransfertFicheAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer2