from google_services import (
    get_calendar_events,
    get_document_content,
    list_drive_files,
    get_gmail_messages,
    get_spreadsheet_content,
    brute_force_scopes
)

def display_menu():
    print("\nMenu:")
    print("1. Get Upcoming Calendar Events")
    print("2. Get Document Content from Google Docs")
    print("3. List Files from Google Drive")
    print("4. Get Gmail Messages")
    print("5. Get Content from Google Sheets")
    print("6. Brute Force Accessible Scopes")
    print("7. Exit")

def get_user_choice():
    return input("Choose an option (1-7): ")

def handle_menu_choice(choice, credentials):
    if choice == '1':
        event_count = int(input("Enter the number of events to retrieve (or 0 for all): "))
        get_calendar_events(credentials, event_count if event_count > 0 else None)
    elif choice == '2':
        document_ids = input("Enter document IDs separated by commas: ").split(',')
        document_ids = [doc_id.strip() for doc_id in document_ids]
        get_document_content(credentials, document_ids)
    elif choice == '3':
        list_drive_files(credentials)
    elif choice == '4':
        max_results = int(input("Enter the number of emails to retrieve: "))
        get_gmail_messages(credentials, max_results)
    elif choice == '5':
        spreadsheet_ids = input("Enter spreadsheet IDs separated by commas: ").split(',')
        spreadsheet_ids = [sheet_id.strip() for sheet_id in spreadsheet_ids]
        get_spreadsheet_content(credentials, spreadsheet_ids)
    elif choice == '6':
        brute_force_scopes(credentials)
    elif choice == '7':
        print("Exiting...")
        return False
    else:
        print("Invalid option. Please try again.")
    return True
