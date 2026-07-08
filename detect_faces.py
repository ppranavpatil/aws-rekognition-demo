import boto3
import json

# AWS Configuration
BUCKET_NAME = "security-company-images-pranav-2026"
IMAGE_NAME = "employee.jpg"

# Create AWS clients
s3 = boto3.client("s3")
rekognition = boto3.client("rekognition")

print("Uploading image to S3...")

# Upload image to S3
s3.upload_file(
    "images/employee.jpg",
    BUCKET_NAME,
    IMAGE_NAME
)

print("Image uploaded successfully.")

print("Detecting faces...")

# Call Rekognition
response = rekognition.detect_faces(
    Image={
        "S3Object": {
            "Bucket": BUCKET_NAME,
            "Name": IMAGE_NAME
        }
    },
    Attributes=["ALL"]
)

faces = response["FaceDetails"]

print(f"Number of faces detected: {len(faces)}")

for i, face in enumerate(faces, start=1):
    print(f"Face {i} Confidence: {face['Confidence']:.2f}%")

# Save complete response
with open("result.json", "w") as file:
    json.dump(response, file, indent=4)

print("Result saved to result.json")