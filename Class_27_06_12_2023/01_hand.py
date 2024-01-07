import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        # draw hand landmarks
        thumb = hand_landmarks.landmark[4]
        index = hand_landmarks.landmark[8]
        middle = hand_landmarks.landmark[12]
        ring = hand_landmarks.landmark[16]
        pinky = hand_landmarks.landmark[20]

        # convert to pixel
        height, width, _ = image.shape

        # convert to pixel
        index = int(index.x * width), int(index.y * height)
        thumb = int(thumb.x * width), int(thumb.y * height)
        middle = int(middle.x * width), int(middle.y * height)
        ring = int(ring.x * width), int(ring.y * height)
        pinky = int(pinky.x * width), int(pinky.y * height)

        # draw line
        cv2.line(image, index, thumb, (0, 0, 255), 2)

        # draw on thumb
        cv2.circle(image, thumb, 20, (0, 0, 255), 2)

        # draw on index
        cv2.circle(image, index, 20, (0, 0, 255), 2)

        # draw on other fingers
        cv2.circle(image, middle, 20, (0, 0, 255), 2)
        cv2.circle(image, ring, 20, (0, 0, 255), 2)
        cv2.circle(image, pinky, 20, (0, 0, 255), 2)
        
        # calculate radius
        radius = (((index[0] - thumb[0])**2 + (index[1] - thumb[1])**2)**0.5) // 2

        # flip the screen horizontally
        image = cv2.flip(image, 1)

        # show radius on screen top left corner
        cv2.putText(image, f'Radius: {int(radius)}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # flip the screen horizontally
        image = cv2.flip(image, 1)
        
        # calculate center
        ox = int((index[0] + thumb[0]) / 2)
        oy = int((index[1] + thumb[1]) / 2)
        
        # draw circle in between thumb and index
        cv2.circle(image, (ox, oy), int(radius), (0, 0, 255), 2)
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()