# object_id: 6710e05ac0aa34b2756a197f
import automation_steps
import os
import logging
log_filename = os.path.splitext(__file__)[0] + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('开始==========')
print('开始')
automation_steps.set_flag_use_model('调试')
client = automation_steps.initialize_client()
automation_steps.get_ver_code()
print('结束')
logging.info('结束**********')
