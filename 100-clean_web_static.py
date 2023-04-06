#!/usr/bin/python3
"""
Fabric script deletes out of date version using do_clean function
"""


from fabric.api import local, env, cd
from datetime import datetime
from os import listdir, path

env.hosts = ["34.224.94.161", "35.153.232.246"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    Deletes out of date archives
    """
    number = int(number)
    if number >= 0 and number <= 1:
        val = 1
    elif number > 1:
        val = number
    files = []
    fil = sorted(listdir("versions"))
    fil_num = len(fil)
    for i in range(fil_num - val):
        files.append(fil[i])

    for x in files:
        file_name = "versions/{}".format(x)
        local("rm -rf {}".format(file_name))

    with cd("/data/web_static/releases"):
        fil = run("ls").split()
        allfiles = []
        for y in range((len(fil) - val)):
            allfiles.append(fil[y])
        for i in allfiles:
            run("rm -rf {}".format(i))
