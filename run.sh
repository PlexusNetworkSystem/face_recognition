
while [[ $choose != "exit" ]]; do
echo "-------------------------------"
echo -e "Select module:\n[1] Run script\n[2] Add user\n[3] To do list"
        read -e -p "$(echo -ne "Choose: ")" choose

        echo "$choose"

        case $choose in
           '1' )
                bash face_recognition.sh
                ;;
            '2' )
                read -e -p "$(echo -ne "Type the new user name: ")" new_user_name
                echo -e "$new_user_name" > user/new_user_name.txt
                bash files/add.user_encodings.sh
                ;;
              '3'|'exit' )
                clear
                echo "To Do"
                cat to\ do
                ;;
            * )
                echo -e "Choose options: 1/2"
            ;;
        esac
done
