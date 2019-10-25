import tkinter as tk
import tkinter.font as tkFont

music_window = tk.Tk()
music_window.title("music player")
music_window['background'] = 'white'
music_window.geometry("1020x570")
# music_window.overrideredirect(True)

# 左侧菜单栏
frm_l = tk.Frame(music_window, bg='#F7F7F7', width=210)
# 图标和名称
frm_l_t = tk.Frame(frm_l, bg='#F7F7F7')
flag1 = tk.PhotoImage(file="images/flag.png")
tk.Label(frm_l_t, image=flag1, bg='#F7F7F7').grid(row=0, column=0)
ft1 = tkFont.Font(family='华文新魏', size=15, weight=tkFont.BOLD)
tk.Label(frm_l_t, text="心随乐动", font=ft1, bg='#F7F7F7').grid(row=0, column=1)
frm_l_t.pack(side=tk.TOP, padx=45, pady=10)
# 菜单栏
frm_l_b = tk.Frame(frm_l, bg='#F7F7F7')
ft2 = tkFont.Font(family='华文新魏', size=11)
tk.Label(frm_l_b, text="我的音乐", font=ft2, bg='#F7F7F7').pack()
# 音乐库
frm_l_b_1 = tk.Frame(frm_l_b, bg='#F7F7F7')
flag2 = tk.PhotoImage(file="images/myMusic.png")
tk.Label(frm_l_b_1, image=flag2, bg='#F7F7F7').grid(row=0, column=0)
ft3 = tkFont.Font(family='华文新魏', size=12)
tk.Label(frm_l_b_1, text="音乐库", font=ft3, bg='#F7F7F7').grid(row=0, column=1)
frm_l_b_1.pack(pady=5)
# 我喜欢
frm_l_b_2 = tk.Frame(frm_l_b, bg='#F7F7F7')
flag3 = tk.PhotoImage(file="images/like.png")
tk.Label(frm_l_b_2, image=flag3, bg='#F7F7F7').grid(row=0, column=0)
tk.Label(frm_l_b_2, text=" 我喜欢", font=ft3, bg='#F7F7F7').grid(row=0, column=1)
frm_l_b_2.pack(pady=5)
# 待开发
frm_l_b_3 = tk.Frame(frm_l_b, bg='#F7F7F7')
flag4 = tk.PhotoImage(file="images/history.png")
tk.Label(frm_l_b_3, image=flag4, bg='#F7F7F7').grid(row=0, column=0)
tk.Label(frm_l_b_3, text=" 待开发", font=ft3, bg='#F7F7F7').grid(row=0, column=1)
frm_l_b_3.pack(pady=5)
frm_l_b.pack(padx=45, pady=10)
frm_l.pack(side=tk.LEFT, fill=tk.Y)

# 右侧展示区
frm_r = tk.Frame(music_window, bg='white', width=810, height=100)
# 搜索栏
frm_r_t = tk.Frame(frm_r, bg='white', width=810, height=60)
tk.Entry(frm_r_t).pack(side=tk.LEFT, pady=10, padx=50)
frm_r_t.pack(side=tk.TOP, fill=tk.BOTH)
# 歌曲列表
frm_r_c = tk.Frame(frm_r, bg='red')
frm_r_c.pack(fill=tk.BOTH, expand=tk.YES)
# 播放控制
frm_r_b = tk.Frame(frm_r, bg='green', width=810, height=100)
frm_r_b.pack(side=tk.BOTTOM, fill=tk.BOTH)

frm_r.pack(side=tk.RIGHT, fill=tk.Y)

music_window.mainloop()
