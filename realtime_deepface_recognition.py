# -*- coding: utf-8 -*-
"""realtime_Deepface recognition

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zHscbhoDX4NPzyjb6kwd-BKjKSPby3AJ
"""

!pip install deepface opencv-python

import cv2
import deepface
from IPython.display import display, clear_output
import numpy as np

def show_camera():
    cap = cv2.VideoCapture(1)
    while True:
        ret, frame = cap.read()
        display(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def real_time_face_recognition():
    cap = cv2.VideoCapture(0)
    deepface.set_verbose(False)

    while True:
        ret, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = deepface.detect_faces(frame_rgb)

        for face in faces:
            x, y, w, h = face['box']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            face_rgb = frame_rgb[y:y+h, x:x+w]
            face_resized = cv2.resize(face_rgb, (224, 224))

            obj = deepface.analyze(face_resized, actions=['emotion', 'age', 'race'], enforce_detection=False)

            emotion = obj[0]['dominant_emotion']
            age = obj[0]['age']
            race = obj[0]['race']

            cv2.putText(frame, f"Emotion: {emotion}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv2.putText(frame, f"Age: {age} years old", (x, y + h + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv2.putText(frame, f"Race: {race}", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        display(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

show_camera()

