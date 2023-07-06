# ruldap - Remote User LDAP

A [ColdFront](https://coldfront.readthedocs.io/en/latest/) plugin that provides `LDAPRemoteUserBackend` that will configure a user based on information pulled from LDAP. If a user doesn't exist in LDAP, the user will **not** be created.

## Installation
If you're using a virtual environment (following ColdFront's deployment instructions should have you make and use a virtual environment), make sure you're in the virutal environment first.

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

## Details
`ruldap` uses the [`CombinedUserSearch`](https://github.com/ubccr/coldfront/blob/v1.1.4/coldfront/core/user/utils.py#L74) class built in to ColdFront that uses the classes in `ADDITIONAL_USER_SEARCH_CLASSES`. This means that if you add additional user search classes, it will attempt to use those classes. For example, if you enable the [`ldap_user_search` plugin](https://github.com/ubccr/coldfront/tree/v1.1.4/coldfront/plugins/ldap_user_search), `ruldap` will use `ldap_user_search` to find users.
