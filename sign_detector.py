

import cv2
import mediapipe as mp
import math

# Function to calculate distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# Function to check if the gesture is "Thumbs Up"
def is_thumbs_up(landmarks):
    thumb_tip = landmarks.landmark[4]  # Tip of the thumb
    thumb_ip = landmarks.landmark[3]    # Thumb IP joint
    index_mcp = landmarks.landmark[5]   # Index finger MCP joint

    return thumb_tip.y < thumb_ip.y < index_mcp.y

# Function to check if the gesture is "Thumbs Down"
def is_thumbs_down(landmarks):
    thumb_tip = landmarks.landmark[4]  # Tip of the thumb
    thumb_ip = landmarks.landmark[3]    # Thumb IP joint
    index_mcp = landmarks.landmark[5]   # Index finger MCP joint

    return thumb_tip.y > thumb_ip.y > index_mcp.y

# Function to check if the gesture is "Rock" (Fist with thumb tucked in)
def is_rock(landmarks):
    thumb_tip = landmarks.landmark[4]  # Tip of the thumb
    index_mcp = landmarks.landmark[5]   # Index finger MCP joint
    return thumb_tip.x < index_mcp.x  # Thumb tucked in

# Function to check if the gesture is "Five" (All fingers extended)
def is_five(landmarks):
    # Check if all the fingertips (except thumb) are above their respective MCP joints
    return all(landmarks.landmark[i].y < landmarks.landmark[i - 2].y for i in range(8, 21, 4))

# Function to check if the gesture is "Three" (First three fingers extended)
def is_three(landmarks):
    return (landmarks.landmark[8].y < landmarks.landmark[6].y and  # Index finger extended
            landmarks.landmark[12].y < landmarks.landmark[10].y and  # Middle finger extended
            landmarks.landmark[16].y < landmarks.landmark[14].y and  # Ring finger extended
            landmarks.landmark[20].y > landmarks.landmark[18].y)  # Pinky folded

def run_sign_detection():
    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=2)
    mp_draw = mp.solutions.drawing_utils

    # Open webcam or video input
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Draw landmarks
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Check and display the corresponding gesture
                if is_thumbs_up(hand_landmarks):
                    cv2.putText(frame, "Thumbs Up!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif is_thumbs_down(hand_landmarks):
                    cv2.putText(frame, "Thumbs Down!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif is_rock(hand_landmarks):
                    cv2.putText(frame, "Rock!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif is_five(hand_landmarks):
                    cv2.putText(frame, "Five!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif is_three(hand_landmarks):
                    cv2.putText(frame, "Three!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Hand Sign Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_sign_detection()
