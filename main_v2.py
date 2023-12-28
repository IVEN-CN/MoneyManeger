"""version:v2.5"""

from handeler import *  # 引入自定义的文件
from tkinter import *  # 引入三方模块


def main():
    # 创建第一个主窗口
    win1 = Tk()  # 建立窗口
    win1.title('资金管理器')  # 窗口的名字
    win1.minsize(400, 150)  # 窗口最小大小

    for i in range(3):  # 使内部控件可以随着父级窗口大小改变而改变，3是行数，采用的表格GUI排布（grid）
        win1.grid_rowconfigure(index=i, weight=1)
    for k in range(5):  # 5是列数，有5列
        win1.grid_columnconfigure(index=k, weight=1)
    win1.grid_rowconfigure(index=2, weight=0)
    win1.grid_rowconfigure(index=0, weight=0)

    label1 = Label(win1,
                   text='选择使用的服务',
                   font=('楷体', 15, 'bold'))  # 建立第一个文本标签
    label1.grid(row=0, column=0, columnspan=5)  # 位置的布局左上角是0列，0行

    # 创建bt1按钮控件
    bt1 = Button(win1,  # 按钮所在的窗口，即父级
                 text='收入',  # 按钮的文字
                 font=('宋体', '12', 'normal'),  # 按钮文字的字体
                 command=inwin)  # 按钮指向的方法，这个方法在handeler包里
    bt1.grid(row=1, column=0, padx=2, pady=10, sticky=W + S + E + N)  # 将控件放入窗口，sticky的参数为了让控件随着窗口大小变化而变化
    # padx，pady是控件向x和y轴方向扩张的多少

    bt2 = Button(win1, text='支出',
                 font=('宋体', '12', 'normal'),
                 command=outwin)
    bt2.grid(row=1, column=1, padx=2, pady=10, sticky=W + S + E + N)

    bt3 = Button(win1, text='保存',
                 font=('宋体', '12', 'normal'),
                 command=savewin)
    bt3.grid(row=1, column=3, padx=2, pady=10, sticky=W + S + E + N)

    bt4 = Button(win1,
                 text='重置',
                 font=('宋体', '12', 'normal'),
                 command=initwin)
    bt4.grid(row=1, column=4, padx=2, pady=10, sticky=W + S + E + N)

    bt5 = Button(win1,
                 text='欠款',
                 font=('宋体', '12', 'normal'),
                 command=lenwin)
    bt5.grid(row=1, column=2, padx=2, pady=10, sticky=W + S + E + N)

    bt0 = Button(win1,
                 text='退出',
                 width=5,
                 height=2,
                 command=win1.destroy)
    bt0.grid(row=2, column=1, padx=10, pady=10, sticky=W + S + E + N, columnspan=3)

    win1.mainloop()  # 主窗口的事件主循环


if __name__ == '__main__':
    main()
