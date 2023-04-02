import soundcard as sc
import soundfile as sf
import tkinter as tk

OUTPUT_FILE_NAME = "out.wav"    # file name.
SAMPLE_RATE = 48000              # [Hz]. sampling rate.
RECORD_SEC = 10                  # [sec]. duration recording audio.

with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
    # record audio with loopback from default speaker.
    data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)

    # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
    sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)


class TextDisplayWidget:

    def __init__(self, master):
        def close():
            self.master.destroy()
        self.master = master
        # Make the window always on
        self.master.overrideredirect(True)
        self.master.wm_attributes("-topmost", True)
        self.master.title("Text Display")

        # Create a label widget to display the text
        self.label = tk.Label(self.master, text="Hello, world!")

        self.label.pack(padx=50, pady=50)
        self.button = tk.Button(self.master, text="hohioiho",
                                command=close)
        self.button.pack(padx=50, pady=50)


if __name__ == '__main__':
    root = tk.Tk()
    widget = TextDisplayWidget(root)
    root.mainloop()
