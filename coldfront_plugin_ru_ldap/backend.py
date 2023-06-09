from coldfront.plugins.ldap_user_search.utils import LDAPUserSearch
from django.contrib.auth.backends import RemoteUserBackend

import logging

logger = logging.getLogger(__name__)


class LDAPRemoteUserBackend(RemoteUserBackend):
    create_unknown_user = False

    def __init__(self):
        super().__init__()

    def authenticate(self, request, remote_user):
        if not remote_user:
            return None
        username = self.clean_username(remote_user)
        search = LDAPUserSearch(username, "username_only")
        self.user_dict = search.search_a_user(username, "username_only")
        if len(self.user_dict) == 0:
            # LDAP doesn't have this user
            return None
        else:
            self.create_unknown_user = True
        return super().authenticate(request, remote_user)

    def clean_username(self, username):
        return username.split("@")[0]

    def configure_user(self, request, user, created=True):
        ud = self.user_dict[0]
        logger.debug(ud)
        user.first_name = ud["first_name"]
        user.last_name = ud["last_name"]
        user.email = ud["email"]
        return user
