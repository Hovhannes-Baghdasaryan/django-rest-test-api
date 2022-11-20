from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
#
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Django Movie",
#         default_version='1.0.0',
#         description="Test Description",
#         license=openapi.License(name="BSD License")
#     ),
#     public=True
# )

urlpatterns = [
    # path(r"^swagger(?P<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json", ),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
    path('openapi', get_schema_view(title="Your Project",description="API for all things …",version="1.0.0"), name='openapi-schema'),
    path('', TemplateView.as_view(template_name='swagger-doc.html', extra_context={'schema_url': 'openapi-schema'}), name='api_doc'),
]
