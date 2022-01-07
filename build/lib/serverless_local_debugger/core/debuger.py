import abc
import os
import importlib as importlib
import json
from typing import Optional


class StaticVar:
    AWS_AK_ENV = 'AWS_ACCESS_KEY_ID'
    AWS_SK_ENV = 'AWS_SECRET_ACCESS_KEY'
    AWS_ENTRYPOINT = 'lambda_handler'

    ALI_AK_ENV = 'accessKeyID'
    ALI_SK_ENV = 'accessKeySecret'
    ALI_ENTRYPOINT = 'handler'

    @staticmethod
    def get_entrypoint() -> dict:
        return {'AWS': StaticVar.AWS_ENTRYPOINT, 'ALI': StaticVar.ALI_ENTRYPOINT}


class FakeContext:
    def __init__(self):
        self.invoked_function_arn = "invoked_function_arn"


def os_env_check(env):
    if not os.environ.get(env):
        raise Exception("The env {} must be set".format(env))


class ServerlessDebugger(abc.ABC):
    CONTEXT = FakeContext()

    def __init__(self, function, envs: dict, event: dict = None, event_path: str = None):
        if not event and not event_path:
            raise "The args 'event' and 'event_path' cannot be None at the same time"
        if event:
            self.event = event
        else:
            with open(event_path) as f:
                self.event = json.load(f)
        self.cloud_type = 'AWS'
        self.envs = envs
        self.function = function

    @staticmethod
    @abc.abstractmethod
    def _specific_envs() -> Optional[dict]:
        return {}

    def run(self):
        env = self._specific_envs()
        env.update(self.envs)

        for k, v in env.items():
            os.environ[k] = v
        module = importlib.import_module(self.function)
        ep = StaticVar.get_entrypoint()
        if self.cloud_type == 'ALI':
            # 适配ali function的解析方式：
            # json.loads(event.decode())
            self.event = json.dumps(self.event).encode()
        rsp = module.__dict__[ep[self.cloud_type]](self.event, self.CONTEXT)
        return rsp


class AWSServerlessDebugger(ServerlessDebugger):
    def __init__(self, function, envs: dict, event: dict = None, event_path: str = None):
        super().__init__(function, envs, event, event_path)
        self.cloud_type = 'AWS'

    @staticmethod
    def _specific_envs():
        os_env_check(StaticVar.AWS_AK_ENV)
        os_env_check(StaticVar.AWS_SK_ENV)
        envs = {'AWS_ACCESS_KEY_ID': os.environ.get(StaticVar.AWS_AK_ENV),
                'AWS_SECRET_ACCESS_KEY': os.environ.get(StaticVar.AWS_SK_ENV),
                'AWS_XRAY_SDK_ENABLED': 'false'}
        return envs


class ALIServerlessDebugger(ServerlessDebugger):
    def __init__(self, function, envs: dict, event: dict = None, event_path: str = None):
        super().__init__(function, envs, event, event_path)
        self.cloud_type = 'ALI'

    @staticmethod
    def _specific_envs():
        os_env_check(StaticVar.ALI_AK_ENV)
        os_env_check(StaticVar.ALI_SK_ENV)
        envs = {'accessKeyID': os.environ.get(StaticVar.ALI_AK_ENV),
                'accessKeySecret': os.environ.get(StaticVar.ALI_SK_ENV)}
        return envs
