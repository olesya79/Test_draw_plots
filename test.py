import os

import matplotlib.pyplot as plt
import pandas as pd

url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
df = pd.read_json(url)
print(df)


# Этот класс используется для создания графиков
class Plot:
    def __init__(self, datafreim, link):
        self.datafreim = datafreim
        self.link = link

    def drow(self):
        plot_1 = df.plot(kind='hist', title='График')
        return plt.show()

url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
df = pd.read_json(url)
plots = Plot(link=url, datafreim=df)
plots.drow()


# Эта функция используется для создания и сохранения графиков
def draw_plots():
    link = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
    reads = pd.read_json(link)  # читает json file переданный как параметр pandas dataframe
    draws = df.plot()  # создаёт график для сравнения различных столбцов
    fig = draws.figure
    saves = fig.savefig('C:/test_prodect/plots/file.png')  # сохраняет график в директорию
    returns = os.path.abspath('*')  # возвращает пути к графикам
    return reads, draws, saves, returns


print(draw_plots())
