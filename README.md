# Serverless-local-debugger

#####  Very convenient debugging tool for serverless

##### Support:

+ [x] AWS
+ [x] ALI

##### Install

```sh
python setup.py sdist bdist_wheel	
cd dist && pip3 install  *.whl

OR

pip install serverless-local-debugger
```



##### Usage

| Static Variable |        Description         |          Default           |
| :-------------: | :------------------------: | :------------------------: |
|   AWS_AK_ENV    |  AWS ACCESS_KEY ENV NAME   |     AWS_ACCESS_KEY_ID      |
|   AWS_SK_ENV    |  AWS SECRET_KEY ENV NAME   |   AWS_SECRET_ACCESS_KEY    |
| AWS_ENTRYPOINT  |  AWS Function Entrypoint   |  AWS Function Entrypoint   |
|   ALI_AK_ENV    | Aliyun ACCESS_KEY ENV NAME |        accessKeyID         |
|   ALI_SK_ENV    | Aliyun SECRET_KEY ENV NAME |      accessKeySecret       |
| ALI_ENTRYPOINT  | Aliyun Function Entrypoint | Aliyun Function Entrypoint |


=======

support ali cloud function decode 

=======



#### More --->>  See [Examples](https://github.com/kekeee-shine/serverless-local-debugger/tree/main/examples)





