import numpy as np
import matplotlib.pyplot as plt

# 1. 在 [0, 2*pi] 之间生成 100 个等间距的点
x = np.linspace(0, 2 * np.pi, 100)

# 2. 计算对应的 y 值
y = np.sin(x)  # 已修复：补充了缺失的括号

# 3. 创建绘图
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='y = sin(x)', color='blue', linewidth=2)

# 4. 添加图像装饰
plt.title('Visualization Test: Sine Wave', fontsize=14)
plt.xlabel('x (radians)', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.text(1, 0.5, r'$y = \sin(x)$', fontsize=15, color='red')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# 5. 显示图像
print("正在生成图像，请查看弹出的窗口...")
plt.show()