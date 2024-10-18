# object_id: 6710b0458207497c6e6936c0
import automation_steps
import os
import logging
log_filename = os.path.splitext(__file__)[0] + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('开始==========')
print('开始')
client = automation_steps.initialize_client()
automation_steps.login('18590259129', 'aaaa1111')
automation_steps.all_features_to_click('转账')
automation_steps.transfer_accounts('李富国', '6231500010381264', '300')
print('结束')
logging.info('结束**********')
