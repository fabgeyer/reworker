#!/usr/bin/env python

from reworker import Worker

w = Worker()
w.register()
w.set_status(q=1)
w.unregister()
