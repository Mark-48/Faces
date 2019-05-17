import vk_api
import random
import os
import webbrowser
import dlib
import sys
from skimage import io
from scipy.spatial import distance
import urllib.request
import time
from vk_api.longpoll import VkLongPoll, VkEventType
print("Bot activated......")
vk=vk_api.VkApi(token="Token vk-bot")
vk._auth_token()
#основной цикл
while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        print(body.lower())
        if body.lower() == "начало":
            vk.method("messages.send",
                      {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
        elif body.lower()=="кот":
            vk.method("messages.send",
                      {"peer_id": id, "message": "Казнить грешника!", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "привет":
            vk.method("messages.send",
                      {"peer_id": id, "message": "Пашел нафуй", "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "нет":
            vk.method("messages.send",
                      {"peer_id": id, "message": "Пидора ответ))))))))", "random_id": random.randint(1, 2147483647),})


        elif body.lower()=='лицо':
            vk.method("messages.send",
                      {"peer_id": id, "message": "Давай ссылку", "random_id": random.randint(1, 2147483647), })
            break


        else:
            x=["Чего?","А?","Переспроси","обьясни!","Каво?","чтооооо?"]
            vk.method("messages.send", {"random_id":0,"peer_id": id, "message": x[random.randint(0,5)]})
    break

while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["from_id"]
        bady = messages["items"][0]["last_message"]["text"]
        print(bady.lower())
        url = (bady.lower())
        name = "face.jpg"


        def download(url):
            urllib.request.urlretrieve(url, name)


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
        # print(face_descriptor1)
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
        if x == 1:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/1.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 2:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/2.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 3:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/3.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 4:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/4.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 5:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/5.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 6:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/6.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 7:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/7.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 8:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/8.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 9:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/9.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 10:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/10.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 11:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/11.jpg",
                       "random_id": random.randint(1, 2147483647)})
        if x == 12:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Вооо- http://network42.info/faces/Photo/12.jpg",
                       "random_id": random.randint(1, 2147483647)})
        # im = 'ph.jpg'
        # img = Image.open(r"C:/Users/maksim/Desktop/FaceFacts/FF/Ph/" + str(x) + str(im))
        # img.show()




