# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("pictures/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("pictures/biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

abra_image = face_recognition.load_image_file("pictures/abra.jpg")
abra_face_encoding = face_recognition.face_encodings(abra_image)[0]
