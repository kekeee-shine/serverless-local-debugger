import os
from setuptools import setup

# 需要将那些包导入
packages = ["serverless_local_debugger", "serverless_local_debugger.core"]

# 第三方依赖
requires = [
]

# 自动读取readme
with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='serverless-local-debugger',  # 包名称
    version="0.0.3",  # 包版本
    description="",  # 包详细描述
    long_description=readme,  # 长描述，通常是readme，打包到PiPy需要
    author="kekeee",  # 作者名称
    author_email="yangfan-shine@qq.com",  # 作者邮箱
    url="https://github.com/kekeee-shine/serverless-local-debugger",  # 项目官网
    packages=packages,  # 项目需要的包
    python_requires=">=3.0, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3*",  # Python版本依赖
    install_requires=requires,  # 第三方库依赖
    zip_safe=False,  # 此项需要，否则卸载时报windows error
    classifiers=[  # 程序的所属分类列表
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
