# Recipe App

### Description

This is the recipe web application built with Django framework. This application includes an admin panel for data handling and visualization.
User can create recipes and a difficulty parameter automatically calculated by the application. Also, they can search
for recipes by difficulty.

### Features

- User Authentication: Allow for user authentication, login, and logout.
- Search Functionality: Let users search for recipes according to difficulty.
- Difficulty Level: Automatically calculate difficulty level according to the number of ingredients and cooking time.
- Data Visualization: Visualize recipe trends and statistics for better insights and decision-making.
- Error Handling: Ensure smooth user experience through comprehensive error handling and validation mechanisms.
- Database Integration: Seamlessly integrate with SQLite database for efficient data storage and retrieval.
- Admin Dashboard: Utilize Django Admin dashboard for easy management of recipe data.

### Tech Stack

- Python
- Django
- SQLite
- HTML/CSS
- Heroku

### Installation

1. Clone the repository:

git clone <https://github.com/nozomis0129/recipe-app>

cd recipe-app

2. Create and activate a virtual environment:

python -m venv venv

source venv/bin/activate

3. Install the dependencies:

pip install -r requirements.txt

4. Apply database migrations:

python manage.py migrate

5. Run the development server:

python manage.py runserver
