import cv2
import datetime

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 represents the default camera

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open camera")
    exit()

# Set the desired frame rate (every 2 seconds)
frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Get the frame rate of the camera
frame_interval = int(frame_rate * 2)  # Calculate the frame interval

# Read and display frames from the camera
frame_count = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Failed to capture frame")
        break

    # Increment the frame count
    frame_count += 1

    # Grab a frame every 2 seconds
    if frame_count % frame_interval == 0:
        # Specify the output path and filename
        output_path = './collect_data/'
    
        # Get the current date and time
        current_time = datetime.datetime.now()

        # Format the date and time into a string
        time_string = current_time.strftime("%Y-%m-%d_%H-%M-%S")

        cv2.putText(img=frame, text=time_string, org=(850, 700), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 0, 0),thickness=2)

        # Generate the file name with the time-series format
        file_name = f"data_{time_string}.jpg"
        
        # Save the image
        cv2.imwrite(output_path + file_name, frame)


    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
