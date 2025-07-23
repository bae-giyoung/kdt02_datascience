import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

x = np.linspace(0, 10, 100)
print(x[99])

# 같은 셀에서는 겹쳐서 그림
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()