import tkinter
from tkinter import ttk

class application(object):
    def __init__(self):
        self.win = tkinter.Tk()
        # 给主窗口设置标题内容
        self.win.title("成绩处理系统（相城区学校版）")
        self.win.geometry('400x300')
        self.win.resizable(0, 0)

        self.tabControl = ttk.Notebook(self.win)  # Create Tab Control

        '''self.tab1 = ttk.Frame(self.tabControl)  # Create a tab
        self.tabControl.add(self.tab1, text='数据库')  # Add the tab

        self.tab2 = ttk.Frame(self.tabControl)  # Add a second tab
        self.tabControl.add(self.tab2, text='导入数据')  # Make second tab visible

        self.tab3 = ttk.Frame(self.tabControl)  # Add a third tab
        self.tabControl.add(self.tab3, text='数据分析')  # Make second tab visible
        self.tab4 = ttk.Frame(self.tabControl)  # Add a third tab
        self.tabControl.add(self.tab4, text='其他')  # Make second tab visible
        self.tabControl.pack(expand=1, fill="both")  # Pack to make visible
        '''
        self.tab={}
        self.frame={}
        tabtxt=('数据库',"导入文件",'数据分析',"其他")
        frametxt=("数据库相关操作","导入文件或文件夹中的数据","成绩分析","其他")
        for i in range(0,4):
            self.tab[i]=ttk.Frame(self.tabControl)
            self.tabControl.add(self.tab[i],text=tabtxt[i])
            self.frame[i]=ttk.LabelFrame(self.tab[i],text=frametxt[i])
            self.frame[i].grid(column=0,row=0,padx=4,pady=6)
            self.frame[i].pack(expand=1,fill="both")
        self.tabControl.pack(expand=1, fill="both")  # Pack to make visible

        # 完成布局


    def gui_arrang(self):
        pass


def main():
    # 初始化对象
    app = application()
    # 进行布局
    app.gui_arrang()
    # 主程序执行
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()