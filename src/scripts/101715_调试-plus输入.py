# object_id: 6710be6d8207497c6e693707
import automation_steps
import os
import logging
log_filename = os.path.splitext(__file__)[0] + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('开始==========')
print('开始')
automation_steps.set_flag_use_model('调试')
client = automation_steps.initialize_client()
automation_steps.click_some_keyboard('plus', 'aaaa1111')
print('结束')
logging.info('结束**********')
