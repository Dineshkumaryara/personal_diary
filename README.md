# My Diary

My Diary is a web application that allows users to create, manage, and securely store their personal diary entries. The application provides a user-friendly interface with various features to enhance the diary-keeping experience.

## Features

- **User Authentication**: Users can register, login, and logout securely.
- **Create Diary Entries**: Users can create new diary entries with titles and content.
- **View and Edit Entries**: Users can view, edit, and delete their previous entries.
- **Search Functionality**: Users can search for specific entries based on titles or content.
- **Support Messages**: Users can send support messages to the admin and view replies.
- **Responsive Design**: The application is designed to be responsive and user-friendly on all devices.

## Project Structure

- `static/`: Contains static files such as CSS, JavaScript, and images.
- `templates/`: Contains HTML templates for various pages.
- `diary/`: Contains Django app files including models, views, and forms.

## How to Run the Project

1. **Clone the repository**:
   ```sh
   https://github.com/Dineshkumaryara/personal_diary.git
   cd diary
2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
4. **Run the migrations**:
   ```sh
   python manage.py migrate
5. **Create a superuser**:
   ```sh
   python manage.py createsuperuser
6. **Run the development server**:
   ```sh
   python manage.py runserver
7. **Access the application**:
   Open a web browser and go to http://127.0.0.1:8000

## Usage
**Registration and Login**:
- Navigate to the registration page to create a new account.
- Use the login page to access your account.
**Creating and Managing Entries**:
- Use the "Create Entry" button in the sidebar to create a new diary entry.
- View your previous entries in the "History" section.
- Edit or delete existing entries as needed.
**Support Messages**:
- Use the "Support" button in the sidebar to send messages to the admin.
- View replies from the admin in the "Replies" section.
**Search Entries**:
- Use the search box beside the "History" section to search for specific entries by title or content.
**Contribution**:
- If you wish to contribute to the project, please fork the repository and submit a pull request.

## Contact
- For any inquiries or issues, please contact 2100031355cseh@gmail.com.
