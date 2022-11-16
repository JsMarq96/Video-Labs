#!/usr/bin/env python3

from tkinter import Label, Entry, Button, Tk, filedialog, messagebox, ttk, END
from resizer import resize_video

CODEC_LIST = ['VP8', 'VP9', 'h265', 'AV1']
CODEC_NAME = ['libvpx', 'libvpx-vp9', 'libx265', 'libaom-av1']
EXT_LIST = ['.webm', '.webm', '.mp4', '.webm']


def converter_GUI(window):
    window.title('Converter Utility')
    window.geometry('420x200')

    # VIDEO RESOLUTION GUI
    label = Label(window, text='Video resolution')
    label.grid(column=0, row=0)

    txt_width_res = Entry(window, width=6)
    txt_width_res.grid(column=0, row=1)

    label = Label(window, text='x')
    label.grid(column=0, row=2)

    txt_height_res = Entry(window, width=6)
    txt_height_res.grid(column=0, row=3)

    # VIDEO CODEC SELECTION GUI
    label = Label(window, text='Video codec')
    label.grid(column=1, row=1)

    combo_codec_selector = ttk.Combobox(state='readonly', values=CODEC_LIST)
    combo_codec_selector.grid(column=1, row=2)

    # Video file selection
    txt_video_dir = Entry(window, width=20)
    txt_video_dir.grid(column=0, row=4)

    label = Label(window, text='New video name:')
    label.grid(column=0, row=5)

    txt_new_video_dir = Entry(window, width=20)
    txt_new_video_dir.grid(column=1, row=5)

    def launch_item_search():
        selected_folder = filedialog.askopenfilename()
        txt_video_dir.delete(0, END)
        txt_video_dir.insert(0, selected_folder)

    video_search_button = Button(window,
                                 text='Search video file',
                                 command=launch_item_search)
    video_search_button.grid(column=1, row=4)

    # VIDEO CONVERTION BUTTON
    def launch_conversion():
        new_file_name = txt_new_video_dir.get() + \
            EXT_LIST[combo_codec_selector.current()]

        messagebox.showinfo('Converter Utility', 'Starting compression')

        resize_video(txt_video_dir.get(),
                     new_file_name,
                     txt_width_res.get(),
                     txt_height_res.get(),
                     CODEC_NAME[combo_codec_selector.current()])
        messagebox.showinfo('Converter Utility', 'Finished compression')

    convert_button = Button(window, text='Convert', command=launch_conversion)
    convert_button.grid(column=4, row=2)


if __name__ == '__main__':
    window = Tk()
    converter_GUI(window)
    window.mainloop()
