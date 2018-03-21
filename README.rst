Siteimprove – the hack!
=======================

Installation
------------

1. Append this to `settings.py` (or, preferably, in your custom
   settings file
   (cf. https://docs.djangoproject.com/en/2.0/topics/settings/#designating-the-settings)):

  .. code-block:: python

    if config.has_option('siteimprove', 'code'):
        SITEIMPROVE_CODE = config.get('siteimprove', 'code')
        MIDDLEWARE[MIDDLEWARE.index('pretix.base.middleware.SecurityMiddleware')] = 'pretix_siteimprove.middleware.SecurityMiddleware'

2. Define your siteimprove code in `pretix.cfg`:

  .. code-block::

    [siteimprove]
    code = xxxxxxx

3. Copy `base_footer.html` to
   `%pretix.datadir%/templates/pretixpresale/base_footer.html/`
   (defined in `pretix.cfg`) and append this line:

  .. code-block:: HTML

    <script type="text/javascript" src="{% url 'plugins:pretix_siteimprove:siteimprove' %}"></script>

4. Restart Pretix



This is a plugin for `pretix`_.

Development setup
-----------------

1. Make sure that you have a working `pretix development setup`_.

2. Clone this repository, eg to ``local/pretix-siteimprove``.

3. Activate the virtual environment you use for pretix development.

4. Execute ``python setup.py develop`` within this directory to register this application with pretix's plugin registry.

5. Execute ``make`` within this directory to compile translations.

License
-------

Copyright 2018 Mikkel Ricky

Released under the terms of the Apache License 2.0


.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
