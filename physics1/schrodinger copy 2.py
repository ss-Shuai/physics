import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.cm as cm
import mpl_toolkits.mplot3d.axes3d as axes3d

from scipy import special
from math import factorial


# 定义函数radial_wave_function，计算径向函数的值
def radial_wave_function(n, l, r, theta):
   # 计算系数
   coeff = np.sqrt((2/n) ** 3 * (factorial(n - l - 1) / (2 * n * factorial(n + l)))) * np.exp(-r/n)
   # 计算 legendre 多项式
   legendre_polynomial = special.eval_legendre(l, np.cos(theta))
   # 计算 laguerre 多项式
   laguerre_polynomial = special.eval_laguerre(n - l - 1, 2*r/n)
   # 返回计算结果
   return coeff * legendre_polynomial * laguerre_polynomial


def plot_hydrogen(n0, l0, m0):
    # 计算r,theta和phi的网格
    r_min = 0
    r_max = 4
    r0 = np.linspace(r_min, r_max, 40)
    theta, phi = np.linspace(0, np.pi, 50), np.linspace(0, 1*np.pi, 40)
    r, THETA, PHI = np.meshgrid(r0, theta, phi)

    # 计算函数值
    psi = radial_wave_function(n0, l0, r, THETA)*special.sph_harm(m0, l0, PHI, THETA).real
    #psi = r *special.sph_harm(m0, l0, PHI, THETA).real
    # 计算，并计算R
    intensity_values = (psi)**2

    #m=2, l=3
    X = r * np.sin(THETA) * np.cos(PHI)
    Y = r * np.sin(THETA) * np.sin(PHI)
    Z = r * np.cos(THETA)

    # 设置颜色映射
    #color_map = plt.cm.get_cmap('coolwarm', 100)

    # 创建3D图
    fig = plt.figure()

    ax = fig.add_subplot(1,1,1, projection='3d')
  
    scatter = ax.scatter(X, Y, Z, c=intensity_values, cmap='viridis_r', marker='o', alpha= intensity_values/np.max(intensity_values))

    # 添加颜色条
    cbar = plt.colorbar(scatter)
    cbar.set_label('Intensity')


    max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
    mid_x = (X.max()+X.min()) * 0.5
    mid_y = (Y.max()+Y.min()) * 0.5
    mid_z = (Z.max()+Z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # 设置坐标轴标签
    ax.set_xlabel('X', fontsize=14)  # 设置标签大小
    ax.set_ylabel('Y', fontsize=14)
    ax.set_zlabel('Z', fontsize=14)
    ax.set_title("Hydrogen wavefunction n={}, l={}, m={}".format(n0, l0, m0), fontsize=16)

    # 设置视角
    ax.view_init(elev=10,azim=30)  # 调节

    # 设置视角
    ax.view_init(elev=10,azim=30)  # 调节视角，elev指向上(z方向)旋转的角度，azim指xy平面内旋转的角度

    # 显示图片
    plt.show()
    print("hydrogen wavefuvtion n=%d, l=%d, m=%d.jpg" % (n0, l0, m0))
    #plt.savefig("spherical harmonics m=%d l=%d.jpg",m0,l0)

# 测试函数
plot_hydrogen(4,3,2)