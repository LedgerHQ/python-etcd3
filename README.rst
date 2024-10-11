============
python-etcd3
============


.. image:: https://img.shields.io/pypi/v/etcd3.svg
        :target: https://pypi.python.org/pypi/etcd3

.. image:: https://img.shields.io/travis/kragniz/python-etcd3.svg
        :target: https://travis-ci.org/kragniz/python-etcd3

.. image:: https://readthedocs.org/projects/python-etcd3/badge/?version=latest
        :target: https://python-etcd3.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/kragniz/python-etcd3/shield.svg
     :target: https://pyup.io/repos/github/kragniz/python-etcd3/
     :alt: Updates

.. image:: https://codecov.io/github/kragniz/python-etcd3/coverage.svg?branch=master
        :target: https://codecov.io/github/kragniz/python-etcd3?branch=master


Python client for the etcd API v3, supported under python 2.7, 3.4 and 3.5.

**Warning: the API is mostly stable, but may change in the future**

If you're interested in using this library, please get involved.

* Free software: Apache Software License 2.0
* Documentation: https://python-etcd3.readthedocs.io.

Generate proto stubs:

.. code-block:: bash
    python -m grpc_tools.protoc -Ietcd3/proto --python_out=etcd3/etcdrpc --grpc_python_out=etcd3/etcdrpc etcd3/proto/rpc.proto
    python -m grpc_tools.protoc -Ietcd3/proto --python_out=etcd3/etcdrpc etcd3/proto/kv.proto
    python -m grpc_tools.protoc -Ietcd3/proto --python_out=etcd3/etcdrpc etcd3/proto/auth.proto
    # Then manually edit import path of rpc stubs
    # See: commit eea9880b0c4c2227d2374018eb6c56167526ed6b "chore: manually fix the stubs"


Generate requirements:

.. code-block:: bash
    cd requirements
    pip-compile --output-file=base.txt base.in
    pip-compile --output-file=test.txt test.in


Basic usage:

.. code-block:: python

    import etcd3

    etcd = etcd3.client()

    etcd.get('foo')
    etcd.put('bar', 'doot')
    etcd.delete('bar')

    # locks
    lock = etcd.lock('thing')
    lock.acquire()
    # do something
    lock.release()

    with etcd.lock('doot-machine') as lock:
        # do something

    # transactions
    etcd.transaction(
        compare=[
            etcd.transactions.value('/doot/testing') == 'doot',
            etcd.transactions.version('/doot/testing') > 0,
        ],
        success=[
            etcd.transactions.put('/doot/testing', 'success'),
        ],
        failure=[
            etcd.transactions.put('/doot/testing', 'failure'),
        ]
    )

    # watch key
    watch_count = 0
    events_iterator, cancel = etcd.watch("/doot/watch")
    for event in events_iterator:
        print(event)
        watch_count += 1
        if watch_count > 10:
            cancel()

    # watch prefix
    watch_count = 0
    events_iterator, cancel = etcd.watch_prefix("/doot/watch/prefix/")
    for event in events_iterator:
        print(event)
        watch_count += 1
        if watch_count > 10:
            cancel()

    # recieve watch events via callback function
    def watch_callback(event):
        print(event)

    watch_id = etcd.add_watch_callback("/anotherkey", watch_callback)

    # cancel watch
    etcd.cancel_watch(watch_id)

    # recieve watch events for a prefix via callback function
    def watch_callback(event):
        print(event)

    watch_id = etcd.add_watch_prefix_callback("/doot/watch/prefix/", watch_callback)

    # cancel watch
    etcd.cancel_watch(watch_id)
