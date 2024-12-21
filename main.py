import cv2

def pencil_art(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
    inverted_one = cv2.bitwise_not(gray_image)
    blured_one = cv2.GaussianBlur(inverted_one, (21, 21), sigmaX=0, sigmaY=0)
    invertedand_blurred = cv2.bitwise_not(blured_one)
    pencilsketch_photo = cv2.divide(gray_image, invertedand_blurred, scale=256.0)
    return pencilsketch_photo

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    sketch_frame = pencil_art(frame)
    combined = cv2.hconcat([frame, cv2.cvtColor(sketch_frame, cv2.COLOR_GRAY2BGR)])
    cv2.imshow("Original vs Pencil image", combined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
