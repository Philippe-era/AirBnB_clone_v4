#!/usr/bin/python3
# file form the web server
import os.path
from fabric.api import run
from fabric.api import env
from fabric.api import put

env.hosts = ["54.160.85.72", "35.175.132.106"]


def do_deploy(archive_path):
    """ARCHIVE WELL DISTRIBUTED
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
       THE FILE IN STAR
    """
    if os.path.isfile(archive_path) is False:
        return False
    file_create = archive_path.split("/")[-1]
    name = file_create.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file_create)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file_create)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True

