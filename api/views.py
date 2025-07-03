from rest_framework import viewsets, permissions
from .models import Utilisateur, Produit, Commande, CommandeProduit, Paiement, Messagerie, Avis

from rest_framework.parsers import MultiPartParser,FormParser,JSONParser,FileUploadParser
from rest_framework import viewsets,mixins
from rest_framework.permissions import IsAdminUser,IsAuthenticated


from .serializers import (
    UtilisateurCreateUpdateSerializer, UtilisateurListSerializer,
    ProduitCreateUpdateSerializer, ProduitListSerializer,
    CommandeCreateUpdateSerializer, CommandeListSerializer,
    CommandeProduitCreateUpdateSerializer, CommandeProduitListSerializer,
    PaiementCreateUpdateSerializer, PaiementListSerializer,
    MessagerieCreateUpdateSerializer, MessagerieListSerializer,
    AvisCreateUpdateSerializer, AvisListSerializer
)



# Utilisateur ViewSet
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', "create"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]  

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return UtilisateurListSerializer
        return UtilisateurCreateUpdateSerializer


# Produit ViewSet
class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()] 

    def get_parser_classes(self):
        if self.action in ("create", "update", "partial_update"):
            return [MultiPartParser, FormParser,JSONParser]
        # fall back to DRF’s default parsers (or your global DEFAULT_PARSER_CLASSES)
        return super().get_parser_classes() 
    

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProduitListSerializer
        return ProduitCreateUpdateSerializer

# Commande ViewSet
class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CommandeListSerializer
        return CommandeCreateUpdateSerializer

# CommandeProduit ViewSet
class CommandeProduitViewSet(viewsets.ModelViewSet):
    queryset = CommandeProduit.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CommandeProduitListSerializer
        return CommandeProduitCreateUpdateSerializer

# Paiement ViewSet
class PaiementViewSet(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PaiementListSerializer
        return PaiementCreateUpdateSerializer

# Messagerie ViewSet
class MessagerieViewSet(viewsets.ModelViewSet):
    queryset = Messagerie.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return MessagerieListSerializer
        return MessagerieCreateUpdateSerializer

# Avis ViewSet
class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]  

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AvisListSerializer
        return AvisCreateUpdateSerializer