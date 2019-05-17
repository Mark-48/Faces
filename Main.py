
import webbrowser
from PIL import Image
import dlib
import os
import sys
from skimage import io
from scipy.spatial import distance
import urllib.request
url=input("Ссылка на фото: ")
name="face.jpg"
def download(url):
    urllib.request.urlretrieve(url,name)

download(url)
print('Beginning file download with wget module')
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
img = io.imread('face.jpg')
win1 = dlib.image_window()
win1.clear_overlay()
win1.set_image(img)
dets = detector(img, 1)
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
    win1.clear_overlay()
    win1.add_overlay(d)
    win1.add_overlay(shape)
    face_descriptor1 = facerec.compute_face_descriptor(img, shape)
    i = 2
#print(face_descriptor1)
for x in range(1, 13):
        pop = '.jpg'
        img = io.imread('C:/Users/maksim/Desktop/FaceFacts/FF/Photo/' + str(x) + pop)
        win2 = dlib.image_window()
        win2.clear_overlay()
        win2.set_image(img)
        dets_webcam = detector(img, 1)
        for k, d in enumerate(dets_webcam):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                k, d.left(), d.top(), d.right(), d.bottom()))
            shape = sp(img, d)
            win2.clear_overlay()
            win2.add_overlay(d)
            win2.add_overlay(shape)
            face_descriptor2 = facerec.compute_face_descriptor(img, shape)
            # print(face_descriptor2)
            a = distance.euclidean(face_descriptor1, face_descriptor2)
            print(a)
            if (a <= 0.65):

                break
                print("Совпадение, это один человек")
            else:
                print("Not found in data center")

        if (a <= 0.65):
            break

print(x)
if x==5:
 webbrowser.open('https://vk.com/id435178442')

im='ph.jpg'
img=Image.open(r"C:/Users/maksim/Desktop/FaceFacts/FF/Ph/"+str(x)+str(im))
img.show()
input("By?:")