from rest_framework import viewsets, permissions
from .models import Utilisateur, Produit, Commande, CommandeProduit, Paiement, Messagerie, Avis

from rest_framework.parsers import MultiPartParser,FormParser,JSONParser,FileUploadParser
from rest_framework import viewsets,mixins


from .serializers import *



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
class ProduitViewSetListRetrieve(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class= ProduitListSerializer
    queryset = Produit.objects.all()
    permission_classes=[permissions.AllowAny()]


    
class ProductCreateUpdate(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class=ProduitCreateUpdateSerializer
    queryset=Produit.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,FileUploadParser)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(agriculteur=user)
        return user

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