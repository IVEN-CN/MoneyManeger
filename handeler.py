from tkinter import *
import csv
from tkinter.messagebox import *
import time


def inwin():
    win2 = Tk()
    win2.title('资金收入记录')

    def _quit():
        win2.quit()
        win2.destroy()

    def inedit():
        ask = askyesno(title='注意', message='是否继续')
        if ask:
            with open('in.csv', 'a', encoding='gbk', newline='') as f:
                file = csv.writer(f)
                file.writerow([ent_time.get(), ent_money.get(), ent_reason.get()])
            showinfo(title='注意', message='进程结束')
            _quit()  # 关闭原来有数据的窗口
            inwin()  # 重新建立一个空白的窗口
        else:
            showinfo(title='注意', message='返回')
        # inwin()

    for i in range(3):  # 使内部控件可以随着父级窗口大小改变而改变
        win2.grid_rowconfigure(index=i, weight=1)
    for k in range(3):
        win2.grid_columnconfigure(index=k, weight=1)
    win2.grid_rowconfigure(index=3, weight=0)

    win2.minsize(width=300, height=150)  # 设置窗口最小的大小

    label_time = Label(win2, text='收入时间', font=('楷体', 15, 'bold'))
    label_time.grid(row=0, column=0, sticky=W + S + E + N)

    ent_time = Entry(win2)
    ent_time.grid(row=0, column=1, sticky=W + S + E + N, columnspan=2)

    label_money = Label(win2, text='收入金额', font=('楷体', 15, 'bold'))
    label_money.grid(row=1, column=0, sticky=W + S + E + N)

    ent_money = Entry(win2)
    ent_money.grid(row=1, column=1, sticky=W + S + E + N, columnspan=2)

    label_reason = Label(win2, text='收入来源/原因', font=('楷体', 15, 'bold'))
    label_reason.grid(row=2, column=0, sticky=W + S + E + N)

    ent_reason = Entry(win2)
    ent_reason.grid(row=2, column=1, sticky=W + S + E + N, columnspan=2)

    bt = Button(win2, text='写入', command=inedit)
    bt.grid(row=3, column=1, sticky=W + S + E + N)

    bt_q = Button(win2, text='返回', command=_quit)
    bt_q.grid(row=3, column=2, sticky=W + S + E + N)

    win2.mainloop()


def outwin():
    win3 = Tk()
    win3.title('资金收入记录')

    def _quit():
        win3.quit()
        win3.destroy()

    def outedit():
        ask = askyesno(title='注意', message='是否继续')  # askyesno是提示对话框
        if ask:  # aks == True的简写
            with open('out.csv', 'a', encoding='gbk', newline='') as f:
                file = csv.writer(f)
                file.writerow([ent_time.get(), ent_money.get(), ent_reason.get(), v.get()])
            showinfo(title='注意', message='进程结束')
            _quit()  # 关闭原来有数据的窗口
            outwin()  # 重新建立一个空白的窗口
        else:
            showinfo(title='注意', message='返回')  # showinfo是一个警告窗口
        # win3.quit()
        # outwin()

    for i in range(5):  # 使内部控件可以随着父级窗口大小改变而改变
        win3.grid_rowconfigure(index=i, weight=1)
    for k in range(5):
        win3.grid_columnconfigure(index=k, weight=1)
    win3.grid_rowconfigure(index=5, weight=0)

    win3.minsize(width=300, height=150)  # 设置窗口最小的大小

    label_time = Label(win3, text='消费时间', font=('楷体', 15, 'bold'))
    label_time.grid(row=0, column=0, sticky=W + S + E + N)

    ent_time = Entry(win3)  # entry是输入框控件，ent_time是传入值的变量
    ent_time.grid(row=0, column=1, sticky=W + S + E + N, columnspan=4)

    label_money = Label(win3, text='消费金额', font=('楷体', 15, 'bold'))
    label_money.grid(row=1, column=0, sticky=W + S + E + N)

    ent_money = Entry(win3)
    ent_money.grid(row=1, column=1, sticky=W + S + E + N, columnspan=4)

    label_reason = Label(win3, text='消费原因', font=('楷体', 15, 'bold'))
    label_reason.grid(row=2, column=0, sticky=W + S + E + N)

    ent_reason = Entry(win3)
    ent_reason.grid(row=2, column=1, sticky=W + S + E + N, columnspan=4)

    bt = Button(win3, text='写入', command=outedit)
    bt.grid(row=5, column=1, sticky=W + S + E + N, columnspan=2)
    # 回车也可以使此按钮生效
    win3.bind('<Return>', lambda event: outedit())

    bt_q = Button(win3, text='返回', command=_quit)
    bt_q.grid(row=5, column=3, sticky=W + S + E + N)

    label_type = Label(win3, text='选择消费类型', font=('楷体', 15, 'bold'))
    label_type.grid(row=3, column=1, sticky=W + S + E + N, columnspan=2)

    v = StringVar(win3)  # 字符串变量
    v.set('食品')  # 多选菜单的默认值
    # OptionMenu只是一个对象
    # 参数1是在哪个窗口显示
    # 参数2是用于保存的变量，这里是v
    # 参数3及之后的是菜单的可选项 ，也可以使用*号操作，比如,效果是一样的
    #      ↓是构建对象  ↓参数1 ↓参数2 ↓参数3 ↓参数4 ↓参数5 。。。
    # om = OptionMenu(win3, v, '食品', '出行', '购物', '还款', '住宿')
    menu_items = ['出行', '购物', '还款', '住宿', '生活用品', '其他']  # ↓ *号操作是对数组或对象取地址
    om = OptionMenu(win3, v, '食品', *menu_items)
    om.grid(row=4, column=1, sticky=W + S + E + N, columnspan=2)

    win3.mainloop()


def savewin():
    swin = Tk()
    swin.title('文件管理')
    swin.minsize(width=300, height=100)

    def save_csv_out():
        name = 'out.csv'
        tpe = 'out'
        ask = askyesno(title='注意', message='是否继续')
        if ask:
            time.gmtime()
            new_name = time.strftime(tpe + '%Y-%m-%d.csv')
            with open(name, 'r', encoding='gbk') as f1:
                b1 = f1.read()
            with open(new_name, 'w', encoding='gbk') as f2:
                f2.write(b1)
            showinfo(title='注意', message='进程结束')
        else:
            showinfo(title='注意', message='返回')
        return 'done'

    def save_csv_in():
        name = 'in.csv'
        tpe = 'in'
        ask = askyesno(title='注意', message='是否继续')
        if ask:
            time.gmtime()
            new_name = time.strftime(tpe + '%Y-%m-%d.csv')
            with open(name, 'r', encoding='gbk') as f1:
                b1 = f1.read()
            with open(new_name, 'w', encoding='gbk') as f2:
                f2.write(b1)
            showinfo(title='注意', message='进程结束')
        else:
            showinfo(title='注意', message='返回')
        return 'done'

    def _quit():
        swin.quit()
        swin.destroy()

    for i in range(3):  # 使内部控件可以随着父级窗口大小改变而改变
        swin.grid_rowconfigure(index=i, weight=1)
    for k in range(2):
        swin.grid_columnconfigure(index=k, weight=1)
    swin.grid_rowconfigure(index=2, weight=0)

    slabel = Label(swin, text='选择保存的文件类型', font=('楷体', 15, 'bold'))  # 建立第一个文本
    slabel.grid(row=0, column=0, columnspan=2)  # 位置的布局

    # save_csv() 调用函数
    # save_csv 指向函数地址
    sbt1 = Button(swin, text='收入', command=save_csv_in)
    sbt1.grid(row=1, column=0, sticky=W + S + E + N)

    sbt2 = Button(swin, text='支出', command=save_csv_out)
    sbt2.grid(row=1, column=1, sticky=W + S + E + N)

    bt_q = Button(swin, text='返回', command=_quit)
    bt_q.grid(row=3, column=2, sticky=W + S + E + N)

    swin.mainloop()


def initwin():
    win = Tk()
    win.title('重置窗口')
    win.minsize(width=300, height=100)

    def init_csv_out():  # 重置文件函数
        name = 'out.csv'
        list1 = ['消费时间', '消费金额', '消费项目', '消费类型']
        ask = askyesno(title='注意', message='是否继续')
        if ask:
            with open(name, 'w', encoding='gbk', newline='') as f:
                file = csv.writer(f)
                file.writerow(list1)
            showinfo(title='注意', message='进程结束')
        else:
            showinfo(title='注意', message='返回')

    def init_csv_len():  # 重置文件函数
        name = 'len.csv'
        list1 = ['借钱时间', '借入金额', '借入原因', '出钱人', '收钱人', '还钱时间', '有无利息', '利息大小']
        ask = askyesno(title='注意', message='是否继续')
        if ask:
            with open(name, 'w', encoding='gbk', newline='') as f:
                file = csv.writer(f)
                file.writerow(list1)
            showinfo(title='注意', message='进程结束')
        else:
            showinfo(title='注意', message='返回')

    def init_csv_in():  # 重置文件函数
        name = 'in.csv'
        list1 = ['收入时间', '收入金额', '收入来源']
        ask = askyesno(title='注意', message='是否继续')
        if ask:
            with open(name, 'w', encoding='gbk', newline='') as f:
                file = csv.writer(f)
                file.writerow(list1)
            showinfo(title='注意', message='进程结束')
        else:
            showinfo(title='注意', message='返回')

    def _quit():
        win.quit()
        win.destroy()

    for i in range(2):  # 使内部控件可以随着父级窗口大小改变而改变
        win.grid_rowconfigure(index=i, weight=1)
    for k in range(3):
        win.grid_columnconfigure(index=k, weight=1)
    win.grid_rowconfigure(index=2, weight=0)

    initlabel = Label(win, text='选择保存的文件类型', font=('楷体', 15, 'bold'))  # 建立第一个文本
    initlabel.grid(row=0, column=0, columnspan=3)  # 位置的布局

    # save_csv() 调用函数
    # save_csv 指向函数地址
    sbt1 = Button(win, text='收入', command=init_csv_in)
    sbt1.grid(row=1, column=0, sticky=W + S + E + N)

    sbt2 = Button(win, text='支出', command=init_csv_out)
    sbt2.grid(row=1, column=1, sticky=W + S + E + N)

    sbt2 = Button(win, text='借款', command=init_csv_len)
    sbt2.grid(row=1, column=2, sticky=W + S + E + N)

    bt_q = Button(win, text='返回', command=_quit)
    bt_q.grid(row=3, column=2, sticky=W + S + E + N)

    win.mainloop()


def lenwin():
    # global a
    win2 = Tk()
    win2.title('资金借入记录')

    def _quit():
        win2.quit()
        win2.destroy()

    def lenedit():
        ask = askyesno(title='注意', message='是否继续')
        if ask:
            if v1.get() == 1:
                a = '有'
            if v1.get() == 0:
                a = '无'
            with open('len.csv', 'a', encoding='gbk', newline='') as f:
                file = csv.writer(f)
                file.writerow(
                    [ent_time.get(),
                     ent_money.get(),
                     ent_reason.get(),
                     ent_name1.get(),
                     ent_name2.get(),
                     ent_time1.get(),
                     a,
                     ent.get()])
            showinfo(title='注意', message='进程结束')
            _quit()  # 关闭原来有数据的窗口
            lenwin()  # 重新建立一个空白的窗口
        else:
            showinfo(title='注意', message='返回')

    for i in range(8):  # 使内部控件可以随着父级窗口大小改变而改变
        win2.grid_rowconfigure(index=i, weight=1)
    for k in range(3):  # 行数
        win2.grid_columnconfigure(index=k, weight=1)
    win2.grid_rowconfigure(index=6, weight=0)

    win2.minsize(width=300, height=150)  # 设置窗口最小的大小

    label_time = Label(win2, text='借钱时间', font=('楷体', 15, 'bold'))
    label_time.grid(row=0, column=0, sticky=W + S + E + N)

    ent_time = Entry(win2)  # 借钱时间
    ent_time.grid(row=0, column=1, sticky=W + S + E + N, columnspan=2)

    label_money = Label(win2, text='借入金额', font=('楷体', 15, 'bold'))
    label_money.grid(row=1, column=0, sticky=W + S + E + N)

    ent_money = Entry(win2)  # 借钱金额
    ent_money.grid(row=1, column=1, sticky=W + S + E + N, columnspan=2)

    label_reason = Label(win2, text='借入原因', font=('楷体', 15, 'bold'))
    label_reason.grid(row=2, column=0, sticky=W + S + E + N)

    ent_reason = Entry(win2)  # 原因
    ent_reason.grid(row=2, column=1, sticky=W + S + E + N, columnspan=2)

    label_name1 = Label(win2, text='出钱人', font=('楷体', 15, 'bold'))
    label_name1.grid(row=3, column=0, sticky=W + S + E + N)

    ent_name1 = Entry(win2)  # 出钱人
    ent_name1.grid(row=3, column=1, sticky=W + S + E + N, columnspan=2)

    label_name2 = Label(win2, text='收钱人', font=('楷体', 15, 'bold'))
    label_name2.grid(row=4, column=0, sticky=W + S + E + N)

    ent_name2 = Entry(win2)  # 收钱人
    ent_name2.grid(row=4, column=1, sticky=W + S + E + N, columnspan=2)

    label_time1 = Label(win2, text='还钱时间', font=('楷体', 15, 'bold'))
    label_time1.grid(row=5, column=0, sticky=W + S + E + N)

    ent_time1 = Entry(win2)  # 还钱时间
    ent_time1.grid(row=5, column=1, sticky=W + S + E + N, columnspan=2)

    label = Label(win2, text='利息', font=('楷体', 15, 'bold'))

    ent = Entry(win2)  # 利息大小

    def callcha():
        if v1.get() == 1:  # 创建利息大小的交互框
            label.grid(row=7, column=0, sticky=W + S + E + N)
            ent.grid(row=7, column=1, sticky=W + S + E + N, columnspan=2)

        elif v1.get() == 0:  # 在复选框不勾选的时候不显示利息大小交互框
            label.grid_remove()
            ent.grid_remove()  # 利息

    v1 = BooleanVar(master=win2)  # 创建是否有利息的复选框, 这里
    Checkbutton(win2, variable=v1, text='利息', command=callcha).grid(row=6, column=1, sticky=W + S + E + N)

    bt = Button(win2, text='写入', command=lenedit)
    bt.grid(row=9, column=1, sticky=W + S + E + N)

    bt_q = Button(win2, text='返回', command=_quit)
    bt_q.grid(row=9, column=2, sticky=W + S + E + N)

    win2.mainloop()


if __name__ == '__main__':
    outwin()
