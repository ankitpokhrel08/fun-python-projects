import tkinter as tk
from tkinter import simpledialog, ttk
import time


class TowerOfHanoi:
    def __init__(self, canvas, num_disks, move_label, speed_var):
        self.canvas = canvas
        self.num_disks = num_disks
        self.rods = [[], [], []]
        self.disk_ids = []
        self.disk_colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "lime", "brown"]
        self.move_label = move_label
        self.speed_var = speed_var
        self.create_disks()

    def create_disks(self):
        """Creates disks and places them on the first rod."""
        for i in range(self.num_disks, 0, -1):
            disk_width = i * 20
            x0 = 100 - disk_width // 2
            x1 = 100 + disk_width // 2
            y0 = 400 - len(self.rods[0]) * 20
            y1 = y0 + 20
            color = self.disk_colors[i - 1]  # Assign unique color to each disk
            disk_id = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
            self.rods[0].append(i)
            self.disk_ids.append(disk_id)

    def move_disk(self, from_rod, to_rod):
        """Moves a disk from one rod to another with animations."""
        disk = self.rods[from_rod].pop()
        self.rods[to_rod].append(disk)
        disk_id = self.disk_ids[disk - 1]

        # Update the label to show the move
        self.move_label.config(text=f"Moving disk {disk} from Rod {from_rod + 1} to Rod {to_rod + 1}")

        # Get current coordinates and calculate the new position
        x0, y0, x1, y1 = self.canvas.coords(disk_id)
        new_x = 100 + 200 * to_rod
        new_y = 400 - len(self.rods[to_rod]) * 20

        speed = 0.01 * float(self.speed_var.get())  # Adjust speed dynamically

        # Animation: Move up
        while y0 > 100:
            self.canvas.move(disk_id, 0, -5)
            self.canvas.update()
            time.sleep(speed)
            x0, y0, x1, y1 = self.canvas.coords(disk_id)

        # Animation: Move horizontally
        while abs(x0 - new_x) > 5:
            self.canvas.move(disk_id, 5 if x0 < new_x else -5, 0)
            self.canvas.update()
            time.sleep(speed)
            x0, y0, x1, y1 = self.canvas.coords(disk_id)

        # Animation: Move down
        while y0 < new_y:
            self.canvas.move(disk_id, 0, 5)
            self.canvas.update()
            time.sleep(speed)
            x0, y0, x1, y1 = self.canvas.coords(disk_id)

    def solve_hanoi(self, n, from_rod, to_rod, aux_rod):
        """Solves the Tower of Hanoi puzzle using recursion."""
        if n == 1:
            self.move_disk(from_rod, to_rod)
            return
        self.solve_hanoi(n - 1, from_rod, aux_rod, to_rod)
        self.move_disk(from_rod, to_rod)
        self.solve_hanoi(n - 1, aux_rod, to_rod, from_rod)


def main():
    root = tk.Tk()
    root.title("Tower of Hanoi")

    canvas = tk.Canvas(root, width=600, height=450, bg="white")
    canvas.pack()

    # Rods visualization
    for i in range(3):
        x = 100 + 200 * i
        canvas.create_rectangle(x - 5, 100, x + 5, 400, fill="black")
        canvas.create_text(x, 420, text=f"Rod {i + 1}", font=("Arial", 12))

    # Label for moves
    move_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
    move_label.pack()

    # Speed adjustment slider
    speed_frame = tk.Frame(root)
    speed_frame.pack()
    tk.Label(speed_frame, text="Speed:", font=("Arial", 12)).pack(side="left")
    speed_var = tk.StringVar(value="1")
    speed_slider = ttk.Scale(speed_frame, from_=0.1, to=5, variable=speed_var, orient="horizontal", length=200)
    speed_slider.pack(side="left")

    # Ask for number of disks
    num_disks = simpledialog.askinteger("Input", "Enter the number of disks:", minvalue=1, maxvalue=10)
    if num_disks is None:
        return

    hanoi = TowerOfHanoi(canvas, num_disks, move_label, speed_var)
    root.after(1000, hanoi.solve_hanoi, num_disks, 0, 2, 1)
    root.mainloop()


if __name__ == "__main__":
    main()