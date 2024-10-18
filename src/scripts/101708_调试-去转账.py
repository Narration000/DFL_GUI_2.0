# object_id: 67105d49a2484e0a4fab8973
import automation_steps
import os
import logging
log_filename = os.path.splitext(__file__)[0] + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('开始==========')
print('开始')
automation_steps.set_flag_use_model('调试')
client = automation_steps.initialize_client()
automation_steps.all_features_to_click('转账')
automation_steps.transfer_accounts('李富国', '6231500010381264', '1017.01')
print('结束')
logging.info('结束**********')
