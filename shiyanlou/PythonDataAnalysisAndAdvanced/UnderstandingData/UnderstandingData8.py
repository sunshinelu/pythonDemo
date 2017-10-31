# -*- coding: UTF-8 -*-
#UnderstandingData8－离群点标记并导出


from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("test_file.csv", header=0)

Total_Population = data["Total Population"]

P = plt.boxplot(Total_Population)

outlier = P['fliers'][0].get_ydata()

print(outlier)

data.boxplot()
plt.show()