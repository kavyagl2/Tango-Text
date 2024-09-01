# Tango Text

**Tagline:** Twirl Through Languages with Ease!

Tango Text is a sleek and interactive web application that offers real-time language translation. Powered by OpenAI's GPT-4-turbo, Tango Text allows users to translate text into multiple languages with ease and provides the ability to search for translation tasks by their ID.

## Features

- **Real-Time Translation:** Submit text and receive translations into multiple languages.
- **Task Tracking:** Check the status of translation tasks and view results once completed.
- **Search Functionality:** Retrieve translations by task ID.
- **Interactive UI:** User-friendly interface with a stylish and functional design.

## Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** FastAPI
- **Database:** SQLAlchemy with PostGres
- **Translation Service:** OpenAI GPT-4-turbo

## Installation

### Prerequisites

- Python 3.8 or higher
- Poetry (for dependency management)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/tango-text.git
   cd tango-text
   ```

2. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following:
   ```ini
   DATABASE_URL=sqlite:///./test.db
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the application:**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

   The application will be accessible at `http://localhost:8000`.

## Directory Structure

```
tango-text/
│
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── utils.py
│   └── templates/
│       └── index.html
│
├── .env
├── poetry.lock
├── pyproject.toml
└── README.md
```

## API Endpoints

- **POST /translate:** Submits a translation request.
- **GET /translate/{task_id}:** Retrieves the status of a translation task.
- **GET /search:** Searches for a translation by task ID.

## Frontend

- **index.html** - The main HTML file containing the user interface for text translation and search functionalities.
