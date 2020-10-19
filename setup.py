import os
from setuptools import setup, find_packages
import zipapp

from distutils.cmd import Command

class ZipAppCommand(Command):
    description = "create a zipapp executable file"
    user_options = [
        ("dist-dir=", None, "directory to put final built distributions in [default: dist]"),
        ("exec-name=", None, "file name of executable [default: vnc-keysnail]"),
    ]

    def initialize_options(self):
        self.dist_dir = "dist"
        self.exec_name = "vnc-keysnail"

    def finalize_options(self):
        pass

    def run(self):

        def zipapp_filter(path):
            return str(path).startswith("vnc_keysnail/")

        out = os.path.join(self.dist_dir, self.exec_name)
        srcdir = os.path.dirname(__file__)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        zipapp.create_archive(
            srcdir, out,
            main="vnc_keysnail:main",
            interpreter="/usr/bin/python3",
            filter=zipapp_filter)

version_path = os.path.join(os.path.dirname(__file__), "pdddar", "__version__.py")
with open(version_path) as fin:
    line = fin.readline()
    version = line.split()[-1]

setup(
    cmdclass={
        "zipapp" : ZipAppCommand,
    },
    name="pdddar",
    version=version,
    packages=find_packages(),
)
