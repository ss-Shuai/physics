import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.cm as cm
from scipy import special
from math import factorial

# 定义函数radial_wave_function，计算球谐函数的值
def radial_wave_function(n, l, r):
 # 计算系数
 coeff = np.sqrt((2/n) ** 3 * (factorial(n - l - 1) / (2 * n * factorial(n + l)))) * np.exp(-r/n)
 # 返回计算结果
 return coeff * (2 * l / n) ** l * special.assoc_laguerre(2*r/n, n-l-1, 2*l+1)

# 定义函数plot_radial_wave_function，绘制函数图像
def plot_radial_wave_function(n_min, n_max, l_min, l_max, r_min, r_max, num_points):
   # 创建图像
    fig = plt.figure()
    ax = fig.add_subplot(111)
   
    # 循环绘制函数图像
    for n in range(n_min, n_max+1):
        for l in range(l_min, l_max+1):
            if l >= n: break
            r = np.linspace(r_min, r_max, num_points)
            psi = radial_wave_function(n, l, r)
            im = ax.plot(r, np.abs(psi), label=f'n={n}, l={l}')
   
    # 设置坐标轴标签
    ax.set_xlabel('r/a0')
    ax.set_ylabel('|Ψ|')
   
    # 设置图例
    ax.legend()
   
    # 显示图形
    plt.show()

  # 调用函数
plot_radial_wave_function(1, 4, 0, 3, 0, 10, 100)