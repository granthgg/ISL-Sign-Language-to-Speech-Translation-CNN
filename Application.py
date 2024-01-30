import tensorflow
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font
import cv2
import os
import numpy as np
from keras.models import model_from_json
import operator
import time
import sys, os
import matplotlib.pyplot as plt
import pyttsx3
import requests
from string import ascii_uppercase
 

class Application:
    def __init__(self):
        self.engine = None
        self.vs = cv2.VideoCapture(0)
        self.current_image = None
        self.current_image2 = None

        self.json_file = open("model-bw.json", "r")
        self.model_json = self.json_file.read()
        self.json_file.close()
        self.loaded_model = model_from_json(self.model_json)
        self.loaded_model.load_weights( "model-bw.h5")

        self.ct = {}
        self.ct['blank'] = 0
        self.blank_flag = 0
        for i in ascii_uppercase:
            self.ct[i] = 0

        print("Model Loaded")
        pyttsx3.speak("Model Loaded")


        self.root = tk.Tk()
        self.root.title("Sign Language to Speech Converter")
        self.root.geometry("900x1100")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.configure(bg="#FFFFFF")

        self.photo = "Empty"
        self.current_symbol = "Empty"
        self.str = ""
        self.word = ""

        # Initialize the image panel
        self.panel = tk.Label(self.root, bg="#FFFFFF")
        self.panel.place(x=135, y=10, width=640, height=640)

        # Initialize the output labels
        label_font = font.Font(family="Times New Roman", size=40, weight="bold")

        self.T = tk.Label(self.root, text="SIGN LANGUAGE TO SPEECH", font=label_font, bg="#FFFFFF")
        self.T.place(x=31, y=17)

        self.T1 = tk.Label(self.root, text="Symbol :", font=label_font, bg="#FFFFFF")
        self.T1.place(x=10, y=640)

        self.T2 = tk.Label(self.root, text="Word :", font=label_font, bg="#FFFFFF")
        self.T2.place(x=10, y=700)

        self.T3 = tk.Label(self.root, text="Sentence :", font=label_font, bg="#FFFFFF")
        self.T3.place(x=10, y=760)

        # Initialize the output panels
        self.panel3 = tk.Label(self.root, bg="#FFFFFF")
        self.panel3.place(x=500, y=640)

        self.panel4 = tk.Label(self.root, bg="#FFFFFF")
        self.panel4.place(x=220, y=700)

        self.panel5 = tk.Label(self.root, bg="#FFFFFF")
        self.panel5.place(x=350, y=760)

        # Initialize the image panel for video output
        self.panel2 = tk.Label(self.root, bg="#FFFFFF")
        self.panel2.place(x=460, y=95, width=310, height=310)
        #pyttsx3.speak("This Application is Sign Language to Speech Converter")


        self.video_loop()

    def video_loop(self):
        ok, frame = self.vs.read()
        if ok:
            cv2image = cv2.flip(frame, 1)
            x1 = int(0.5 * frame.shape[1])
            y1 = 10
            x2 = frame.shape[1] - 10
            y2 = int(0.5 * frame.shape[1])
            cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
            cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
            self.current_image = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)
            cv2image = cv2image[y1:y2, x1:x2]
            gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 2)
            th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            self.predict(res)

            self.current_image2 = Image.fromarray(res)
            imgtk = ImageTk.PhotoImage(image=self.current_image2)
            self.panel2.imgtk = imgtk
            self.panel2.config(image=imgtk)
            self.panel3.config(text=self.current_symbol, font=("Times New Roman", 50))
            self.panel4.config(text=self.word, font=("Times New Roman", 40))
            self.panel5.config(text=self.str, font=("Times New Roman", 40))

            pyttsx3.speak(text=self.current_symbol)
            #pyttsx3.speak(text=self.word)
            #pyttsx3.speak(text=self.str)

        self.root.after(60, self.video_loop)

    def predict(self, test_image):
        test_image = cv2.resize(test_image, (128, 128))
        result = self.loaded_model.predict(test_image.reshape(1, 128, 128, 1))
        prediction = {}
        prediction['blank'] = result[0][0]
        inde = 1
        for i in ascii_uppercase:
            prediction[i] = result[0][inde]
            inde += 1

        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        self.current_symbol = prediction[0][0]

        if (self.current_symbol == 'blank'):
            for i in ascii_uppercase:
                self.ct[i] = 0
        self.ct[self.current_symbol] += 1
        if (self.ct[self.current_symbol] > 30):
            for i in ascii_uppercase:
                if i == self.current_symbol:
                    continue
                tmp = self.ct[self.current_symbol] - self.ct[i]
                if tmp < 0:
                    tmp *= -1
                if tmp <= 10:
                    self.ct['blank'] = 0
                    for i in ascii_uppercase:
                        self.ct[i] = 0
                    return
            self.ct['blank'] = 0
            for i in ascii_uppercase:
                self.ct[i] = 0
            if self.current_symbol == 'blank':
                if self.blank_flag == 0:
                    self.blank_flag = 1
                    if len(self.str) > 0:
                        self.str += " "
                    self.str += self.word
                    self.word = ""
            else:
                if (len(self.str) > 16):
                    self.str = ""
                self.blank_flag = 0
                self.word += self.current_symbol



    def speak(self):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        self.engine.say()
        self.engine.runAndWait()

    def destructor(self):
        print("Application is Closing !!!")
        #pyttsx3.speak("Application is Closing")
        self.root.destroy()
        self.vs.release()
        cv2.destroyAllWindows()

    def destructor1(self):
        print("Aplication is Closing !!!")
        #pyttsx3.speak("Application is Closing")
        self.root1.destroy()

print("Application is Starting !!!")
pyttsx3.speak("Application is Starting")

pba = Application()
pba.root.mainloop()
