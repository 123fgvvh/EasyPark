import cv2    # OpenCV library for image handling and GUI functions
import pickle # pickle for saving/loading data to/from a file

# Define the width and height for each parking slot
SLOT_WIDTH, SLOT_HEIGHT = 107, 48

# Attempt to load existing parking slot positions from a file, or initialize an empty list if it doesn't exist
try:
    with open('CarParkPos', 'rb') as f:
        parking_positions = pickle.load(f) # Load positions from 'CarParkPos' file
except FileNotFoundError:
    parking_positions = [] # If file is not found, start with an empty list

def handle_mouse_click(event, x, y, flags, params):
    """
    Callback function to handle mouse events for adding/removing parking slots.
    - Left-click adds a new slot at the clicked position.
    - Right-click removes a slot if clicked within an existing slot's area.
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        # Add a new parking slot at the (x, y) position of the left mouse click
        parking_positions.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Right-click removes a slot if clicked within an existing slot's rectangle
        for index, pos in enumerate(parking_positions):
            x1, y1 = pos
            # Check if the click is within the boundaries of this parking slot
            if x1 < x < x1 + SLOT_WIDTH and y1 < y < y1 + SLOT_HEIGHT:
                parking_positions.pop(index) # Remove the slot from the list
                break  # Exit the loop after removing the first match

    # Save the updated list of parking slots to the file after any change
    with open('CarParkPos', 'wb') as f:
        pickle.dump(parking_positions, f)

def main():
    """
    Main function to display the image with interactive parking slot marking.
    Continuously displays the image and updates it with marked parking slots.
    """
    # Infinite loop to keep the window open and responsive to mouse events
    while True:
        # Load the image each time to ensure a clean slate for drawing
        img = cv2.imread('carParkImg.png')

        # Draw each parking slot from parking_positions onto the image
        for pos in parking_positions:
            top_left = pos  # Top-left corner of the rectangle
            bottom_right = (pos[0] + SLOT_WIDTH, pos[1] + SLOT_HEIGHT) # Bottom-right corner
            # Draw a rectangle for each parking slot
            cv2.rectangle(img, top_left, bottom_right, (255, 0, 255), 2) # Magenta color, thickness of 2

        # Display the image with drawn rectangles in a window named "Parking Layout"
        cv2.imshow("Parking Layout", img)

        # Set the mouse callback function for the window to handle clicks
        cv2.setMouseCallback("Parking Layout", handle_mouse_click)

        # Refresh display; wait 1 ms for any key press to continue looping
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Exit loop if 'q' is pressed

    # Close all OpenCV windows after exiting the loop
    cv2.destroyAllWindows()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
