import os
import tests


def file_path(element, path):
    element.send_keys(
        os.path.abspath(os.path.join(os.path.dirname(tests.__file__), path)))
