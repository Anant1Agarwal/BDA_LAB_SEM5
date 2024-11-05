import tkinter as tkinter
import random
import time

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.canvas = tk.Canvas(root, width=800, height=400, bg='white')
        self.canvas.pack()
        self.array = []
        self.create_ui()

    def create_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_sorting)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_array)
        self.reset_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.reset_array()
        
    def reset_array(self):
        self.array = [random.randint(1, 100) for _ in range(50)]
        self.draw_array()

    def draw_array(self, color_array=None):
        self.canvas.delete("all")
        canvas_height = 400
        canvas_width = 800
        bar_width = canvas_width / len(self.array)
        offset = 30
        spacing = 5

        if not color_array:
            color_array = ['gray' for _ in range(len(self.array))]

        for i, height in enumerate(self.array):
            x0 = i * bar_width + offset
            y0 = canvas_height - height * 3
            x1 = (i + 1) * bar_width + offset
            y1 = canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

        self.root.update_idletasks()

    def start_sorting(self):
        self.bubble_sort()

    def bubble_sort(self):
        for i in range(len(self.array) - 1):
            for j in range(len(self.array) - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array(['green' if x == j or x == j + 1 else 'gray' for x in range(len(self.array))])
                    time.sleep(0.1)
        self.draw_array(['green' for _ in range(len(self.array))])

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()

