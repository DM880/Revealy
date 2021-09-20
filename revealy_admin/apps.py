from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class RevealyAdminConfig(AdminConfig):
    default_site = 'revealy_admin.admin.RevealyAdmin'
