import base64, logging

from pyamf.remoting import RemotingError
from pyamf.remoting.client import RemotingService


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s'
)

# login details
username = password = 'admin'
url = 'http://localhost:8000/login/rpc'
client = RemotingService(url, logger=logging)

# add authentication
auth = base64.encodestring('%s:%s' % (username, password))[:-1]
client.addHTTPHeader("Authorization", "Basic %s" % auth)

# call service
service = client.getService('system')
version = service.getAPIVersion()

print "Trac-RPC version: %s.%s" % (version[0], version[1])
