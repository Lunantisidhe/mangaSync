import keyboard
import tkinter as tk

key_1 = 'z'
key_2 = '-'

pressed_keys = {key_1: False, key_2: False}

title = "done"
message = "done!"
duration_seconds = 2
size = "300x200+650+300"


def on_key_press(event):
    global pressed_keys

    if event.name in pressed_keys:
        pressed_keys[event.name] = True

        if all(pressed_key for pressed_key in pressed_keys.values()):
            show_toast()
            reset_keys()


def show_toast():
    global title, message, duration_seconds, size

    toast = tk.Tk()
    toast.title(title)
    toast.geometry(size)

    label = tk.Label(toast, text=message, padx=10, pady=10)
    label.pack(anchor="center", pady=(toast.winfo_reqheight() - label.winfo_reqheight()) // 2)

    toast.after(duration_seconds * 300, toast.destroy)

    toast.mainloop()


def reset_keys():
    global pressed_keys

    pressed_keys = {key_1: False, key_2: False}


keyboard.on_press_key(key_1, on_key_press)
keyboard.on_press_key(key_2, on_key_press)
keyboard.wait()
