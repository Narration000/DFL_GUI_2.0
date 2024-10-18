import argparse
import os
import logging
import automation_steps


log_filename = os.path.splitext(__file__)[0] + '.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')

# 在这里导入自定义的模块
def process_arguments(arg1, arg2):
    logging.info('开始==========')
    # 在这里处理传入的参数
    print(f"Argument 1: {arg1}")
    print(f"Argument 2: {arg2}")
    automation_steps.set_flag_use_model('用户')
    client = automation_steps.initialize_client()
    automation_steps.login(arg1, arg2)
    logging.info('结束**********')

def main():
    parser = argparse.ArgumentParser(description="接收传参并运行的模版")
    parser.add_argument('--arg1', type=str, required=True, help='账户')
    parser.add_argument('--arg2', type=str, required=True, help='密码')
    
    args = parser.parse_args()
    
    process_arguments(args.arg1, args.arg2)

if __name__ == "__main__":
    main()