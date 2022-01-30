#!/usr/bin/python3
"""Import FileStorage and read existing data into storage variable
using either absolute or relative path import file_storage.py
absolute path used here
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
# storage is an instance of the class FileStorage imported

storage.reload()
# calling the function reload on the variable storage(instance)
