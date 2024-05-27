# DeepFace_Model :
- This code uses the DeepFace library to analyze facial features in images from the LFW dataset, detecting faces, emotions, ages, and races, and printing the results for each image.
# About the file:
- Code Summary:

  - Model Name: DeepFace
      - Dataset Used: LFW (Labeled Faces in the Wild) dataset
  - Working:
      - The code takes a main folder path and subfolder names as input from the user.
      It loops through the specified subfolders and analyzes each image file (jpg, jpeg, or png) in the folder.
      For each image, it detects the face using DeepFace's detectFace function.
      If a face is detected, it analyzes the face using DeepFace's analyze function, which returns the dominant emotion, age, and race of the person in the image.
      The code then prints the results for each image, including the image name, race, dominant emotion, and age.
  - Output:
      - The output of the code is a series of print statements for each image, including the image name, race, dominant emotion, and age.
      - For example:
      - Image AJ_Cook.jpg:
      - Race is White
      - Feelings: happy
      - Age: 30 years old
      - Image AJ_Lamas.jpg:
      - Race is White
      - Feelings: neutral
      - Age: 35 years old
  - Note: The output may vary depending on the images in the dataset and the performance of the DeepFace model.
  # Realtime Recognition :
  - Done
