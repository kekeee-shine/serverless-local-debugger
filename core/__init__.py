import os
import importlib as importlib
import json


class FakeContext:
    def __init__(self):
        self.invoked_function_arn = "invoked_function_arn"


class ServerlessDebuger:
    CONTEXT = FakeContext()

    def __init__(self, function, envs: dict, event: dict = None, event_path: str = None):
        if not event and not event_path:
            raise "The args 'event' and 'event_path' cannot be None at the same time"
        if event:
            self.event = event
        else:
            with open(event_path) as f:
                self.event = json.load(f)

        self.envs = envs
        self.function = function

    def run(self):
        env = {}
        env['AWS_ACCESS_KEY_ID'] = 'AKIAW33XGL4ASVWIXPGK'
        env['AWS_SECRET_ACCESS_KEY'] = '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'
        env['AWS_XRAY_SDK_ENABLED'] = 'false'
        env.update(self.envs)

        for k, v in env.items():
            os.environ[k] = v
        print(os.environ)
        module = importlib.import_module(self.function)
        module.__dict__['lambda_handler'](self.event, self.CONTEXT)
        print('Serverless Run Complete')
