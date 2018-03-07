# Siteimprove – the hack!

## Installation

1. Add this at end of `settings.py`:

```
if config.has_option('siteimprove', 'code'):
    SITEIMPROVE_CODE = config.get('siteimprove', 'code')
    MIDDLEWARE[MIDDLEWARE.index('pretix.base.middleware.SecurityMiddleware')] = 'pretix_siteimprove.middleware.SecurityMiddleware'
```

Add your siteimprove code in `pretix.cfg`:

```
[siteimprove]
code = xxxxxxx
```

Copy

Restart Pretix
