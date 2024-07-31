# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
import requests

FILE_TYPES_MIME_MAPPING = {
    'csv': 'application/csv',
    'txt': 'text/plain',
    'log': 'text/plain',
    'xls': 'application/vnd.ms-excel',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'zip': 'application/zip'
}


def determine_file_mime_type(file_name):
    if file_name.endswith(".csv"):
        return FILE_TYPES_MIME_MAPPING['csv']
    elif file_name.endswith(".txt"):
        return FILE_TYPES_MIME_MAPPING['txt']
    elif file_name.endswith(".log"):
        return FILE_TYPES_MIME_MAPPING['log']
    elif file_name.endswith(".xls"):
        return FILE_TYPES_MIME_MAPPING['xls']
    elif file_name.endswith(".xlsx"):
        return FILE_TYPES_MIME_MAPPING['xlsx']
    elif file_name.endswith(".zip"):
        return FILE_TYPES_MIME_MAPPING['zip']
    raise ValueError("No MIME type available")


class Email:
    def __init__(self, app):
        self.app = app
        secrets = app.config['SECRETS']
        self.url = secrets['NODE_NOTIFICATION_BASE_URL']
        self.NOTIFICATION_EMAIL_FILE_POSTFIX_URL = "api/v1/queueing-notification/send-mail"
        self.auth_token = secrets['NOTIFICATION_AUTH_TOKEN']
        self.logger = self.app.logger

    def send_email_file(self, subject, mail_body, emails_to, file_paths=None, file_uris=None):
        multiple_files = list()
        url = self.url + self.NOTIFICATION_EMAIL_FILE_POSTFIX_URL
        headers = {'Authorization': self.auth_token}

        if isinstance(emails_to, list):
            emails_to = ','.join(email_id for email_id in emails_to)

        data = {
            'subject': subject,
            'body': mail_body,
            'to_emails': emails_to,
            'from_email': 'tech@generico.in',
            'is_html': 'false',
        }
        for file_path in (file_paths or []):
            file_name = file_path.split('/')[::-1][0]
            mime_type = determine_file_mime_type(file_name)
            multiple_files.append(('file', (file_name, open(file_path, 'rb'), mime_type)))

        """ to send s3 files as email attachment """
        # for file_uri in (file_uris or []):
        #     file_name = file_uri.split('/')[-1]
        #     mime_type = determine_file_mime_type(file_name)
        #     file_bytes = self.s3.get_file_object(uri=file_uri)
        #     multiple_files.append(('file', (file_name, file_bytes, mime_type)))

        response = requests.post(url, data=data, files=multiple_files, headers=headers, timeout=(1, 60))
        response_data = response.json()
        if response.status_code != 200:
            raise Exception(f"Email sending failed: {response.text}")
        else:
            if response_data["is_error"]:
                raise Exception(f"Email sending failed, error message: {response_data['message']}")
            self.logger.info(f"Email sending successful: {response.text}")
