import cv2
import mediapipe as mp

#inisialisasi MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

#Webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
       break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        lm = results.pose_landmarks.landmark

        #Landmark penting
        left_shoulder = lm[mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_wrist = lm[mp_pose.PoseLandmark.LEFT_WRIST]
        right_shoulder = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        right_wrist = lm[mp_pose.PoseLandmark.RIGHT_WRIST]

        status = "Tangan Tidak Terangkat"

        #Deteksi tangan kiri/kanan
        if left_wrist.y < left_shoulder.y:
            status = "Tangan Kiri Terangkat"
        elif right_wrist.y < right_shoulder.y:
            status = "Tangan Kanan Trangkat"

        #Tampilkan status
        cv2.putText(img, status, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0), 2)

    cv2.imshow("Deteksi Angkat Tangan", img)

    if cv2.waitKey(1) & 0xFF == ord ('q'):
            break

cap.release()
cv2.destroyAllWindows()
