# ruldap - Remote User LDAP

A [ColdFront](https://coldfront.readthedocs.io/en/latest/) plugin that provides `LDAPRemoteUserBackend` that will configure a user based on information pulled from LDAP.

## Installation
`pip install git+https://github.com/cecilialau6776/ruldap`

## Configuration
Add the following to ColdFront's [local settings](https://coldfront.readthedocs.io/en/latest/config/#configuration-files):

```
INSTALLED_APPS += ["coldfront_plugin_ru_ldap"]
MIDDLEWARE += ["django.contrib.auth.middleware.RemoteUserMiddleware"]
AUTHENTICATION_BACKENDS.remove("django.contrib.auth.backends.ModelBackend")
AUTHENTICATION_BACKENDS += [
    "coldfront_plugin_ru_ldap.backend.LDAPRemoteUserBackend",
]
```
If you wish to define a custom header, append `coldfront_plugin_ru_ldap.middleware.CustomHeaderMiddleware` to `MIDDLEWARE` instead and set `RULDAP_CUSTOM_HEADER="HTTP_MY_CUSTOM_HEADER"`. **This value can be spoofed.** Be careful and read the [warning](https://docs.djangoproject.com/en/4.2/howto/auth-remote-user/#configuration) from Django's docs. 

By default, `ruldap` will use the `LDAP_USER_SEARCH` plugin and it's configuration, searching by username only. To change this, set the following relevant options in ColdFront's local settings:
```
RULDAP_USER_LDAP_USER_SEARCH = False
RULDAP_SERVER_URI = "ldap://example.com"
RULDAP_BASE = "dc=example,dc=com"
RULDAP_BIND_DN = "cn=Manager,dc=example,dc=com"
RULDAP_BIND_PASSWORD = "secret"
RULDAP_CONNECT_TIMEOUT = 2.5                         # Optional, default 2.5
RULDAP_USE_SSL = True
RULDAP_USE_TLS = False
RULDAP_PRIV_KEY_FILE = "/path/to/key"
RULDAP_CERT_FILE = "/path/to/cert"
RULDAP_CACERT_FILE = "/path/to/cacert"
```


### Other Options
| Setting                 | Default                              | Description              |
| ----------------------- | ------------------------------------ | ------------------------ |
| `RULDAP_USERNAME_FIELD` | `"(uid=%s)"`                         | The search filter used   |
| `RULDAP_ATTRIBUTES`     | `{"uid": "username", "sn": "last_name", "givenName": "first_name", "mail": "email"}` | A mapping from requested LDAP attributes to User attributes. Changing the keys will change the requested attributes. |
