# Late Show API

A Flask-based RESTful API that manages guests, episodes, and appearances on the Late Show. This project is part of the Phase 4 Code Challenge at Moringa School.

## Features

* Episodes: View all episodes or a specific episode.
* Guests: View all guests.
* Appearances: Create, update, delete, and list guest appearances on episodes.

## Endpoints

### Episodes

* GET /episodes
  Get all episodes.

* GET /episodes/<id>
  Get a single episode by ID.

### Guests

* GET /guests
  Get all guests.

### Appearances

* GET /appearances
  Get all appearances.

* POST /appearances
  Create a new appearance.
* PATCH /appearances/<id>
  Update an appearance’s rating.

## Installation & Setup

1. Clone the repository:
   git clone git@github.com:Elvis108-coder/Phase-4-Code-Challenge-Lateshow.git
   cd Phase-4-Code-Challenge-Lateshow/code-challenge
   
2. Install dependencies:
   pipenv install

3. Activate virtual environment:
   pipenv shell

4. Run migrations:
   flask db upgrade
 
5. Start the server:
   python server/app.py
## Technologies Used
* Python 3.11
* Flask
* Flask-Migrate
* SQLAlchemy
* SQLite
* Pipenv
## Author
Elvis Kiprono
Github:Elvis108-coder
email:elvis.rotich1@student.moringaschool.com
