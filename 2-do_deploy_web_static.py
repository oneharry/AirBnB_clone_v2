#!/usr/bin/python3
"""
Fabric script for sys admin automation
"""


from fabric.api import sudo, run, local
from datetime import datetime
from os.path import exists


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


def do_deploy(archive_path):
    """ Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers"""
    env.hosts = ["34.224.94.161", "35.153.232.246"]
    env.user = "ubuntu"

    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        path = "/tmp/{}".format(filename)
        put(archive_path, path)
        arch_dir = "/data/web_static/releases/{}".format(file_name)
        run("mkdir -p {}".format(new_dir))
        run("tar -zxf {} -C {}".format(path, arch_dir))
        run("rm -rf {}".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(arch_dir))
        return True
    except Exception:
        return False
