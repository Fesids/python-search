
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import HomePage
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("book/", include("book.urls")),
    path("", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("profiles/", include("profiles.urls")),
    path("cart/", include("cart.urls")),
    path("", HomePage.as_view(), name="home"),


    # API path's
    path("api/v1/",include("api.urls")),
    path("api/v1/", include("rest_framework.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("ap/schema/swagger-ui/", SpectacularSwaggerView.as_view(
        url_name="schema"
    ), name="swagger-ui")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








