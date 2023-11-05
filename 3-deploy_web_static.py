#!/usr/bin/python3
# file will distributed done and dusted
import os.path
from datetime import datetime
from fabric.api import local
from fabric.api import put
from fabric.api import run
from fabric.api import env


env.hosts = ["54.160.85.72", "35.175.132.106"]


def do_pack():
"""zipped archive involved in and checked"""
date_create = datetime.utcnow()
file_new = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_create.year,
date_create.month,
date_create.day,
date_create.hour,
date_create.minute,
date_create.second)
if os.path.isdir("versions") is False:
if local("mkdir -p versions").failed is True:
return None
if local("tar -cvzf {} web_static".format(file_new)).failed is True:
return None
return file


def do_deploy(archive_path):
"""evenly distributed and sorted
Args:
archive_path (str): The path of the archive to distribute.
Returns:
file is on site and fixed
"""
if os.path.isfile(archive_path) is False:
return False
file_new = archive_path.split("/")[-1]
name = file_new.split(".")[0]

if put(archive_path, "/tmp/{}".format(file_new)).failed is True:
return False
if run("rm -rf /data/web_static/releases/{}/".
format(name)).failed is True:
return False
if run("mkdir -p /data/web_static/releases/{}/".
format(name)).failed is True:
return False
if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
format(file_new, name)).failed is True:
return False
if run("rm /tmp/{}".format(file_new)).failed is True:
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


def deploy():
"""distribute web server because they are baie"""
file_new = do_pack()
if file_new is None:
return False
return do_deploy(file_new)
