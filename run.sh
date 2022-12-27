
while [[ $choose != "exit" ]]; do
echo "-------------------------------"
echo -e "Select module:\n[1] Run script\n[2] Add user\n[3] List users\n[4] To do list"
        read -e -p "$(echo -ne "Choose: ")" choose

        echo "$choose"

        case $choose in
            '1' )
                bash face_recognition.sh
                ;;
            '2' )
                read -e -p "$(echo -ne "Type the new user name: ")" new_user_name
                echo -e "$new_user_name" > user/new_user_name.txt
                bash files/add.user.sh
                ;;
            '3' )
                cat files/users.txt
                echo ""
                ;;
            '4'|'exit' )
                clear
                echo "To Do"
                cat to\ do
                ;;
            * )
                echo -e "Choose options: 1/2/3/4"
            ;;
        esac
done
