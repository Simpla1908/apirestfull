from django.urls import path
from .views import UtilisateurList,UtilisateurLogin,UtilisateurDetailView,PatientListCreateView,PatientDetailView,TransfertFicheAPIView

urlpatterns = [
    path('medecins/', UtilisateurList.as_view(), name='medecin-list-create'),
    path('medecin/authentifier/', UtilisateurLogin.as_view(), name='medecin-authentifier'),
    path('encoder/fiche/', PatientListCreateView.as_view(), name='encoder-fiche'),
    path('lire/fiche/<int:pk>/', PatientDetailView.as_view(), name='lire-fiche'),
    path('transferer/dossier/<int:pk>/', TransfertFicheAPIView.as_view(), name='transferer-dossier'),


]


 