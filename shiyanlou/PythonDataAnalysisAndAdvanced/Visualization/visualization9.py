# -*- coding: UTF-8 -*-
#visualization9－Pandas绘图

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

s =  Series(np.random.randn(10).cumsum(), index=np.arange(0,100,10))
s.plot()
plt.show()

df = pd.DataFrame(np.random.rand(5,4), columns=['A','B','C','D'])
df.boxplot()
plt.show()