from django.urls import path, include

urlpatterns = [
    path('accounts/', include('djagno.contrib.auth.urls'))
]
