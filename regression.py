# regression.py

import numpy as np


def func(x):
    import numpy as np

    def func(x):
        # 线性部分: y = kx + D
        k = 0.4516893073665399
        D = 6.0186559415094205
        y_linear = k * x + D

        # 周期性部分: y = A*sin(Bx + C)
        A = -7.822343323847942
        B = 0.49091912642959035
        C = -14.797127473342602
        y_sin = A * np.sin(B * x + C)

        # 最终函数是线性部分与周期性部分的和
        y = y_linear + y_sin
        return y


