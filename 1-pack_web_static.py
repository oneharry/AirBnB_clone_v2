#!/usr/bin/python3
"""
generates a .tgz archive from contents of the web_static
"""


from fabric.api import sudo, run, local
from datetime import datetime


def do_pack():
    """ Return the archive path of generated .tgz archive"""
    local("mkdir -p versions")
    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    print(time)
    path = "versions/web_static_{}.tgz".format(time)
    arch = local("tar -cvzf {} web_static".format(path))
    if arch.succeeded:
        return arch
    return None
