import cv2

# Load image
image_path = r"D:\live coding\Python file\Face.png"
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Image not found at {image_path}")
    exit()

print("Image loaded successfully!")

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces
faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Save output image instead of showing it
output_path = r"D:\live coding\Python file\output.png"
cv2.imwrite(output_path, image)
print(f"Output saved as {output_path}")
