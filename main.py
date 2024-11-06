"""主程序，主窗口"""
import numpy as np
import wordcloud
from ui_main import Ui_MainWindow
from wordsCount import *
from pachong import *
from delete import *
from cookies import *

# B站视频的bv号，爬虫的核心变量
video_bv = ''


class MainWindow(QMainWindow):
    """主窗口类"""
    def __init__(self):
        """初始化"""
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        # 初始化各个按钮的回调函数
        self.ui.generate_wordcloud_pushButton.clicked.connect(self.handle)
        self.ui.pachong_pushButton.clicked.connect(self.save_pachong)
        self.ui.del_checkBox.stateChanged.connect(self.del_app)
        self.ui.login_pushButton.clicked.connect(self.login)
        self.ui.cookies_pushButton.clicked.connect(self.show_get_cookies)

    def login(self):
        """登录以获取cookies"""
        cookies_app()

    def show_get_cookies(self):
        """显示如何获取cookies的图片教程"""
        img_cookies = Image.open("./res/qt/img/show_get_cookies.png")
        img_cookies.show()

    def save_pachong(self):
        """保存爬虫的结果"""
        cookies_input = self.ui.cookies_lineEdit.text()
        video_bv = self.ui.video_bv_lineEdit.text()
        max_pages = 10 if self.ui.max_pages_lineEdit.text() == '' else int(self.ui.max_pages_lineEdit.text())
        if video_bv != '':
            # 调用pachong.py中的fetch_comments函数获取评论区文本
            if cookies_input == '':  # 以登录方式获取cookies
                comments = fetch_comments(video_bv, get_cookies(), max_pages=max_pages)
            else:  # 以手动输入方式获取cookies
                comments = fetch_comments(video_bv, cookies_input, max_pages=max_pages)
            # 如果comments不为空，则保存结果以便读取处理，保存词和词频的字典words_count.json，词、词性和词频的字典words.json 到./res/result
            if comments:
                comment_content_txt_name = save_comment_content_to_txt(comments)
                words_list = words_count(comment_content_txt_name)
                save_words_count_to_json(words_list)
                save_words_to_json()

    def del_app(self):
        """筛选界面主窗口"""
        if mainw.ui.del_checkBox.checkState() == Qt.Checked:
            # 在窗口开启的时候进行初始化，防止调用上次的数据
            del_mainw.cx = del_mainw.ganerate_table()
            if del_mainw.cx:
                del_mainw.cx_others = del_mainw.cx - set(del_mainw.cx_list)
                del_mainw.choose_dict = {}
                for cx in del_mainw.cx:
                    del_mainw.choose_dict[cx] = False
                del_mainw.show()
        else:
            del_mainw.close()

    def handle(self):
        """获取相关参数设置并生成词云图"""
        wordcloud_name = "wordcloud.png" if self.ui.wordcloud_name_lineEdit.text() == '' else self.ui.wordcloud_name_lineEdit.text()+".png"
        wordcloud_path = self.ui.wordcloud_path_lineEdit.text()
        mask_pic_path = "./res/mask_pic/" if self.ui.mask_pic_path_lineEdit.text() == '' else self.ui.mask_pic_path_lineEdit.text()
        mask_pic_name = '1.png' if self.ui.mask_pic_name_lineEdit.text() == '' else self.ui.mask_pic_name_lineEdit.text()
        background_color = 'white' if self.ui.background_color_lineEdit.text() == '' else self.ui.background_color_lineEdit.text()
        width = 800 if self.ui.width_lineEdit.text() == '' else int(self.ui.width_lineEdit.text())
        height = 600 if self.ui.height_lineEdit.text() == '' else int(self.ui.height_lineEdit.text())
        font_path = './res/font/simfang.ttf' if self.ui.font_path_lineEdit.text() == '' else self.ui.font_path_lineEdit.text()
        generate_wordcloud(wordcloud_name=wordcloud_name,
                           wordcloud_path=wordcloud_path,
                           mask_pic_path=mask_pic_path,
                           mask_pic_name=mask_pic_name,
                           background_color=background_color,
                           width=width,
                           height=height,
                           font_path=font_path)


def generate_wordcloud(words_count_json_path='./res/result/',
                       words_count_json_name="words_count.json",
                       wordcloud_name="wordcloud.png",
                       wordcloud_path='',
                       mask_pic_path="./res/mask_pic/",
                       mask_pic_name='1.png',
                       background_color='white',
                       width=800,
                       height=600,
                       font_path='./res/font/simfang.ttf'):
    """生成词云图"""
    # 异常处理，尝试打开words_count.json读取数据
    try:
        with open(words_count_json_path + words_count_json_name, "r", encoding='utf-8') as f:
            words_dict = json.load(f)
        f.close()
    except FileNotFoundError:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(f"未找到words_count.json文件！请先爬取评论！")
        msg_box.setWindowTitle("警告消息框")
        msg_box.exec()
        return
    w = wordcloud.WordCloud(background_color=background_color,
                            width=width,
                            height=height,
                            font_path=font_path,
                            mask=np.array(Image.open(mask_pic_path + mask_pic_name))).fit_words(words_dict)
    # 词云图生成结果展示
    img = w.to_image()
    img.show()
    # 保存词云图生成结果
    w.to_file(wordcloud_path + wordcloud_name)


if __name__ == '__main__':
    """主程序"""
    # 创建app实例，主窗口实例并显示，筛选窗口实例
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    del_mainw = DelMainWindow()
    app.exec()
