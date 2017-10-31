# -*- coding: UTF-8 -*-
#UnderstandingData7－异常值检测

from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("test_file.csv", header=0)

Total_Population = data["Total Population"]

plt.boxplot(Total_Population)

plt.show()