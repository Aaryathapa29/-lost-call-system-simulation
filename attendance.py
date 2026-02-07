import tkinter as tk
import random

# ---------------- PARAMETERS ----------------
STUDENTS = 15
CLASS_START = 10      # minutes
MAX_ARRIVAL = 20      # max arrival time
MOVE_STEP = 5

# ---------------- SIMULATION CLASS ----------------
class AttendanceSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance Simulation (Animated)")

        self.canvas = tk.Canvas(root, width=900, height=400, bg="white")
        self.canvas.pack()

        self.info = tk.Label(
            root,
            text="Green = On Time | Red = Late",
            font=("Arial", 12)
        )
        self.info.pack()

        self.students = []
        self.arrival_times = []
        self.current = 0

        self.draw_classroom()
        self.create_students()

        self.root.after(1000, self.simulate)

    def draw_classroom(self):
        self.canvas.create_rectangle(750, 80, 880, 320, fill="lightgray")
        self.canvas.create_text(815, 60, text="Classroom", font=("Arial", 10))

    def create_students(self):
        for i in range(STUDENTS):
            y = 90 + i * 15
            student = self.canvas.create_oval(50, y, 70, y + 20, fill="blue")
            self.students.append(student)
            self.arrival_times.append(random.randint(0, MAX_ARRIVAL))

    def simulate(self):
        if self.current >= STUDENTS:
            return

        student = self.students[self.current]
        arrival = self.arrival_times[self.current]

        # Decide status
        if arrival <= CLASS_START:
            color = "green"
            status = "On Time"
        else:
            color = "red"
            status = "Late"

        self.canvas.itemconfig(student, fill=color)

        def move():
            self.canvas.move(student, MOVE_STEP, 0)
            x = self.canvas.coords(student)[2]
            if x < 750:
                self.root.after(30, move)

        move()
        self.current += 1
        self.root.after(800, self.simulate)


# ---------------- RUN PROGRAM ----------------
root = tk.Tk()
app = AttendanceSimulation(root)
root.mainloop()