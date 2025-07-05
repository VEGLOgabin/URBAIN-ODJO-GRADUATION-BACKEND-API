from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilisateurViewSet, ProductCreateUpdate, ProduitViewSetListRetrieve, CommandeViewSet, CommandeProduitViewSet, PaiementViewSet, MessagerieViewSet, AvisViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'produits', ProductCreateUpdate, basename='produit-create-update')
router.register(r'produits', ProduitViewSetListRetrieve, basename='produit-list-retrieve')
router.register(r'commandes', CommandeViewSet)
router.register(r'commande-produits', CommandeProduitViewSet)
router.register(r'paiements', PaiementViewSet)
router.register(r'messagerie', MessagerieViewSet)
router.register(r'avis', AvisViewSet)

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),
]