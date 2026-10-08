import cv2
from deepface import DeepFace

# Open Camo camera using Windows DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Could not open Camo camera")
    exit()

# Load face detector
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

print("Camo camera started!")
print("Emotion detector started!")
print("Press Q to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read camera frame")
        break

    # Convert camera image to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    for (x, y, w, h) in faces:

        # Draw rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Get face area
        face = frame[y:y+h, x:x+w]

        try:
            result = DeepFace.analyze(
                face,
                actions=["emotion"],
                enforce_detection=False
            )

            emotion = result[0]["dominant_emotion"]
            confidence = result[0]["emotion"][emotion]

            text = f"{emotion}: {confidence:.2f}%"

            cv2.putText(
                frame,
                text,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        except Exception as e:
            print("Emotion detection error:", e)

    cv2.imshow("Emotion Detector - Camo Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()