import cv2

src=cv2.imread('pic.jpg',cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)

#Percentage by Which image is resized
src_percent=50

#Calculate 50% of origial Image
new_width=int((src.shape[1]*src_percent/100))
new_height=int((src.shape[0]*src_percent/100))

dsize=(new_width,new_height)
output=cv2.resize(src,dsize)


cv2.imwrite("newImage.png",output)

new_Image=cv2.imread('newImage.png',cv2.IMREAD_UNCHANGED)
cv2.imshow("title",new_Image)


cv2.waitKey(0)