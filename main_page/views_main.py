from django.shortcuts import render

# Create your views here.
import numpy as np
from django.http import JsonResponse
#先预设每个指标最好情况能达到的值
best_data = []

# #负向指标正向化，对data矩阵中第num列的指标正向化
# def norm_toward_big(data,num):
#     data[num] =  data[num]*(-1) + data[num].max()
#     return data

#通过FAHP确定指标权重
def confirm_the_weight():
    #先列出专家判断矩阵,n个指标矩阵就有n行、n列,每一个元素是一个三元元组(模糊数)
    dataset = []
    #随后确定各指标权重
    '''
        dataset: 专家判断矩阵，n*n*3，n表示指标数
    '''
    row_sum = []
    s_row = []
    f_w = []  # 模糊权重
    d_w = []  # 去模糊权重
    # 一致性检测指标
    inc_rat = np.array([0, 0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51, 1.48, 1.56, 1.57, 1.59])
    # 模糊判断矩阵转为清晰判断矩阵
    X = [(item[0] + 4 * item[1] + item[2]) / 6 for i in range(0, len(dataset)) for item in dataset[i]]  # 三角数转为模糊数
    X = np.asarray(X)  # 列表转数组
    X = np.reshape(X, (len(dataset), len(dataset)))  # 转为n*n矩阵

    # S4. 计算每个准则的模糊比较值的几何平均值r_i(公式4)
    for i in range(0, len(dataset)):
        a, b, c = 1, 1, 1
        for j in range(0, len(dataset[i])):
            d, e, f = dataset[i][j]
            # 计算公式(4)的括号内部分: r_s = \prod_{j=1}^n d_ij
            a, b, c = a * d, b * e, c * f
        row_sum.append((a, b, c))
    L, M, U = 0, 0, 0
    for i in range(0, len(row_sum)):
        a, b, c = row_sum[i]
        # 计算公式(4)的括号外部分: s_r = (r_s)^(1/n)
        a, b, c = a ** (1 / len(dataset)), b ** (1 / len(dataset)), c ** (1 / len(dataset))
        s_row.append((a, b, c))
        # 计算公式(5)中⨁运算部分：R5 = r1⨁r2⨁...⨁rn
        L = L + a
        M = M + b
        U = U + c

    for i in range(0, len(s_row)):
        a, b, c = s_row[i]
        # 计算公式公式(5)中⨂运算部分：wi = ri⨂R5
        a, b, c = a * (U ** -1), b * (M ** -1), c * (L ** -1)
        # 模糊权重
        f_w.append((a, b, c))
        # 计算公式(6):去模糊权重
        d_w.append((a + b + c) / 3)
    # 计算公式(7): 归一化权重
    n_w = [round(item / sum(d_w),3) for item in d_w]
    # 计算特征根向量
    vector = np.sum(X * n_w, axis=1) / n_w
    # 获得平均特征根
    lamb_max = np.mean(vector)
    # 计算一致性指标
    cons_ind = (lamb_max - X.shape[1]) / (X.shape[1] - 1)
    # 一致性判断
    rc = cons_ind / inc_rat[X.shape[1]]
    if rc<0.1:
        print("yyyyyyyyyyyyes!!!!!")
    return n_w


def evaluate_security_of_web_site(request):
    receive_data = request.POST.get()

    finished_data = []
    final_score = 0
    weight = confirm_the_weight()
    for i in range(len(best_data)):
        if best_data[i]<finished_data[i]:
            final_score += (best_data[i]/finished_data[i])*weight[i]
        else:
            final_score += (finished_data[i]/best_data[i])*weight[i]
    return JsonResponse(final_score)