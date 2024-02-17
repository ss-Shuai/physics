import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.cm as cm
import mpl_toolkits.mplot3d.axes3d as axes3d

from scipy import special
from math import factorial


# 定义函数radial_wave_function，计算径向函数的值
def radial_wave_function(n, l, r):
 # 计算系数
 coeff = np.sqrt((2/n) ** 3 * (factorial(n - l - 1) / (2 * n * factorial(n + l)))) * np.exp(-r/n)
 # 返回计算结果
 return coeff * (2 * l / n) ** l * special.assoc_laguerre(2*r/n, n-l-1, 2*l+1)


def plot_hydrogen(n0, l0, m0):
   # 计算r,theta和phi的网格
    r = np.linspace(0, 10, 100)
    
    theta, phi = np.linspace(0, np.pi, 100), np.linspace(0, 2*np.pi, 100)
    THETA, PHI = np.meshgrid(theta, phi)
    #help(special.sph_harm)

    # 计算函数值
    psi = radial_wave_function(n0, l0, r)*special.sph_harm(m0, l0, PHI, THETA).real
    # 计算，并计算R
    R = (psi)**2

    #m=2, l=3
    X = R * np.sin(THETA) * np.cos(PHI)
    Y = R * np.sin(THETA) * np.sin(PHI)
    Z = R * np.cos(THETA)

    # 设置颜色映射
    color_map = plt.cm.get_cmap('coolwarm', 10)

    # 创建3D图
    fig = plt.figure()

    ax = fig.add_subplot(1,1,1, projection='3d')
    plot = ax.plot_surface(
        X, Y, Z, rstride=1, cstride=1, cmap=color_map,
        linewidth=0, antialiased=False, alpha=0.5)

    # 添加颜色条
    bar = plt.colorbar(plot, ax=ax)

    # below are codes copied from stackoverflow, to make the scaling correct
    # 设置坐标轴范围
    max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
    mid_x = (X.max()+X.min()) * 0.5
    mid_y = (Y.max()+Y.min()) * 0.5
    mid_z = (Z.max()+Z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # 设置坐标轴标签
    ax.set_xlabel('X', rotation=0)  # 设置标签角度
    ax.set_ylabel('Y', rotation=0)
    ax.set_zlabel('Z', rotation=0)
    ax.set_title("hydrogen wavefuvtion n=%d, l=%d, m=%d.jpg" % (n0, l0, m0))

    # 设置视角
    ax.view_init(elev=10,azim=30)  # 调节视角，elev指向上(z方向)旋转的角度，azim指xy平面内旋转的角度

    # 显示图片
    plt.show()
    print("hydrogen wavefuvtion n=%d,l=%d, m=%d.jpg" % (n0, l0, m0))
    #plt.savefig("spherical harmonics m=%d l=%d.jpg",m0,l0)

# 测试函数
plot_hydrogen(1,0,0)