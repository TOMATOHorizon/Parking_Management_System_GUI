import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

class DataChart:
    def __init__(self):

        mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体

        # 读取 CSV 文件
        df = pd.read_csv('DataSet/ScoreAnalysis_Dataset.csv', encoding='utf-8')

        # 指定列名称和权重列名称
        col_name = '分数最低名称'
        weight_name = '分数最低数值'

        # 计算每一类别的权重总和
        grouped = df.groupby(col_name).sum(numeric_only=True)

        # 创建 2x2 子图矩阵
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))

        # 绘制饼状图
        axs[0, 0].pie(grouped[weight_name], labels=grouped.index, autopct='%1.1f%%')
        axs[0, 0].set_title('饼状图')

        # 绘制簇状图
        sns.barplot(x=grouped.index, y=grouped[weight_name], ax=axs[0, 1], data=grouped.reset_index())
        axs[0, 1].set_title('簇状图')

        # 绘制热力图
        heatmap_data = np.random.rand(10, 10)
        sns.heatmap(heatmap_data, ax=axs[1, 0])
        axs[1, 0].set_title('热力图')

        # 绘制折线图
        line_data = grouped.reset_index()
        sns.lineplot(x=line_data.index, y=grouped[weight_name], data=line_data, ax=axs[1, 1])
        axs[1, 1].set_title('折线图')

        # 保存图像
        plt.savefig('DataAndAnalysis_Visualization/DataAndAnalysis_Visualizations.png')

        # 显示图像
        plt.show()

datachart = DataChart()