# read user name from file
user_name="$(cat user/new_user_name.txt)"

# add encode (known_face_encodings.py)
add_user_encode="${user_name// /_}_face_encoding,\n    abra_face_encoding"
user_encod=$(cat "files/known_face_encodings.py" | sed -r "s#abra_face_encoding#$add_user_encode#g");



# add name (known_face_names.py)
add_user_name=$(cat "files/known_face_names.py" | sed -r "s#\"Abra AURORA\"#\"$user_name\",\n    \"Abra AURORA\"#g")


echo -e "Choose an image"
image_dir="$(zenity --file-selection --file-filter='Image files (jpg,png,jpeg) | *.jpg *.jpeg *.png' --file-filter='All files | *')"
echo -e "image dir: $image_dir"

# add user (users.py)
change="${user_name// /_}_image = face_recognition.load_image_file(\"$image_dir\")
${user_name// /_}_face_encoding = face_recognition.face_encodings(${user_name// /_}_image)[0]"

if [[ -f $image_dir ]]; then

    echo -e "$user_encod" > files/known_face_encodings.py
    echo -e "$add_user_name" > files/known_face_names.py
    echo -e "\n$change" >> files/users.py
    echo -e "$user_name" >> files/users.txt

:
else
    echo -e "User add proc is aborted"
:
fi