from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi





schema_view = get_schema_view(
    openapi.Info(
        title="Farming Matket API",
        default_version='v1',
        description="We are helping agriculture farmers to have access to a  good online market",
        contact=openapi.Contact(email="contact.agriculturemarket@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)