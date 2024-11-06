"""二维码登录获取cookies"""
from time import sleep
from http.cookiejar import LWPCookieJar
import requests
from re import findall
from tkinter import StringVar, Tk, messagebox
from os import path
from io import BytesIO
from PIL import Image, ImageTk
from qrcode import QRCode
from tkinter.ttk import Button, Label
from threading import Thread


temp_cookie = './res/cookie/bzcookies.txt'  # cookies保存路径
headers2 = {
    'authority': 'api.vc.bilibili.com', 'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://message.bilibili.com', 'referer': 'https://message.bilibili.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"', 'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81',
}


def is_login(session):
    """发起会话，判断是否登录成功"""
    try:
        session.cookies.load(ignore_discard=True)
    except Exception as e:
        pass
        # messagebox.showinfo(str(e))
    login_url = session.get("https://api.bilibili.com/x/web-interface/nav", verify=False, headers=headers2).json()
    if login_url['code'] == 0:
        return True
    else:
        return False


def scan_code(session2):
    """扫描二维码登录"""
    global bili_jct
    get_login = session2.get('https://passport.bilibili.com/x/passport-login/web/qrcode/generate?source=main-fe-header',
                             headers=headers2).json()
    qrcode_key = get_login['data']['qrcode_key']
    qr = QRCode()
    qr.add_data(get_login['data']['url'])
    img = qr.make_image()
    pil_image_change = img.resize((200, 200), resample=Image.BICUBIC, box=None, reducing_gap=None)
    code_pic = ImageTk.PhotoImage(pil_image_change)
    token_url = f'https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key={qrcode_key}&source=main-fe-header'
    label_ver1 = Label(root, image=code_pic)
    v1.set('等待扫码')
    label_ver1.grid(row=1, column=1, rowspan=8, columnspan=1, sticky='n')
    while 1:
        qrcode_data = session2.get(token_url, headers=headers2).json()
        if qrcode_data['data']['code'] == 0:
            v1.set('扫码成功')
            session2.get(qrcode_data['data']['url'], headers=headers2)
            break
        else:
            v1.set(qrcode_data['data']['message'])
        sleep(1)
        root.update()
    session2.cookies.save()
    with open(temp_cookie, 'r', encoding='utf-8') as f:
        bzcookie = f.read()
    bili_jct = findall(r'bili_jct=(.*?);', bzcookie)[0]


def bz_login(session1):
    """登录b站"""
    global code_pic
    session1.cookies = LWPCookieJar(filename=temp_cookie)
    status = is_login(session1)
    if not status:
        scan_code(session1)
    verification(session1)


def verification(session1):
    """验证cookies是否有效"""
    url = 'https://api.bilibili.com/x/web-interface/nav'
    resp1 = session1.get(url=url, headers=headers2).json()
    global tk_image
    if resp1['data']['isLogin']:
        face_url = resp1['data']['face']
        image_bytes = requests.get(face_url).content
        data_stream = BytesIO(image_bytes)
        pil_image = Image.open(data_stream)
        pil_image_change = pil_image.resize((200, 200), resample=Image.BICUBIC, box=None, reducing_gap=None)
        tk_image = ImageTk.PhotoImage(pil_image_change)
        status = "cookie有效！登录成功！"
    else:
        thread_it(bz_login)
        status = 'cookie无效！重新登录'
    label_ver = Label(root, image=tk_image)
    label_ver.grid(row=1, column=1, rowspan=8, columnspan=1, sticky='n')
    v1.set(status)


def thread_it(func, *args):
    thread = Thread(target=func, args=args, daemon=True)
    thread.start()


def cancel_login():
    """注销登录"""
    msg1 = messagebox.askyesno(title="提示", message="注销后cookie将失效，是否注销登录？")
    if msg1:
        url3 = 'https://passport.bilibili.com/login/exit/v2'
        data3 = {'biliCSRF': f'{bili_jct}'}
        session1.post(url=url3, headers=headers2, data=data3).json()
        verification(session1)


def get_cookies():
    """从./res/cookie/bzcookies.txt获取cookies字典"""
    with open(temp_cookie, "r", encoding="utf-8") as f:
        cookie_data = f.read()
    f.close()
    if cookie_data == '':
        messagebox.showwarning("尚未登录！")
    cookie_dict = {}
    for line in cookie_data.split("\n"):
        if line.find("Set-Cookie3") != -1:
            line = line.split(":")[1]
            for kv in line.split(";"):
                lst = list(kv.split("="))
                if len(lst) == 2:
                    k = lst[0]
                    v = lst[1]
                    cookie_dict[k.strip()] = v.strip("\"")
    return cookie_dict


def cookies_app():
    """二维码登录窗口主程序"""
    global root, v1, session1
    root = Tk()
    v1 = StringVar()
    if not path.exists(temp_cookie):
        with open(temp_cookie, 'w', encoding='utf-8') as f:
            f.write("")
    with open(temp_cookie, 'r', encoding='utf-8') as f:
        bzcookie = f.read()
    requests.packages.urllib3.disable_warnings()
    session1 = requests.session()
    root.geometry('330x230')
    root.title("cookie")
    thread_it(bz_login(session1))
    btn1 = Button(root, width=10, text='注销登录', command=cancel_login)
    btn1.grid(row=3, column=2)
    label_ver2 = Label(root, textvariable=v1)
    label_ver2.grid(row=9, column=1, rowspan=8, columnspan=1, sticky='n')
    root.mainloop()
