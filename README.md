# Campus Connect

Campus Connect is a web application designed to facilitate interaction among college students. It enables users to ask and answer college-related questions, fostering a collaborative learning environment. The project is built using **Django** for both the backend and frontend, utilizing HTML for rendering pages.

## Screenshots
**Login page**
![Screenshot 2025-04-03 105131](https://github.com/user-attachments/assets/43494767-ebb5-4ed0-b870-22cd6a46282e)

**Home page**

![Screenshot 2025-04-03 105215](https://github.com/user-attachments/assets/62f1156e-e9f4-4ec3-bc37-b4b829649ff6)

**User profile**
![Screenshot 2025-04-03 105243](https://github.com/user-attachments/assets/9b09a557-453c-4456-941a-ceee4bce62b9)

**Announcement page**

![Screenshot 2025-04-03 105253](https://github.com/user-attachments/assets/3589eb7b-495d-469a-b473-bf2738c5d940)



## Features
- **User Authentication**: Users can sign up, log in, and reset their passwords.
- **Post Questions**: Users can ask college-related questions.
- **Upvote/Downvote Questions**: Users can upvote and downvote other questions.
- **Answer Questions**: Other users can respond to the posted questions
- **Logout Functionality**: Ensures secure session handling.
- **Report Functionality**: Users can report inappropriate content.
- **Announcement Tab**: Admins can post important updates and announcements.
- **Improved UI**: A user-friendly interface for smooth interaction.

## Tech Stack
- **Backend & Frontend**: Django
- **Database**: SQLite 
- **Authentication**: Django’s built-in authentication system
- **Styling**: CSS 

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/vaibhavRaj7667/sem_project
   cd campus-connect
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the Django server:
   ```sh
   python manage.py runserver
   ```

## Usage
1. Register or log in to your account.
2. Post your questions related to college life.
3. Browse and answer questions from other students.
4. Report inappropriate content if necessary.
5. Stay updated with college announcements.

## Contribution
Contributions are welcome! If you’d like to improve the project:
1. Fork the repository.
2. Create a new branch (`feature-xyz`).
3. Make your changes and commit them.
4. Push to your fork and create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, feel free to reach out at **zivaibhav1@gamil.com**.

