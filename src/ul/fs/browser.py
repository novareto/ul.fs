# -*- coding: utf-8 -*-

import os
from cromlech.webob import Response
from mimetypes import guess_type

CHUNK_SIZE = 1 << 12


class FileIterable(object):

    def __init__(self, iterator):
        self.iterator = iterator

    def __iter__(self):
        return iter(self.iterator)

    @classmethod
    def make_response(cls, file, filename, content_type, content_length):
        fileobj = cls(file)
        res = Response(content_type=content_type)
        res.content_disposition = 'attachment; filename="%s"' % filename
        res.app_iter = fileobj
        res.content_length = content_length
        return res


class FileIterator(object):
    chunk_size = CHUNK_SIZE

    def __init__(self, f):
        self.fp = f

    def __iter__(self):
        return self

    def next(self):
        chunk = self.fp.read(self.chunk_size)
        if not chunk:
            self.fp.close()
            raise StopIteration
        return chunk
