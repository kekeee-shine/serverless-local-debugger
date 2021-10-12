from serverless_local_debugger import AWSServerlessDebugger, ALIServerlessDebugger, StaticVar
import os

os.environ['AWS_ACCESS_KEY_ID'] = 'XXX'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'XXX'
os.environ['accessKeyID'] = 'XXX'
os.environ['accessKeySecret'] = 'XXX'

AWS_DEBUGGER = AWSServerlessDebugger(function='examples.AWS.lambda', envs={'aaa': '111'},
                                     event={'bbb': '222'})
rsp1 = AWS_DEBUGGER.run()

print(rsp1)

StaticVar.ALI_AK_ENV = 'cst_accessKeyID'

ALI_DEBUGGER = ALIServerlessDebugger(function='examples.ALI.function', envs={'ccc': '333'},
                                     event_path='./example.json')
try:
    ALI_DEBUGGER.run()
except Exception as e:
    print("EEEEEEEError: {}".format(e))

StaticVar.ALI_AK_ENV = 'accessKeyID'

rsp2 = ALI_DEBUGGER.run()
print(rsp2)
