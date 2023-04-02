import threading
from tkinter import Tk
import tkinter as tk
import wave
import pyaudio
import soundcard as sc
import soundfile as sf


class Recorder:
    def __init__(self):
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 2
        self.fs = 44100
        self.frames = []
        self.recording = False
        self.paused = False

    def start(self):
        self.recording = True
        self.paused = False
        self.frames = []
        t = threading.Thread(target=self._record)
        t.start()

    def _record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.sample_format, channels=self.channels,
                            rate=self.fs, frames_per_buffer=self.chunk, input=True)
        while self.recording:
            data = stream.read(self.chunk)
            if not self.paused:
                self.frames.append(data)
        stream.stop_stream()
        stream.close()
        audio.terminate()

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def stop(self):
        self.recording = False
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(pyaudio.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        self.frames = []

    def record_system_audio(self, filename):
        self.filename = filename
        with sc.get_speaker(include_loopback=True).recorder(samplerate=self.fs) as mic:
            # record system audio with loopback from default speaker.
            while self.recording:
                data = mic.record(numframes=self.chunk)
                if not self.paused:
                    sf.write(file=self.filename, data=data, samplerate=self.fs)

    def start_system_audio_recording(self):
        self.recording = True
        self.paused = False
        t = threading.Thread(
            target=self.record_system_audio, args=(self.filename,))
        t.start()

    def pause_system_audio_recording(self):
        self.paused = True

    def resume_system_audio_recording(self):
        self.paused = False


class App:
    def __init__(self, master):
        self.recording = False
        self.paused = False
        self.recording_system_audio = False
        self.paused_system_audio = False
        self.recorder = None
        self.filename = None
        self.filename_system_audio = None

        # UI setup
        self.master = master
        self.master.title("Audio Recorder and Screenshot Taker")

        self.record_button = tk.Button(
            self.master, text="Record", command=self.record)
        self.record_button.pack()

        self.stop_button = tk.Button(
            self.master, text="Stop", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack()

        self.screenshot_button = tk.Button(
            self.master, text="Take Screenshot", command=self.screenshot, state=tk.DISABLED)
        self.screenshot_button.pack()

        self.filename_label = tk.Label(self.master, text="")
        self.filename_label.pack()

        self.record_system_audio_button = tk.Button(
            self.master, text="Record System Audio", command=self.record_system_audio)
        self.record_system_audio_button.pack()

        self.stop_system_audio_button = tk.Button(
            self.master, text="Stop System Audio Recording", command=self.stop_system_audio, state=Tk.DISABLE)

    def run(self):
        self.master.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.run()
