# -*- coding: utf-8 -*-
"""DeepFace_Kaggle_Dataset

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bStWjANCXAKW9mgtN8ikhIuvy316vQsl
"""

!pip install deepface

from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import os

# Specify the dataset folder path
dataset_folder = '/kaggle/input/lfw-dataset/lfw-deepfunneled/lfw-deepfunneled'
main_folder_path_image = '/kaggle/input/lfw-dataset/lfw-deepfunneled/lfw-deepfunneled'

# Initialize a dictionary to store the results
results = {}

# Get the main folder path from user input
main_folder_path = input("Enter the path to the main folder: ")

# Get the subfolder names to analyze from user input
subfolder_names = input("Enter the names of the subfolders to analyze (separated by commas): ").split(',')

# Remove leading and trailing whitespaces from the subfolder names
subfolder_names = [name.strip() for name in subfolder_names]

# Loop through the specified subfolders
for subfolder_name in subfolder_names:
    folder_path = os.path.join(main_folder_path, subfolder_name)

    # Check if the folder exists and is a directory
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print(f"Processing folder {subfolder_name}...")

        # Loop through all the image files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                # Construct the full path to the image file
                image_path = os.path.join(folder_path, filename)

                # Load the image
                img = cv2.imread(image_path)
                plt.imshow(img[:,:,::-1])
                plt.title("Original Image")
                plt.show()

                # Detect the face
                face = DeepFace.detectFace(image_path, target_size = (224, 224), detector_backend='opencv')

                if face is not None:
                    face = face[0]
                    plt.imshow(face)
                    plt.title("Detected Face")
                    plt.show()

                    # Analyze the face
                    obj = DeepFace.analyze(image_path, enforce_detection=False)

                    if obj is not None:
                        emotion = obj[0]['dominant_emotion']
                        age = obj[0]['age']
                        race = obj[0]['race']

                        print(f"Image {filename}:")
                        print(f"Race is {race}")
                        print(f"Feelings: {emotion}")
                        print(f"Age: {age} years old")
                        print("-------------------------------")
                    else:
                        print(f"Failed to analyze image {filename}.")
                else:
                    print(f"Failed to detect face in image {filename}.")
    else:
        print(f"Folder {subfolder_name} does not exist or is not a directory.")

Subfolders_name = """
AJ_Cook

AJ_Lamas

Aaron_Eckhart

Aaron_Guiel

Aaron_Patterson

Aaron_Peirsol

Aaron_Pena

Aaron_Sorkin

Aaron_Tippin

Abba_Eban

Abbas_Kiarostami

Abdel_Aziz_Al-Hakim

Abdel_Madi_Shabneh

Abdel_Nasser_Assidi

Abdoulaye_Wade

Abdul_Majeed_Shobokshi

Abdul_Rahman

Abdulaziz_Kamilov

Abdullah

Abdullah_Ahmad_Badawi

Abdullah_Gul

Abdullah_Nasseef

Abdullah_al-Attiyah

Abdullatif_Sener

Abel_Aguilar,Abel_Pacheco,Abid_Hamid_Mahmud_Al-Tikriti,Abner_Martinez,Abraham_Foxman,Aby_Har-Even """

