# add encodings  (known_face_encodings)
# read user name from a  file
add_name="$(cat user/new_user_name.txt)_face_encoding,\n    abra_face_encoding"

user_encod=$(cat "files/known_face_encodings.py" | sed -r "s#abra_face_encoding#$add_name#g");

echo -e "$user_encod" > files/known_face_encodings.py

# add names (known_face_names)
