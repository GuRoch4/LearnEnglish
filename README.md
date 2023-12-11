# CS50 Learning English

#### Description:

Hello, my name is Gustavo, and I'd like to present my CS50 project called "CS50 Learning English." This project is a web-based application created using JavaScript, Python (Flask), SQL, HTML, and CSS.

*This site is like a word game where you choose a topic and receive a series of English words to translate into Portuguese. It's a practical, interactive way to practice your translation skills while having fun. You can explore different topics, challenging yourself to find the best Portuguese matches for English words. It's a good way to learn and improve your language skills while having fun!*


### Key Features:

- Database with 10 themes and approximately 80 words per theme, focusing on commonly used words.
- Consists of three simple pages:
  1. Theme selection.
  2. Word translation.
  3. Feedback page: Informs users about their mistakes, provides correct translations, and offers a button to restart the game by returning to the theme selection.

### Technologies Used:

- JavaScript
- Python (Flask)
- SQL
- HTML
- CSS

### Project Structure:

#### app.py

This file contains the main Flask application with the following functionalities:
- Establishing connections to the SQLite database.
- Rendering the initial page with theme options.
- Redirecting to the game page based on the chosen theme.
- Handling the game logic, including selecting a random word for translation and verifying user input.
- Restarting the game in case of an incorrect translation.

### templates folder

#### index.html
- The initial page that displays theme options retrieved from the database.
- Allows users to choose a theme for the game.

#### jogo.html
- Represents the game page where users are prompted to translate a word from English to Portuguese.
- Includes a form for user input and displays the current score.

#### recomecar.html
- A page that appears when the user provides an incorrect translation.
- Offers the option to restart the game and displays the final score.

#### layout.html
- Template file containing the overall structure of the web pages.
- Includes common HTML elements, CSS styles, and scripts used across different pages.

### Research Involved:

I conducted research to identify commonly used English words for different themes. The focus was on providing a set of simpler words for users to memorize, as repetition aids learning.

### Learning Experience:

This project helped me acquire new skills, particularly in Flask. While I am familiar with Python for data handling, working with Flask for web development was a challenge that allowed me to expand my knowledge.

### Project Authorship:

This project was developed solely by Gustavo Henrique Rocha.

---

Thank you for checking out my CS50 Learning English project!
