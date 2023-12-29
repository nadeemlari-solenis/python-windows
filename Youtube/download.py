from pytube import YouTube
# import tkinter as tk
import time
from tkinter import filedialog
import sys


def download_video(url, save_path):
    try:
        # print("Downloading...")
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_resolution = stream.get_highest_resolution()
        highest_resolution.download(output_path=save_path)

        print("Download completed!!")
        time.sleep(2)
    except Exception as e:
        print(e)


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_bar = f'Downloading: [{int(percentage_of_completion) * "="}>] {int(percentage_of_completion)}%'
    sys.stdout.write('\r' + progress_bar)
    sys.stdout.flush()


def open_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        print(f"selected folder: {folder_selected}")
        return folder_selected


if __name__ == '__main__':
    # root = tk.Tk()
    # root.withdraw()
    downloadUrl = input("Enter the url of the video: ")
    # path_save = open_folder()
    path_save = "C:/Users/mnadeem/OneDrive - Solenis LLC/Desktop/Youtube"
    download_video(downloadUrl, path_save)
