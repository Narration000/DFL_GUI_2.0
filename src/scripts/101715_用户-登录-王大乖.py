# object_id: 6710ba498207497c6e693704
import automation_steps
import os
import logging
log_filename = os.path.splitext(__file__)[0] + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('开始==========')
print('开始')
automation_steps.set_flag_use_model('用户')
client = automation_steps.initialize_client()
automation_steps.login('15100001111', 'aaaa1111')
print('结束')
logging.info('结束**********')
