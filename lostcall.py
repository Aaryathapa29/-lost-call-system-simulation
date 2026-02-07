import random
import tkinter as tk


SERVERS = 2
SIM_TIME = 100


current_time = 0
busy_servers = 0
served_calls = 0
lost_calls = 0

active_calls = []  



root = tk.Tk()
root.title("Telephone Lost Call System")
root.geometry("420x350")

title = tk.Label(root, text="📞 TELEPHONE CALL CENTER SIMULATION", font=("Arial", 14, "bold"))
title.pack(pady=10)

time_label = tk.Label(root, text="Time: 0", font=("Arial", 11))
time_label.pack()

busy_label = tk.Label(root, text="Busy Servers: 0", font=("Arial", 11))
busy_label.pack()

served_label = tk.Label(root, text="Served Calls: 0", font=("Arial", 11))
served_label.pack()

lost_label = tk.Label(root, text="Blocked Calls: 0", font=("Arial", 11))
lost_label.pack()

status_label = tk.Label(root, text="Status: Waiting", font=("Arial", 11))
status_label.pack(pady=10)

running = False


def simulation_step():
    global current_time, busy_servers, served_calls, lost_calls, active_calls, running

    if not running:
        return

    if current_time >= SIM_TIME:
        status_label.config(text="Status: Simulation Finished")
        return

    current_time += 1

  
    if random.random() < 0.5:
        if len(active_calls) < SERVERS:
            service_time = random.randint(2, 5)
            active_calls.append(service_time)
            status_label.config(text="Status: Call Accepted")
        else:
            lost_calls += 1
            status_label.config(text="Status: Call Blocked")

 
    new_calls = []
    for t in active_calls:
        if t > 1:
            new_calls.append(t-1)
        else:
            served_calls += 1

    active_calls = new_calls
    busy_servers = len(active_calls)

    time_label.config(text=f"Time: {current_time}")
    busy_label.config(text=f"Busy Servers: {busy_servers}")
    served_label.config(text=f"Served Calls: {served_calls}")
    lost_label.config(text=f"Blocked Calls: {lost_calls}")

   
    root.after(500, simulation_step)



def start_simulation():
    global running
    running = True
    simulation_step()


start_btn = tk.Button(root, text="▶ START SIMULATION", font=("Arial", 11), command=start_simulation)
start_btn.pack(pady=15)

root.mainloop()
