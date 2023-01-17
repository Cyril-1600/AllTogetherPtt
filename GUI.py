import tkinter as tk
from AllTogetherPtt import AllTogetherSpider

window = tk.Tk() #建立tk物件
window.title('O2 Article')
window.geometry('800x600')
window.configure(background='white')

header_label = tk.Label(window, text='O2徵男文章爬蟲')
header_label.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='往前頁數')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

calculate_btn = tk.Button(window, text='相關連結', command=lambda: AllTogetherSpider(height_entry.get()))
calculate_btn.pack()

# 運行主程式
window.mainloop()




