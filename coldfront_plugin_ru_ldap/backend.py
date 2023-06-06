from coldfront.plugins.ldap_user_search.utils import LDAPUserSearch
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth import get_user_model

import logging

logger = logging.getLogger(__name__)

class LDAPRemoteUserBackend(RemoteUserBackend):
    def clean_username(self, username):
        return username.split("@")[0]
    def configure_user(self, request, user, created=True):
        search = LDAPUserSearch(user.username, "username_only")
        user_dict = search.search_a_user(user.username, "username_only")[0]
        user["username"] = user_dict["username"]
        user["first_name"] = user_dict["first_name"]
        user["last_name"] = user_dict["last_name"]
        user["email"] = user_dict["email"]
        return user
