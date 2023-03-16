import cv2
import numpy as np

# Step 1: Load and show image
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    
    global refPt, cropping
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        
        # draw a rectangle around the region of interest
        cv2.rectangle(img, refPt[0], refPt[1], (0, 0, 255), 2)
        cv2.imshow("Input image", img)

img = cv2.imread(r'C:\Users\Admin\Pictures\chromakey\images.jpg')
clone = img.copy()
image = img.copy()
cv2.imshow("Input image", img)
cv2.setMouseCallback("Input image", click_and_crop)

# Step 2: Choose region of interest that has background color
lst_rois = []
refPt = []
cropping = False

while True:
    # display the image and wait for a keypress
    cv2.imshow("Input image", img)

    key = cv2.waitKey(1) & 0xFF
    
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
        
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
        
# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    lst_rois.append(roi.copy())
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
    
# close all open windows
cv2.destroyAllWindows()

# Step 3: Calculate mean of background color values
threshold = np.mean(np.mean(roi[:], axis = 0), axis = 0)
#threshold = threshold.astype(np.uint8)

# Step 4: Calculate threshold
deviation = np.asarray([10, 32, 5])

# Step 5: Import the image you want to replace
fg = cv2.imread(r'C:\Users\Admin\Pictures\chromakey\hurricane.jpg')

# Step 6: Segmentating image with representative color value and deviation
h, w = fg.shape[0:2]
image = cv2.resize(image, (w, h))
result = np.where(abs(image - threshold) < 2 * deviation, [0, 0, 0], image)

# Step 7: Replace background with choosen image
# Replace where pixels have [0, 0, 0] value
final = np.where(result == [0, 0, 0], fg, image)

# Show result
cv2.imshow("Result", final)
cv2.imwrite('Chromaket.jpg', final)
cv2.waitKey(0)
