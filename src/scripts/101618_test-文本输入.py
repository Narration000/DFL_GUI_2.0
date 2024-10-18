# object_id: 670f9a7015b14018a6bd132c
import automation_steps
import os
import logging
log_filename = os.path.splitext(__file__)[0] + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('开始==========')
print('开始')
client = automation_steps.initialize_client()
automation_steps.input_something('value', '请输入手机号码/身份证号码', '123456')
print('结束')
logging.info('结束**********')
