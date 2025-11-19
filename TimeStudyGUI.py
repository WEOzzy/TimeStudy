import tkinter as tk
import TimeStudyOOP as ts

conn = ts.get_connection()
print(conn)
ts.create_table(conn)
print("table should be created")

def submit_plan_id(event):
    plan_id = plan_id_entry.get()
    print("Details for PlanID: ", plan_id)
    ts.fetch_plan_id(conn, plan_id)

# create the main tkinter app window
app = tk.Tk()
app.title("Time Study")
app.geometry("720x360")

plan_id_label = tk.Label(app, text="Enter Plan ID: ")
plan_id_label.grid(row=0, column=0)
plan_id_entry = tk.Entry(app)
plan_id_entry.grid(row=0, column=1)
app.bind("<Return>", submit_plan_id)


app.mainloop()