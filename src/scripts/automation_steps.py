import wda
import time
import requests


# 设置超时时间
wda.HTTP_TIMEOUT = 10
# 连接到设备
c = wda.Client('http://172.20.10.1:8100')
c.implicitly_wait(10.0)
# 启动应用
client = c.session('com.cjccb.MobileBank')

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


def input_ver_code(phone):
    url = 'http://172.20.10.5:5000/get_vercode'
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
        time.sleep(0.3)
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


# 登录功能
def login(username, password):
    client(name = '我的').click()
    time.sleep(1)
    # 关闭可能存在的弹窗
    while client(name = '不再显示该弹窗').exists:
        client(label = 'guiDance closed').click()
        time.sleep(0.2)

    client(name = '登录/注册').click()

    if client(name = '切换用户登录').exists:
        client(name = '切换用户登录').click()

    client(name = 'remember-no').click()
    client(value = '请输入手机号码/身份证号码').set_text(username)
    
    client(name = '注册/登录').click()

    client(value = '请输入密码').click()
    time.sleep(1)
    input_use_keyboard_plus(password)
    client(name = '登录').click()


# 转账功能
def transfer_accounts(receipt_name, receipt_account, amount):
    client(name = '首页').click()
    client(name = '全部功能').click()
    all_features_to_click('转账', '转账')
    client(name = '账号转账').click()
    time.sleep(5)
    client(name = '收款姓名').set_text(receipt_name)
    client(name = '收款账户').set_text(receipt_account)
    client(name = '收款银行').click()
    time.sleep(5)
    client(value = '请输入金额').click()
    input_use_keyboard_num(amount)
    client(name = '下一步').click()
    time.sleep(5)
    client(value = '请输入验证码').set_text(input_ver_code(userPhoneNum))
    client(name = '下一步').click()
    time.sleep(2)

    client.click(0.45, 0.51)
    input_use_keyboard_pro('369258')
    client(name = '确定').click()

# 全部功能菜单点击
def all_features_to_click(scrollName, tableName):
    client.xpath(f'//XCUIElementTypeScrollView//*[@label="{scrollName}"]').click()
    client.xpath(f'//XCUIElementTypeTable[last()]/XCUIElementTypeCell/XCUIElementTypeStaticText[@label="{tableName}"]').click()

if __name__ == '__main__':
    print('开始')
    print('登录')
    userPhoneNum = '13055508296'
    userPassword = 'aaaa1111'

    login(userPhoneNum, userPassword)
    print('登录成功')
    # print('转账')
    # transfer_accounts('李富国', '6231500010381264', '623.02')

    print('结束')