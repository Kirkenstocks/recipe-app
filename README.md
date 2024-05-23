# Recipe App

## Link to Live Site

## Overview
The Recipe App is a full-stack web application built with the Django framework that allows users to store recipes for future reference or to peruse recipes uploaded by others to find their next great meal!
This app was developed to grow my understanding of full-stack web application development, specifically with Python and Django, and includes core features of web development such as user authentication, dynamic content creation, and data visualization.

## Key Features and Functionality
- User authentication and authorization
- Users can add, modify, and delete recipes in a SQLite database
- Difficulty rating for each recipe is automatically calculated
- Recipe search by name, ingredient, and cooking time
- Recipes summarized in cards, with more details available upon clicking a card
- Data visualization with users able to choose from 3 chart options with different statistical analyses
- Error handling for invalid user inputs

## Getting Started
1. **Clone repository**
```bash
git clone https://github.com/Kirkenstocks/recipe-app.git
```
2. **Navigate to root directory**
```bash
cd recipe-app
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Configure database**
- In settings.py, make any necessary adjustments to the SQLite database for your environments.
5. **Navigate to src folder and run database migrations**
```bash
cd src
python manage.py makemigrations
python manage.py migrate
```
6. **Create superuser**
```bash
python manage.py createsuperuser
```
7. **Start a local server**
```bash
python manage.py runserver
```
8. **Open app in browser**
- Navigate to http://127.0.0.1:8000 or http://localhost:8000/ in your browser.

## Credits
This project was built for the CareerFoundry Full-Stack Web Development program, with their instruction essential to its completion.

## License
This project is open source and available under the MIT License.