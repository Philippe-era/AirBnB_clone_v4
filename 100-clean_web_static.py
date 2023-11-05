#!/usr/bin/python3
# out of date archives will be eradicated
import os
from fabric.api import *

env.hosts = ["54.160.85.72", "35.175.132.106"]


def do_clean(number=0):
    """old archives will be deleted
    Args:
        number (int): the number of archives will be deleted
    """
    number = 1 if int(number) == 0 else int(number)

    archives_replace = sorted(os.listdir("versions"))
    [archives_replace.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives_replace]

    with cd("/data/web_static/releases"):
        archives_replace = run("ls -tr").split()
        archives_replace = [a for a in archives_replace if "web_static_" in a]
        [archives_replace.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives_replace]
