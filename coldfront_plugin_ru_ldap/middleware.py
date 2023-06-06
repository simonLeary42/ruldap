from django.contrib.auth.middleware import RemoteUserMiddleware
from coldfront.core.utils.common import import_from_settings

class CustomHeaderMiddleware(RemoteUserMiddleware):
    header = import_from_settings("RULDAP_CUSTOM_HEADER", "REMOTE_USER")
