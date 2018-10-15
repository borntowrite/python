#########################################################################
# Face Recognition with using face_recognition & dlib
# detect faces from image and save one by one 
#########################################################################
from PIL import Image
import face_recognition
import numpy as np

# image = face_recognition.load_image_file("c:/work/python/stock_people.jpg")
# face_locations = face_recognition.face_locations(image)

# print("I found {} faces in this photo".format(len(face_locations)))
# i=0
# for face_location in face_locations:
# 	top, right, bottom, left = face_location
# 	print("a face located at pixel location top: {}, left: {}, bottom: {}, right: {}".format(top, left, bottom, right))

# 	face_image = image[top:bottom, left:right]
# 	pil_image = Image.fromarray(face_image)
# 	pil_image.save("face-{}.jpg".format(i))
# 	i = i+1
	
#########################################################################
# Face Recognition with using face_recognition & dlib
# compare image 
#########################################################################

image = face_recognition.load_image_file("c:/work/python/Barack_Obama.jpg")
#unknown_image = face_recognition.load_image_file("c:/work/python/face-1.jpg")
unknown_image = face_recognition.load_image_file("c:/work/python/barack_2.jpg")

Barack_encoding = face_recognition.face_encodings(image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([Barack_encoding], unknown_encoding)
print(results)

# arr=["a", "b", "c"]
# test = [i for i in arr]
# print(test)