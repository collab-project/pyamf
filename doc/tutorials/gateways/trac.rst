********
  Trac 
********

.. image:: images/trac-logo.png


.. topic:: Introduction

    PyAMF provides a simple WSGI Application that can be used to setup RPC
    style service easily in Python. Because
    Trac_ supports WSGI from top-to-bottom, it's very simple to setup
    a Trac environment that contains web-services for your Flex and Flash applications.

.. contents::

Installation
============

If you haven't installed Trac_, you'll need to do that first_ (``easy_install trac``).

Next install the `Trac XML-RPC Plugin`_ (requires Subversion_)::

  svn co http://trac-hacks.org/svn/xmlrpcplugin/trunk xmlrpc-plugin-trunk
  cd xmlrpc-plugin-trunk
  python setup.py install
  cd ..

Finally install the TracRpcProtocolsPlugin_ (requires Mercurial_)::

  hg clone http://simelo.hg.sourceforge.net:8000/hgroot/simelo/trac-rpcext
  cd trac-rpcext/trac-dev/rpcext
  python setup.py install
  cd ..

Configuration
=============

Create a new Trac environment::

  trac-admin amf_test initenv

Create an ``admin`` user for Trac authentication using the
``htpasswd`` utility::

  htpasswd -c amf_test/.htpasswd admin

Assign administrator permissions to the Trac user::

  trac-admin amf_test permission add admin TRAC_ADMIN

Enable the plugins in the ``[components]`` section of
``amf_test/conf/trac.ini``::

  [components] 
  tracrpc.* = enabled
  tracrpcext._amf.* = enabled

Enabling the console logger for Trac is useful for troubleshooting. Update the
``[logging]`` section like this (or use the Trac `web admin`_)::

  [logging]
  log_level = DEBUG
  log_type = stderr

Now start the ``tracd`` development server::

  tracd --port=8000 --hostname=localhost --single-env --auto-reload --basic-auth="amf_test,amf_test/.htpasswd,AMF Test" amf_test

You should now be able to browse your environment at http://localhost:8000.


Testing the Trac remoting gateway
=================================

Now it's time to test the Trac remoting gateway.

Python
------

The first thing to do is to create a new Python AMF client. Create a file
called ``client.py`` file wherever you want with the following contents:

.. literalinclude:: ../examples/gateways/trac/client.py
   :linenos:

This ...[TODO]...
   
Flex
----

Now we're ready for the big time event, we can create a brand new Flex client
which talks to our Trac hosted PyAMF services. This little tutorial pretty much
assumes that you know how to use Flex and just want to see how to connect it to
a Trac instance.

Here's the MXML:

.. literalinclude:: ../examples/gateways/trac/flex/app.mxml
   :language: xml
   :linenos:


.. _Trac:                       http://trac.edgewall.org
.. _first:                      http://trac.edgewall.org/wiki/TracInstall
.. _TracRpcProtocolsPlugin:     http://trac-hacks.org/wiki/TracRpcProtocolsPlugin
.. _Trac XML-RPC Plugin:        http://trac-hacks.org/wiki/XmlRpcPlugin
.. _Subversion:                 http://subversion.apache.org
.. _Mercurial:                  http://mercurial.selenic.com
.. _web admin:                  http://localhost:8000/admin/general/logging
