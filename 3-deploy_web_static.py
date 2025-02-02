#!/usr/bin/python3
"""
Fabric script for sys admin automation
"""


from fabric.api import sudo, run, local, put, env
from datetime import datetime
from os.path import exists
from sys import argv

env.hosts = ["34.224.94.161", "35.153.232.246"]
env.user = "ubuntu"


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

    if not exists(archive_path):
        return False
    file_name = archive_path.split("/")[-1].split(".")[0]
    path = "/tmp/{}".format(archive_path.split("/")[-1])
    result = put(archive_path, path)
    if result.failed:
        return False
    arch_dir = "/data/web_static/releases/{}/".format(file_name)

    result = run("rm -rf {}".format(arch_dir))
    if result.failed:
        return False
    result = run("mkdir -p {}".format(arch_dir))
    if result.failed:
        return False
    result = run("tar -xzf {} -C {}".format(path, arch_dir))
    if result.failed:
        return False
    result = run("rm -rf {}".format(path))
    if result.failed:
        return False
    result = run("mv /data/web_static/releases/{}/web_static/* {}"
                 .format(file_name, arch_dir))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/{}/web_static/"
                 .format(file_name))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = run("ln -s {} /data/web_static/current".format(arch_dir))
    if result.failed:
        return False

    return True


def deploy():
    """ Deploy to web servers using the other commands"""
    arch_path = do_pack()
    if arch_path:
        return do_deploy(arch_path)
    return False
