__author__ = 'Howard'

from tempfile import mkstemp
import shutil
import os
import re


def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path, 'r') as old_file:
            for line in old_file:
                new_file.write(re.sub(pattern, subst, line))
    os.close(fh)
    # Remove original file
    os.remove(file_path)
    # Move new file
    shutil.move(abs_path, file_path)
