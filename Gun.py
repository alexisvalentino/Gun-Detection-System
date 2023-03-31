import numpy as np
import cv2
import imutils
import telegram
import datetime
import pygame

bot = telegram.Bot(token='5844984312:AAF7vPopMgywe9UTH1gfNefAxFHgCKhHiUM')
CHAT_ID = 917130524

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

firstFrame = None
gun_exist = False
alarm_active = False

pygame.init()
alarm_sound = pygame.mixer.Sound('alarm.wav')

while True:
    ret, frame = camera.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    if len(gun) > 0:
        gun_exist = True
    else:
        gun_exist = False

    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1)

    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if gun_exist:
        print("guns detected")
        if not alarm_active:
            alarm_sound.play(-1)
            alarm_active = True
    else:
        print("guns NOT detected")
        if alarm_active:
            alarm_sound.stop()
            alarm_active = False

    if key == ord('s'):
        if alarm_active:
            alarm_sound.stop()
            alarm_active = False

    if gun_exist:
        print("guns detected")
        try:
            # Save the image of the detected gun
            detected_gun_image = "detected_gun.jpg"
            cv2.imwrite(detected_gun_image, frame)

            # Send the image to the Telegram chat
            with open(detected_gun_image, "rb") as img:
                bot.send_photo(chat_id=CHAT_ID, photo=img, caption="Guns detected!")

        except Exception as e:
            print("Error while sending message:", e)

camera.release()
cv2.destroyAllWindows()
pygame.quit()