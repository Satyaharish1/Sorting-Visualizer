# Sorting Visualizer in Python using Tkinter
# Implements Bubble Sort, Insertion Sort, and Quick Sort with percentage display

import tkinter as tk
from tkinter import ttk
import random
import time


def bubble_sort(data, draw_data, delay):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['red' if x == j or x == j + 1 else 'blue' for x in range(len(data))])
                time.sleep(delay)
    draw_data(data, ['green' for x in range(len(data))])

def insertion_sort(data, draw_data, delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            draw_data(data, ['red' if x == j or x == i else 'blue' for x in range(len(data))])
            time.sleep(delay)
        data[j + 1] = key
    draw_data(data, ['green' for x in range(len(data))])

def quick_sort(data, low, high, draw_data, delay):
    if low < high:
        pi = partition(data, low, high, draw_data, delay)
        quick_sort(data, low, pi - 1, draw_data, delay)
        quick_sort(data, pi + 1, high, draw_data, delay)
    draw_data(data, ['green' for x in range(len(data))])

def partition(data, low, high, draw_data, delay):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            draw_data(data, ['red' if x == j or x == i else 'blue' for x in range(len(data))])
            time.sleep(delay)
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    max_val = max(data)
    normalized_data = [i / max_val for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        # Draw bar
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

        # Display percentage above each bar
        percent = f"{(data[i] / max_val) * 100:.0f}%"
        canvas.create_text(
            x0 + 10, y0 - 10,
            text=percent,
            fill="black",
            font=("Arial", 9, "bold")
        )

    root.update_idletasks()



def generate_data():
    global data
    size = int(size_entry.get())
    data = [random.randint(10, 100) for _ in range(size)]
    draw_data(data, ['blue' for _ in range(len(data))])

def start_sort():
    global data
    if not data:
        return
    delay = speed_scale.get()
    algo = algo_menu.get()

    if algo == "Bubble Sort":
        bubble_sort(data, draw_data, delay)
    elif algo == "Insertion Sort":
        insertion_sort(data, draw_data, delay)
    elif algo == "Quick Sort":
        quick_sort(data, 0, len(data) - 1, draw_data, delay)

# ------------------------------
# GUI Setup
# ------------------------------

root = tk.Tk()
root.title("Sorting Visualizer")
root.maxsize(800, 600)
root.config(bg="lightgray")

selected_algo = tk.StringVar()
data = []

# UI Frame
UI_frame = tk.Frame(root, width=700, height=200, bg="lightgray")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# Canvas
canvas = tk.Canvas(root, width=700, height=380, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# UI Components
tk.Label(UI_frame, text="Algorithm:", bg="lightgray").grid(row=0, column=0, padx=5, pady=5)
algo_menu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=["Bubble Sort", "Insertion Sort", "Quick Sort"])
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

tk.Label(UI_frame, text="Size:", bg="lightgray").grid(row=0, column=2, padx=5, pady=5)
size_entry = tk.Entry(UI_frame)
size_entry.grid(row=0, column=3, padx=5, pady=5)
size_entry.insert(0, "20")

tk.Label(UI_frame, text="Speed (s):", bg="lightgray").grid(row=0, column=4, padx=5, pady=5)
speed_scale = tk.Scale(UI_frame, from_=0.001, to=0.5, resolution=0.01, orient=tk.HORIZONTAL, length=150)
speed_scale.grid(row=0, column=5, padx=5, pady=5)
speed_scale.set(0.05)

tk.Button(UI_frame, text="Generate", command=generate_data, bg="lightblue").grid(row=1, column=2, padx=5, pady=10)
tk.Button(UI_frame, text="Start", command=start_sort, bg="lightgreen").grid(row=1, column=3, padx=5, pady=10)

root.mainloop()

