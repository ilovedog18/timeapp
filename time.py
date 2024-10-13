import tkinter as tk
import time

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Đếm Giờ")
        self.master.geometry("300x200")
        
        self.label = tk.Label(master, text="Thời gian:", font=("Helvetica", 24))
        self.label.pack(pady=20)
        
        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")
        
        self.time_display = tk.Label(master, textvariable=self.time_var, font=("Helvetica", 48))
        self.time_display.pack()
        
        self.start_button = tk.Button(master, text="Bắt đầu", command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(master, text="Dừng", command=self.stop_timer)
        self.stop_button.pack(pady=10)
        
        self.reset_button = tk.Button(master, text="Đặt lại", command=self.reset_timer)
        self.reset_button.pack(pady=10)
        
        self.running = False
        self.elapsed_time = 0  # Thời gian đã trôi qua

    def start_timer(self):
        if not self.running:
            self.running = True
            self.run_timer()

    def run_timer(self):
        if self.running:
            self.elapsed_time += 1
            hours, remainder = divmod(self.elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.time_var.set(f"{hours:02}:{minutes:02}:{seconds:02}")
            self.master.after(1000, self.run_timer)  # Gọi lại hàm sau 1000ms (1 giây)

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.elapsed_time = 0
        self.time_var.set("00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
