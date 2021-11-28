import sys
print(sys.executable)
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import jieba.analyse as analyse
import imageio
from os import path
import chardet   #需要导入这个模块，检测编码格式

def draw_wordcloud():
    text = open('C://Users//dell//female figure.txt', 'rb').read()
    cut_text = " ".join(jieba.cut(text))
    d= path.dirname('C://Users//dell')
    # color_mask = imageio.imread('C://Users//dell//背景图男.jpg')
    cloud=WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path = 'simhei.ttf',
        # 设置背景色
        background_color='white',
        # 词云形状
        # mask=color_mask ,
        # 允许最大词汇
        max_words=3000,
        # 最大号字体
        max_font_size=100,
        # 有多少种情况
        random_state=20
    )
    word_cloud=cloud.generate(cut_text)
    word_cloud.to_file("C://Users//dell//20-30岁以上学历本科或专科的女性.jpg")
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('20-30岁学历本科或专科的女性对于手机银行APP的选择情况')
    plt.show()
draw_wordcloud()


