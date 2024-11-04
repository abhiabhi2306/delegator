import base64
import datetime
import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up logging
logging.basicConfig(level=logging.INFO)


SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents.readonly',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/photoslibrary.readonly',
    'https://www.googleapis.com/auth/photoslibrary',
    'https://www.googleapis.com/auth/tasks.readonly',
    'https://www.googleapis.com/auth/tasks',
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/contacts.readonly',
    'https://www.googleapis.com/auth/contacts',
    'https://www.googleapis.com/auth/firebase',
    'https://www.googleapis.com/auth/fitness.activity.read',
    'https://www.googleapis.com/auth/fitness.activity.write',
    'https://www.googleapis.com/auth/fitness.body.read',
    'https://www.googleapis.com/auth/fitness.body.write',
    'https://www.googleapis.com/auth/fitness.location.read',
    'https://www.googleapis.com/auth/fitness.location.write',
    'https://www.googleapis.com/auth/forms.body.readonly',
    'https://www.googleapis.com/auth/forms.body',
    'https://www.googleapis.com/auth/keep.readonly',
    'https://www.googleapis.com/auth/keep',
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/drive.metadata',
    'https://www.googleapis.com/auth/drive.photos.readonly',
    'https://www.googleapis.com/auth/logging.admin'
]


def check_scope_access(credentials, scope):
    try:
        if 'calendar' in scope:
            service = build('calendar', 'v3', credentials=credentials)
            service.events().list(calendarId='primary', maxResults=1).execute()
        elif 'drive' in scope:
            service = build('drive', 'v3', credentials=credentials)
            service.files().list(pageSize=1).execute()
        elif 'documents' in scope:
            service = build('docs', 'v1', credentials=credentials)
            service.documents().get(documentId='1').execute()
        elif 'gmail' in scope:
            service = build('gmail', 'v1', credentials=credentials)
            service.users().messages().list(userId='me', maxResults=1).execute()
        elif 'userinfo' in scope:
            service = build('oauth2', 'v2', credentials=credentials)
            service.userinfo().get().execute()
        elif 'spreadsheets' in scope:
            service = build('sheets', 'v4', credentials=credentials)
            service.spreadsheets().get(spreadsheetId='1').execute()
        elif 'youtube' in scope:
            service = build('youtube', 'v3', credentials=credentials)
            service.channels().list(part='snippet', mine=True).execute()
        elif 'photoslibrary' in scope:
            service = build('photoslibrary', 'v1', credentials=credentials)
            service.albums().list(pageSize=1).execute()
        elif 'tasks' in scope:
            service = build('tasks', 'v1', credentials=credentials)
            service.tasklists().list(maxResults=1).execute()
        elif 'cloud-platform' in scope:
            service = build('cloudresourcemanager', 'v1', credentials=credentials)
            service.projects().list(pageSize=1).execute()
        elif 'contacts' in scope:
            service = build('people', 'v1', credentials=credentials)
            service.contactGroups().list(pageSize=1).execute()
        elif 'firebase' in scope:
            service = build('firebase', 'v1beta1', credentials=credentials)
            service.projects().list(pageSize=1).execute()
        elif 'fitness' in scope:
            service = build('fitness', 'v1', credentials=credentials)
            service.users().dataSources().list(userId='me').execute()
        elif 'forms' in scope:
            service = build('forms', 'v1', credentials=credentials)
            service.forms().get(formId='1').execute()
        elif 'keep' in scope:
            service = build('keep', 'v1', credentials=credentials)
            service.notes().list(pageSize=1).execute()
        elif 'drive.metadata' in scope:
            service = build('drive', 'v3', credentials=credentials)
            service.files().list(fields="files(id)").execute()

        print(f"Access granted for scope: {scope}")
        return True
    except Exception as e:
        print(f"Access denied for scope: {scope} - {str(e)}")
        return False

def brute_force_scopes(credentials):
    accessible_scopes = []

    # Check each scope for access
    for scope in SCOPES:
        if check_scope_access(credentials, scope):
            accessible_scopes.append(scope)

    if not accessible_scopes:
        print('No accessible scopes found.')
    else:
        print('Accessible scopes:')
        for scope in accessible_scopes:
            print(scope)
        print("\n")


def get_calendar_events(credentials, event_count=None):
    """Fetch upcoming events from Google Calendar."""
    service = build('calendar', 'v3', credentials=credentials)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()  
    logging.info('Getting the upcoming events')

    events_result = service.events().list(
        calendarId='primary', timeMin=now, maxResults=event_count, singleEvents=True,
        orderBy='startTime').execute()

    events = events_result.get('items', [])
    if not events:
        logging.info('No upcoming events found.')
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            logging.info(f"Start Time: {start}, Summary: {event.get('summary', 'No summary')}, Description: {event.get('description', 'No description')}")

def get_document_content(credentials, document_ids):
    """Fetch content from Google Docs."""
    service = build('docs', 'v1', credentials=credentials)

    for document_id in document_ids:
        try:
            document = service.documents().get(documentId=document_id).execute()
            logging.info(f"Document ID: {document_id}, Title: {document.get('title')}")
            for element in document.get('body').get('content'):
                if 'paragraph' in element:
                    for text_element in element['paragraph']['elements']:
                        if 'textRun' in text_element:
                            print(text_element['textRun']['content'], end='')
        except Exception as e:
            logging.error(f"Failed to fetch document with ID {document_id}: {e}")

def list_drive_files(credentials):
    """List files in Google Drive."""
    service = build('drive', 'v3', credentials=credentials)
    logging.info("Files in Google Drive:")
    
    try:
        results = service.files().list(
            pageSize=10,
            fields="nextPageToken, files(id, name)"
        ).execute()
        items = results.get('files', [])

        if not items:
            logging.info('No files found.')
        else:
            for item in items:
                logging.info(f"{item['name']} ({item['id']})")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def get_gmail_messages(credentials, max_results=10):
    """Fetch messages from Gmail."""
    service = build('gmail', 'v1', credentials=credentials)

    logging.info('Getting the latest emails')

    try:
        results = service.users().messages().list(userId='me', maxResults=max_results).execute()
        messages = results.get('messages', [])

        if not messages:
            logging.info('No messages found.')
        else:
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                payload = msg['payload']
                headers = payload['headers']
                
                subject = next(header['value'] for header in headers if header['name'] == 'Subject')
                from_email = next(header['value'] for header in headers if header['name'] == 'From')
                date = next(header['value'] for header in headers if header['name'] == 'Date')

                logging.info(f"From: {from_email}, Subject: {subject}, Date: {date}")

                parts = payload.get('parts', [])
                for part in parts:
                    if part['mimeType'] == 'text/plain':
                        data = part['body'].get('data')
                        if data:
                            decoded_data = base64.urlsafe_b64decode(data).decode('utf-8')
                            logging.info(f"Message: {decoded_data}")
                            break
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def get_spreadsheet_content(credentials, spreadsheet_ids):
    """Fetch content from Google Sheets."""
    service = build('sheets', 'v4', credentials=credentials)

    for spreadsheet_id in spreadsheet_ids:
        try:
            spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
            logging.info(f"Spreadsheet ID: {spreadsheet_id}, Title: {spreadsheet.get('properties').get('title')}")
            sheets = spreadsheet.get('sheets')
            for sheet in sheets:
                logging.info(f"Sheet Name: {sheet.get('properties').get('title')}")
                data = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=sheet.get('properties').get('title')).execute()
                values = data.get('values', [])
                for row in values:
                    print('\t'.join(row))
        except Exception as e:
            logging.error(f"Failed to fetch spreadsheet with ID {spreadsheet_id}: {e}")

