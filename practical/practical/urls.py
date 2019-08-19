from django.contrib import admin
from django.contrib.auth import views as auth_views
from graphene_django.views import GraphQLView
from django.urls import path, include
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/authapi/', include('authapi.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=True))
]
