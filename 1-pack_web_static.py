#!/usr/bin/python3
# Pack it up web way
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Tar archived is on par"""
    date_created = datetime.utcnow()
    file_new = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_created.year,
                                                         date_created.month,
                                                         date_created.day,
                                                         date_created.hour,
                                                         date_created.minute,
                                                         date_created.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_new)).failed is True:
        return None
    return file_new

