Serverless-local-debugger
=========================

Very convenient debugging tool for serverless
'''''''''''''''''''''''''''''''''''''''''''''

Support:
''''''''

-  [x] AWS
-  [x] ALI

Install
'''''''

.. code:: sh

    python setup.py sdist bdist_wheel   
    cd dist && pip3 install  *.whl

    OR

    pip install serverless-local-debugger

Usage
'''''

+-------------------+-------------------------------+------------------------------+
| Static Variable   | Description                   | Default                      |
+===================+===============================+==============================+
| AWS\_AK\_ENV      | AWS ACCESS\_KEY ENV NAME      | AWS\_ACCESS\_KEY\_ID         |
+-------------------+-------------------------------+------------------------------+
| AWS\_SK\_ENV      | AWS SECRET\_KEY ENV NAME      | AWS\_SECRET\_ACCESS\_KEY     |
+-------------------+-------------------------------+------------------------------+
| AWS\_ENTRYPOINT   | AWS Function Entrypoint       | AWS Function Entrypoint      |
+-------------------+-------------------------------+------------------------------+
| ALI\_AK\_ENV      | Aliyun ACCESS\_KEY ENV NAME   | accessKeyID                  |
+-------------------+-------------------------------+------------------------------+
| ALI\_SK\_ENV      | Aliyun SECRET\_KEY ENV NAME   | accessKeySecret              |
+-------------------+-------------------------------+------------------------------+
| ALI\_ENTRYPOINT   | Aliyun Function Entrypoint    | Aliyun Function Entrypoint   |
+-------------------+-------------------------------+------------------------------+

=======

support ali cloud function decode

=======

More --->> See `Examples <https://github.com/kekeee-shine/serverless-local-debugger/tree/main/examples>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
