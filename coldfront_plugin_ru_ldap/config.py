from coldfront.config.base import INSTALLED_APPS, MIDDLEWARE, AUTHENTICATION_BACKENDS
from coldfront.config.env import ENV
from django.core.exceptions import ImproperlyConfigured

import logging

logger = logging.getLogger(__name__)
if "coldfront_plugin_ru_ldap" not in INSTALLED_APPS:
    INSTALLED_APPS += ["coldfront_plugin_ru_ldap"]


# django.contrib.auth.middleware.AuthenticationMiddleware added in base.py
MIDDLEWARE += ["django.contrib.auth.middlware.RemoteUserMiddleware"]
AUTHENTICATION_BACKENDS += [
    "coldfront_plugins_ru_ldap.backend.LDAPRemoteUserBackend",
]

# -----------------------------------------------------------------------------
#  This is a backend to authenticate with REMOTE_USER and pull user information
#  from ldap_user_search
# -----------------------------------------------------------------------------

RULDAP_USE_LDAP_USER_SEARCH = ENV.str("RULDAP_USE_LDAP_USER_SEARCH", default=True)
if RULDAP_USE_LDAP_USER_SEARCH:
    if not ENV.str("PLUGIN_LDAP_USER_SEARCH"):
        raise ImproperlyConfigured(
            "RULDAP_USE_LDAP_USER_SEARCH is enabled but PLUGIN_LDAP_USER_SEARCH"
            " is not. Please enable PLUGIN_LDAP_USER_SEARCH or disable"
            " RULDAP_USE_LDAP_USER_SEARCH."
        )
else:
    RULDAP_SERVER_URI = ENV.str("RULDAP_SERVER_URI")
    RULDAP_BASE = ENV.str("RULDAP_BASE")
    RULDAP_BIND_DN = ENV.str("RULDAP_BIND_DN", default="")
    RULDAP_BIND_PASSWORD = ENV.str("RULDAP_BIND_PASSWORD", default="")
    RULDAP_CONNECT_TIMEOUT = ENV.float("RULDAP_CONNECT_TIMEOUT", default=2.5)
    RULDAP_USE_SSL = ENV.bool("RULDAP_USE_SSL", default=True)
    RULDAP_USE_TLS = ENV.bool("RULDAP_USE_TLS", default=False)
    RULDAP_PRIV_KEY_FILE = ENV.str("RULDAP_PRIV_KEY_FILE", default="")
    RULDAP_CERT_FILE = ENV.str("RULDAP_CERT_FILE", default="")
    RULDAP_CACERT_FILE = ENV.str("RULDAP_CACERT_FILE", default="")
