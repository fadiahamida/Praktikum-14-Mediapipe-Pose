import cv2
import mediapipe as mp
mpose =mp.solutions.pose #inisiasi media pipe pose
pose = mpose.Pose()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #video dari webcam

while True:
    success, img = cap.read() #pembacaan image
    if not success:
        print("frame gagal, lanjut")
        continue
    imgrgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #konversi warna dari bgr ke rgb
    hasil = pose.process(imgrgb) #ekstraksi dari image
    if hasil.pose_landmarks:
        print ("terdeteksi")
    else:
        print ("tidak terdeteksi")

    cv2.imshow("webcame", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release() # Tutup webcam dan jendela tampilan saat q ditekan
cv2.destroyAllWindows()
