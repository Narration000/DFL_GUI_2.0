import wda
import time
import requests
import logging


# 设置超时时间
# wda.HTTP_TIMEOUT = 10
# 用户模式
# # 连接到设备
# c = wda.Client('http://172.20.10.1:8100')
# c.implicitly_wait(10.0)
# # 启动应用
# client = c.session('com.cjccb.MobileBank')

# 调试模式
# client = wda.Client('http://172.20.10.1:8100')
# client.implicitly_wait(10.0)
# 启动应用
# client = c.session('com.cjccb.MobileBank')

flagUseModel = "用户"
client = None


def set_flag_use_model(value):
    global flagUseModel
    flagUseModel = value

# False 为调试模式，True 为用户模式
def initialize_client():
    global flagUseModel, client
    if flagUseModel == "调试":
        client = wda.Client('http://172.20.10.1:8100')
        client.implicitly_wait(10.0)
    # client = wda.USBClient()
    elif flagUseModel == "用户":
        c = wda.Client('http://172.20.10.1:8100')
        c.implicitly_wait(10.0)
        # 关闭应用
        c.app_stop('com.cjccb.MobileBank')
        # 启动应用
        client = c.session('com.cjccb.MobileBank')
    return client



# 非乱序安全键盘对应坐标
def keyboard_plus(character):
    characters_dict = { 'q': (0.05, 0.7), 'w': (0.15, 0.7), 'e': (0.25, 0.7), 'r': (0.35, 0.7), 't': (0.45, 0.7), 'y': (0.55, 0.7), 'u': (0.65, 0.7), 'i': (0.75, 0.7), 'o': (0.85, 0.7), 'p': (0.95, 0.7), \
                        'a': (0.1, 0.77), 's': (0.2, 0.77), 'd': (0.3, 0.77), 'f': (0.4, 0.77), 'g': (0.5, 0.77), 'h': (0.6, 0.77), 'j': (0.7, 0.77), 'k': (0.8, 0.77), 'l': (0.9, 0.77), \
                        'z': (0.2, 0.84), 'x': (0.3, 0.84), 'c': (0.4, 0.84), 'v': (0.5, 0.84), 'b': (0.6, 0.84), 'n': (0.7, 0.84), 'm': (0.8, 0.84), \
                        '1': (0.05, 0.7), '2': (0.15, 0.7), '3': (0.25, 0.7), '4': (0.35, 0.7), '5': (0.45, 0.7), '6': (0.55, 0.7), '7': (0.65, 0.7), '8': (0.75, 0.7), '9': (0.85, 0.7), '0': (0.95, 0.7), \
                            'up': (0.05, 0.84), 'back': (0.94, 0.84), 'change': (0.12, 0.91), 'finsh': (0.88, 0.91) }

    return characters_dict[character][0], characters_dict[character][1]


# 金融键盘对应坐标
def keyboard_num(character):
    characters_dict = { '1': (0.15, 0.72), '2': (0.50, 0.72), '3': (0.85, 0.72), \
                        '4': (0.15, 0.79), '5': (0.50, 0.79), '6': (0.85, 0.79),  \
                        '7': (0.15, 0.86), '8': (0.50, 0.86), '9': (0.85, 0.86),  \
                        '.': (0.15, 0.93), '0': (0.50, 0.93) }
    return characters_dict[character][0], characters_dict[character][1]


# 乱序安全键盘对应坐标
# def keyboard_pro(number_string, number):
#     num_list = list(number_string)
#     print(num_list)
#     numbers_dict = { num_list[0]: (0.15, 0.72), num_list[1]: (0.40, 0.72), num_list[2]: (0.65, 0.72), \
#                         num_list[3]: (0.15, 0.79), num_list[4]: (0.40, 0.79), num_list[5]: (0.65, 0.79),  \
#                         num_list[6]: (0.15, 0.86), num_list[7]: (0.40, 0.86), num_list[8]: (0 ),  \
#                         num_list[9]: (0.15, 0.93) }
#     return numbers_dict[number][0], numbers_dict[number][1]


def get_ver_code():
    url = 'http://172.20.10.5:5000/get_vercode'
    if client(predicate='name LIKE "短信验证码已发送*"').exists:
        phone = client(predicate='name LIKE "短信验证码已发送*"').value[-4:]
    elif client.xpath('//XCUIElementTypeTextField[@label="手机号码"]').exists:
        phone = client.xpath('//XCUIElementTypeTextField[@label="手机号码"]').value
        
    payload = {'phone': phone}
    response = requests.get(url, params=payload)
    ver_code = response.text
    print(ver_code)
    return ver_code


# 乱序安全键盘输入
def input_use_keyboard_pro(pwd):
    url = 'http://172.20.10.5:5000/upload_image'
    # /Users/mac/Narration/test-wda/tmp
    client.screenshot('./tmp/test2.png')
    image_path = './tmp/test2.png'
    with open(image_path, 'rb') as img_file:
        files = {'image': img_file}
        payload = {'pwd': pwd}
        response = requests.post(url, files=files, data=payload)
        pwd_loaction_list = response.json()
        # pwd_loaction_list = list(response.text)
    # print(pwd_loaction_list[0])

    for pwd_loaction in pwd_loaction_list:
        x = pwd_loaction[0]
        y = pwd_loaction[1]
        print(x, y)
        client.click(x, y)
        time.sleep(1.0)
    client.click(0.5, 0.5)



# 非乱序安全键盘输入
def input_use_keyboard_plus(string):
    # 0 is character, 1 is number
    flag = 0
    for character in string:
        if character.isdigit():
            if flag == 0:
                client.click(*keyboard_plus('change'))
                flag = 1
            client.click(*keyboard_plus(character))
        elif character.isalpha():
            if flag == 1:
                client.click(*keyboard_plus('change'))
                flag = 0
            if character.isupper():
                client.click(*keyboard_plus('up'))
                client.click(*keyboard_plus(character.lower()))
                client.click(*keyboard_plus('up'))
            else:
                client.click(*keyboard_plus(character))
        else:
            if flag == 1:
                client.click(*keyboard_plus('change'))
                flag = 0
        time.sleep(0.1)

# 金融键盘输入
def input_use_keyboard_num(string):
    for character in string:
        client.click(*keyboard_num(character))
        time.sleep(0.3)
    client.click(0.5, 0.5)


def wait_for_element():
    while True:
        visibleCount = client.xpath('//XCUIElementTypeImage[@visible="false"]').count()
        if visibleCount != 2:
            break
        elif visibleCount == 2:
            if client(name = '关闭').exists:
                break
        time.sleep(0.3)
    print('等待结束')

# 登录功能
def login(username, password):
    client(name = '我的').click()
    time.sleep(1)
    # 关闭可能存在的弹窗
    try:
        if client(name = '不再显示该弹窗').exists:
            client(label = 'guiDance closed').click()
            time.sleep(0.2)
        print('关闭弹窗')
    except:
        print('无弹窗')
        pass
    logging.info('已确认无弹窗')
    client(name = '登录/注册').click()
    # click_something('登录/注册')
    # 如果已经登录过，且登录账户尾号与传参一致，直接输入密码
    if client(value = '请输入密码').exists:
        if username[-4:] == client(predicate='name LIKE "用户*"').value[-4:]:
            client(value = '请输入密码').click()
            time.sleep(1)
            input_use_keyboard_plus(password)
            client(name = '登录').click()
            print('已登录')
    # 否则，切换用户登录
    elif client(name = '切换用户登录').exists:
        client(name = '切换用户登录').click()

        client(name = 'remember-no').click()
        client(value = '请输入手机号码/身份证号码').set_text(username)
        
        client(name = '注册/登录').click()

        client(value = '请输入密码').click()
        time.sleep(1)
        input_use_keyboard_plus(password)
        client(name = '登录').click()
        print('登录成功')
    else:
        client(name = 'remember-no').click()
        client(value = '请输入手机号码/身份证号码').set_text(username)
        client(name = '注册/登录').click()

        client(value = '请输入密码').click()
        time.sleep(1)
        input_use_keyboard_plus(password)
        client(name = '登录').click()
        print('登录成功')

# 转账功能
def transfer_accounts(receipt_name, receipt_account, amount):
    client(name = '账号转账').click()
    wait_for_element()
    client(name = '收款姓名').set_text(receipt_name)
    client(name = '收款账户').set_text(receipt_account)
    client(name = '收款银行').click()
    wait_for_element()
    client(value = '请输入金额').click()
    input_use_keyboard_num(amount)
    client(name = '下一步').click()

    if client(name = '温馨提示').exists:
        client(name = '确认').click_exists()
        client(name = '确定').click_exists()

    wait_for_element()
    client(value = '请输入验证码').set_text(get_ver_code())
    client(name = '下一步').click()
    print('下一步')
    wait_for_element()
    print('下一步结束')

    client.click(0.45, 0.51)
    input_use_keyboard_pro('369258')
    client(name = '确定').click()


# 全部功能菜单点击
def all_features_to_click(tableName):
    client(name = '首页').click()
    # 关闭可能存在的弹窗
    try:
        if client(name = '不再显示该弹窗').exists:
            client(label = 'guiDance closed').click()
            time.sleep(0.2)
        print('关闭弹窗')
    except:
        print('无弹窗')
        pass
    logging.info('已确认无弹窗')
    client(name = '全部功能').click()

    features_dic = {
        '账户': ['账户总览', '卡管理', '交易查询', '数字人民币', '同号换卡', '同号卡激活'],
        '转账': ['收款人管理', '转账', '预约转账', '手机号转账', '转账记录查询'],
        '存款': ['零存整取', '大额存单', '通知存款', '定期存款', '金钱包'],
        '贷款': ['我的贷款', '贷款', '任意花', '舒心贷', '多存少还', '个人结清证明'],
        '企业服务': ['交易明细', '对公转账', '企业贷款', '抵息活动', '代发工资', '易企赢'],
        '儿童金融': ['儿童金融', '儿童卡管理', '发红包', '未来金计划', '成长树存款'],
        '客户服务': ['视频柜员', '存款证明', '银行网点', '个人设置', '金融助手', '客户权益'],
        '生活服务': ['消费券', '热门活动', '生活缴费', '一键绑卡', '推荐有礼']
    }
    for key in features_dic:
        if tableName in features_dic[key]:
            print(key)
            print(features_dic[key])
            logging.info(f'key: {key}')
            logging.info(f'features_dic[key]: {features_dic[key]}')
            element = client.xpath(f'//XCUIElementTypeScrollView//XCUIElementTypeButton/XCUIElementTypeStaticText[@label="{key}"]').get()
            # 获取元素的边界 (bounds)
            bounds = element.bounds
            x = bounds.x
            y = bounds.y
            print('x:', x, 'y:', y)
            client.click(x, y)
            time.sleep(0.3)
            print('tableName:', tableName)
            client.xpath(f'//XCUIElementTypeTable[last()]/XCUIElementTypeCell/XCUIElementTypeStaticText[@label="{tableName}"]').click()
            wait_for_element()
            break
    # client.xpath(f"//XCUIElementTypeTable[2]//XCUIElementTypeStaticText[@label='{tableName}'][last()]").click()
    # client.xpath(f'//XCUIElementTypeScrollView//*[@label="{scrollName}"]').click()
    # client.xpath(f'//XCUIElementTypeTable[last()]/XCUIElementTypeCell/XCUIElementTypeStaticText[@label="{tableName}"]').click()


def click_something(nameOrValue, e_property):
    if nameOrValue == 'name':
        try:
            client(name = e_property).click()
            logging.info(f'点击{nameOrValue}')
        except:
            logging.info(f'未找到{nameOrValue}')
            pass
    elif nameOrValue == 'value':
        try:
            client(value = e_property).click()
            logging.info(f'点击{nameOrValue}')
        except:
            logging.info(f'未找到{nameOrValue}')
            pass


def input_something(nameOrValue, e_property, text):
    if nameOrValue == 'name':
        try:
            client(name = e_property).set_text(text)
            logging.info(f'输入{nameOrValue}')
        except:
            logging.info(f'未找到{nameOrValue}')
            pass
    elif nameOrValue == 'value':
        try:
            client(value = e_property).set_text(text)
            logging.info(f'输入{nameOrValue}')
        except:
            logging.info(f'未找到{nameOrValue}')
            pass



if __name__ == '__main__':
    pass