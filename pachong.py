"""爬虫部分"""
import time
from PySide6.QtWidgets import QMessageBox
from cookies import *


def show_waring(info):
    """弹出警告框"""
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(info)
    msg_box.setWindowTitle("警告消息框")
    msg_box.exec()


def fetch_comments(video_bv, cookies_dict, max_pages=10):
    """爬取评论"""
    # 构造请求头
    headers = {
        'authority': 'api.bilibili.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'origin': 'https://www.bilibili.com',
        'referer': f'https://www.bilibili.com/video/{video_bv}/?spm_id_from=333.337.search-card.all.click&vd_source=69a50ad969074af9e79ad13b34b1a548',
        'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
    }
    # 判断cookies的输入方式，以构造不同形式的请求头
    if isinstance(cookies_dict, dict):  # 如果是登陆方式获取
        try:
            headers['cookie'] = ";".join([f"{name}={value}" for name, value in cookies_dict.items()])
            headers['SESSDATA'] = cookies_dict["SESSDATA"]
            headers['csrf'] = cookies_dict["bili_jct"]
        except KeyError:
            show_waring("cookies错误！")
            return []
    elif isinstance(cookies_dict, str):  # 如果是手动输入
        headers['cookie'] = cookies_dict
    comments = []
    last_count = 0
    for page in range(1, max_pages + 1):
        # b站评论的懒加载api
        url = f'https://api.bilibili.com/x/v2/reply/main?next={page}&type=1&oid={video_bv}&mode=3'
        try:
            response = requests.get(url, headers=headers, timeout=20)
            # 检查响应状态码是否为200，即成功
            if response.status_code == 200:
                data = response.json()
                # 进一步判断是否正常返回数据
                if data['code'] == -352 or data['code'] == 0 and data['data']['cursor']['pagination_reply'] is None:
                    show_waring("cookies错误!请手动设置cookies或重新登陆！")
                    return []
                if data['data']['replies'] is None:
                    break
                if data and 'replies' in data['data']:
                    for comment in data['data']['replies']:
                        comment_info = {
                            '用户昵称': comment['member']['uname'],
                            '评论内容': comment['content']['message'],
                            '被回复用户': '',
                            '评论层级': '一级评论',
                            '性别': comment['member']['sex'],
                            '用户当前等级': comment['member']['level_info']['current_level'],
                            '点赞数量': comment['like'],
                            '回复时间': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(comment['ctime']))
                        }
                        comments.append(comment_info)
                if last_count == len(comments):
                    break
                last_count = len(comments)
            else:
                break
        except requests.RequestException as e:
            show_waring(f"请求出错: {e}")
            break
        response.close()
        time.sleep(0.1)  # 控制请求频率
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText("爬取完成！")
    msg_box.setWindowTitle("信息消息框")
    msg_box.exec()
    return comments


def purify(comment):
    """去除评论中的表情文本，以免影响分词和词云图结果"""
    s = ''
    stack = []
    i = 0
    cnt = 0
    while i < len(comment):
        if comment[i] == '[':
            stack.append(i-cnt)
        elif comment[i] == ']':
            s = s[:stack[-1]]
            cnt += i-cnt-stack[-1]+1
            stack.pop()
        if comment[i] != ']':
            s += comment[i]
        i += 1
    return s


def save_comment_content_to_txt(comments, comment_content_txt_name="commentContent.txt"):
    """保存评论文本为txt文件以便后续处理和查看"""
    lst = []
    with open(f'./res/result/{comment_content_txt_name}', mode='w', encoding='utf-8') as f:
        for comment in comments:
            lst.append(purify(comment['评论内容'])+'\n')
        f.writelines(lst)
    f.close()
    return comment_content_txt_name
