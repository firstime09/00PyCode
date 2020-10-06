import cv2

dir = r"C:\Users\Felliks\Pictures\Screenshots"
load_img1 = cv2.imread(dir + "/2N-Gambar_.jpg")
cv2.imshow('Gambar_1', load_img1)

b, r, g = cv2.split(load_img1)
br = b - r
cv2.imshow('Gambar_1BR', br)
bg = b - g
cv2.imshow('Gambar_1BG', bg)
rb = r - b
cv2.imshow('Gambar_1RB', rb)
rg = r - g
cv2.imshow('Gambar_1RG', rg)
gb = g - b
cv2.imshow('Gambar_1GB', gb)
gr = g - r
cv2.imshow('Gambar_1GR', gr)

# load_img2 = cv2.imread(dir + "/2N-Gambar_.jpg")
# load_img3 = cv2.imread(dir + "/3N-Gambar_.jpg")
# cv2.imshow('Gambar_2', load_img2)
# cv2.imshow('Gambar_3', load_img3)
# def bentuk_br(data):
#     im = cv2.imread(data)
#     b, r, g = cv2.split(im)
#     br = b - r
#     return br

k = cv2.waitKey (0)
cv2.destroyAllWindows ()