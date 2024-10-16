# object_id: 670f8fd715b14018a6bd1321
import automation_steps
import os
import logging
log_filename = os.path.splitext(__file__)[0] + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('开始==========')
print('开始')
client = automation_steps.initialize_client()
automation_steps.login('16282058411', 'aaaa1111')
automation_steps.all_features_to_click('账户总览')
print('结束')
logging.info('结束**********')
