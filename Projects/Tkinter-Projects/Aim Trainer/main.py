import tkinter
import random

TARGET_RADIUS = 30
X, Y = 340, 30


class MainWindows:
    def __init__(self, width, height, title, target_color):
        self.width = width
        self.height = height
        self.size = self.width if self.width < self.height else self.height
        self.title = title
        self.target_color = target_color
        self.success_counter = 0

        root = tkinter.Tk()
        root.title(self.title)
        root.resizable(False, False)

        self.canvas = tkinter.Canvas(root, width=self.width, height=self.height)
        self.canvas.pack()

        self.draw_target()

    def draw_target(self):
        self.text = self.canvas.create_text(X, Y, text=f"score: {self.success_counter}", font=("Helvetica", 16),
                                            fill="black")

        x = random.randint(self.size * (TARGET_RADIUS / self.size), self.size * (1 - TARGET_RADIUS / self.size))
        y = random.randint(self.size * (TARGET_RADIUS / self.size), self.size * (1 - TARGET_RADIUS / self.size))
        x0 = x - TARGET_RADIUS
        y0 = y - TARGET_RADIUS
        x1 = x + TARGET_RADIUS
        y1 = y + TARGET_RADIUS

        self.target = self.canvas.create_arc(x0, y0, x1, y1, extent=359, start=0, fill=self.target_color,
                                             outline=self.target_color)

        self.canvas.tag_bind(self.target, "<Button-1>", self.on_click)

    def on_click(self, eventx):
        self.canvas.delete(self.target)
        self.canvas.delete(self.text)
        self.success_counter += 1
        self.draw_target()

    def run(self):
        self.canvas.mainloop()


MainWindows(700, 600, "Aim Trainer", "red").run()

