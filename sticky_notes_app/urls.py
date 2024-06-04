"""
URL configuration for sticky_notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import notes_create, home, notes_detail, notes_update, notes_delete
from django.urls import path

urlpatterns = [
    # url patterns for home page displayong list of all notes
    path("", home, name="home"),
    # url pattern for creating notes
    path("create/", notes_create, name="create"),
    # url pattern for details of specific notes
    path("notes/<int:pk>/", notes_detail, name="notes_detail"),
    # url pattern for updating notes
    path("notes/<int:pk>/update/", notes_update, name="notes_update"),
    # url pattern for deleting notes
    path("notes/<int:pk>/delete/", notes_delete, name="notes_delete"),
]
