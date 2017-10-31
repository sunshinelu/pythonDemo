# -*- coding: UTF-8 -*-
#visualization11－其他绘图工具

import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

# sin曲线

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

p = figure(title="Shiyanlou Bokeh Example")
p.circle(x, y, legend="sin(x)")
p.circle(x, 2 * y, legend="2*sin(x)", color="orange")
p.circle(x, 3 * y, legend="3*sin(x)", color="green")

show(p)