# -*- coding: utf-8 -*-

import os
from mimetypes import guess_type
from .browser import FileIterator, FileIterable


class Folder(Location):

    def __init__(self, path):
        assert os.path.isdir(path)
        self.root_path = path

    def get_file(self, name):
        path = os.path.join(self.root_path, name)
        assert os.path.isfile(path)
        iterator = FileIterator(open(path, 'rb'))
        size = os.path.getsize(path)
        return name, iterator, size

    def keys(self):
        return os.listdir(self.root_path)
    
    def __getitem__(self, name):
        filename, data, size = self.get_file(name)
        type, encoding = guess_type(filename)
        return FileIterable.make_response(data, name, type, size)
