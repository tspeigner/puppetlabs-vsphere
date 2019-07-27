import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client

vc_ip = "vcenter-1.puppetlabs.net"
vc_user = "tommy"
vc_password = "password"

session = requests.session()

session.verify = True

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

vsphere_client = create_vsphere_client(
    server=vc_ip, username=vc_user, password=vc_password, session=session)

vsphere_client.vcenter.VM.list()
