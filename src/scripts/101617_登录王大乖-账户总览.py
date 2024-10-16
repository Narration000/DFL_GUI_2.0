# object_id: 670f8e9a15b14018a6bd131d
import automation_steps
import os
import logging
log_filename = os.path.splitext(__file__)[0] + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('开始==========')
print('开始')
client = automation_steps.initialize_client()
automation_steps.login('15100001111', 'aaaa1111')
automation_steps.all_features_to_click('账户总览')
print('结束')
logging.info('结束**********')
