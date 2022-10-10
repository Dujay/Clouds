#-*- coding: utf-8-*-
import cv2

img = cv2.imread("carts/limr.jpg")
img = cv2.resize(img,(700,700))
d = g = r = 0
clicked = False
a = 0
s = 0
b = 0


# def color_fuction(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONUP:
#         global b, r, g, clicked
#         b, g, r = img[y, x]
#         b = int(b)
#         g = int(g)
#         r = int(r)
#         clicked = True
while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color_low = (s, 0, 0)  # Данный цвет
    color_high = (a, 150, 150)  # Данный цвет
    only_hsv = cv2.inRange(hsv, color_low, color_high)
    img = cv2.GaussianBlur(img, (5, 5), 2)
    print(a, s, sep="----")
    cv2.imshow('color_hsv', hsv)
    cv2.imshow('hsv', only_hsv)
    cv2.imshow("main", img)
    # if clicked:
    # cv2.rectangle(img, (10, 10), (100, 100), (b, g, r), 0)
    #
    # if b + g + r <= 400:
    # cv2.putText(img, "R = " + str(r) + "; G = " + str(g) + "; B = " + str(b), (50, 50), 2, 1.0, (255, 255, 255))
    # else:
    # cv2.putText(img, "R = " + str(r) + "; G = " + str(g) + "; B = " + str(b), (50, 50), 2, 1.0, (0, 0, 0))
    # clicked = False

    if cv2.waitKey(20) & 0xFF == ord('q'):
        a += 2
    if cv2.waitKey(20) & 0xFF == ord('w'):
        a -= 2
    if cv2.waitKey(20) & 0xFF == ord('e'):
        s += 2
    if cv2.waitKey(20) & 0xFF == ord('r'):
        s -= 2


    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
