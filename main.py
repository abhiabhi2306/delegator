from credentials import initialize_credentials
from menu import display_menu, get_user_choice, handle_menu_choice

def main():
    print(""" :::::::::  :::::::::: :::        :::::::::: ::::::::      ::: ::::::::::: ::::::::  :::::::::  
:+:    :+: :+:        :+:        :+:       :+:    :+:   :+: :+:   :+:    :+:    :+: :+:    :+: 
+:+    +:+ +:+        +:+        +:+       +:+         +:+   +:+  +:+    +:+    +:+ +:+    +:+ 
+#+    +:+ +#++:++#   +#+        +#++:++#  :#:        +#++:++#++: +#+    +#+    +:+ +#++:++#:  
+#+    +#+ +#+        +#+        +#+       +#+   +#+# +#+     +#+ +#+    +#+    +#+ +#+    +#+ 
#+#    #+# #+#        #+#        #+#       #+#    #+# #+#     #+# #+#    #+#    #+# #+#    #+# 
#########  ########## ########## ########## ########  ###     ### ###     ########  ###    ###  """)
    json_file_path = input("\n Enter the path to your service account JSON file: ")
    credentials = initialize_credentials(json_file_path)

    while True:
        display_menu()
        choice = get_user_choice()
        if not handle_menu_choice(choice, credentials):
            break

if __name__ == '__main__':
    main()
