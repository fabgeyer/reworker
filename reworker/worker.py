#!/usr/bin/env python

import os
import json
import redis
import uuid
import platform


class Worker(object):
    def __init__(self, key=None, config=None, expire=300):
        self.config = {
            'host': 'localhost',
            'port': 6379,
            'db': 0,
            'password': None,
        }
        if config is not None:
            self.config.update(config)

        self.rdb = None
        self.expire = expire
        self.connected = False
        self.registered = False
        if key is None:
            self.key = "reworker-{}:{}:{}".format(platform.node(), os.getpid(), str(uuid.uuid4().hex))
        else:
            self.key = "reworker-{}".format(key)
        self.connect()

    def list(self):
        if not self.connected:
            raise ConnectionError('Worker is not connected')
        try:
            return [Worker(key=name[9:].decode(), config=self.config) for name in self.rdb.keys("reworker-*")]
        except redis.exceptions.ConnectionError as err:
            raise ConnectionError(str(err))

    def connect(self):
        config = self.config
        self.rdb = redis.Redis(config['host'], config['port'], config['db'], config['password'])
        try:
            info = self.rdb.info()
            self.connected = True
        except redis.ConnectionError:
            return False
        return True

    def register(self):
        if not self.connected:
            raise ConnectionError('Worker is not connected')
        self.rdb.set(self.key, "{}")
        if self.expire > 0:
            self.rdb.expire(self.key, self.expire)
        self.registered = True
        return True

    def unregister(self):
        if not self.connected:
            raise ConnectionError('Worker is not connected')
        if not self.registered:
            raise ConnectionError('Worker is not registered')
        self.rdb.delete(self.key, "{}")
        return True

    def set_status(self, **kwargs):
        if not self.connected:
            raise ConnectionError('Worker is not connected')
        if not self.registered:
            raise ConnectionError('Worker is not registered')
        status = json.dumps(kwargs)
        self.rdb.set(self.key, status)
        if self.expire > 0:
            self.rdb.expire(self.key, self.expire)
        return True

    def get_status(self):
        if not self.connected:
            raise ConnectionError('Worker is not connected')
        status = self.rdb.get(self.key)
        return json.loads(status)

    def get_ttl(self):
        if not self.connected:
            raise ConnectionError('Worker is not connected')
        return self.rdb.ttl(self.key)
