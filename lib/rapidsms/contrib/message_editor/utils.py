#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.utils.functional import curry
from rapidsms.contrib.ajax.utils import call_router


# these helper methods are just proxies to app.py
get_templates = curry(call_router, "message_editor", "templates")
