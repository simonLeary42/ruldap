from coldfront.plugins.ldap_user_search.utils import LDAPUserSearch
from django.contrib.auth.backends import RemoteUserBackend

import logging

logger = logging.getLogger(__name__)


class LDAPRemoteUserBackend(RemoteUserBackend):
    create_unknown_user = False

    def authenticate(self, request, remote_user):
        if not remote_user:
            return 
        username = self.clean_username(remote_user)
        search = LDAPUserSearch(username, "username_only")
        user_dict = search.search_a_user(username, "username_only")
        if len(user_dict) == 0:
            # LDAP doesn't have this user
            return None
        else:
            self.create_unknown_user = True
            return super().authenticate(request, remote_user)

    def clean_username(self, username):
        return username.split("@")[0]

    def configure_user(self, request, user, created=True):
        search = LDAPUserSearch(user.username, "username_only")
        user_dict = search.search_a_user(user.username, "username_only")
        user.first_name = user_dict["first_name"]
        user.last_name = user_dict["last_name"]
        user.email = user_dict["email"]
        return user
