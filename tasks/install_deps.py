from subprocess import *
import os
import signal

# Variables
pip_path = os.path.isfile("/usr/local/bin/pip")
pip_url = "https://bootstrap.pypa.io/get-pip.py"
pip_file = "/tmp/get-pip.py"


def check_pip():
    if pip_path == False:
        print("pip is not installed on this node, installing it now...")
        call(["curl", pip_url, "-o", pip_file])
        call(["python", pip_file])
        os.remove(pip_file)
    else:
        print("pip was found to be installed, continuing...")


def install_pyvmomi():
    call(["pip", "install", "--upgrade", "pyvmomi"])


def install_vm_sdk():
    call(["pip", "install", "--upgrade",
          "git+https://github.com/vmware/vsphere-automation-sdk-python.git"])


check_pip()
install_pyvmomi()
install_vm_sdk()
