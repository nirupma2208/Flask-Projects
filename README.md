# Flask Notes Application

## Project Overview

This project is a simple web application built using Python and Flask. It allows users to create an account, log in, and manage their personal notes. Users can add, view, and delete notes in a secure environment, with data stored in a MySQL database.

### Key Features:
- **User Authentication**: Users can sign up and log in using their email and password.
- **Note Management**: Users can add new notes, view existing notes, and read details of specific notes.
- **Persistent Data Storage**: Notes and user information are stored in a MySQL database using SQLAlchemy for easy management and retrieval.
- **Session Management**: User login is managed via cookies to maintain session across requests.

---

## Project Structure

- **FlaskUser Class**: Represents the user of the application. Each user has a name, email (unique), and password stored securely in the database.
- **Notes Class**: Represents the notes created by users. Each note is associated with an email, title, content, and timestamp.
- **Routes**:
    - `/`: Redirects based on user authentication (home or login).
    - `/login`: Allows users to log in with email and password.
    - `/signup`: Allows new users to create an account.
    - `/home`: Displays the user's notes.
    - `/topicadd`: Adds a new note to the user's account.
    - `/shownotes`: Displays detailed content for a specific note.
    - `/logout`: Logs the user out and clears the session.

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <project_directory>
