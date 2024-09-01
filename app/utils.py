# utils.py
from sqlalchemy.orm import Session
from app.crud import update_translation_task
from app.database import SessionLocal  
from dotenv import load_dotenv
import openai
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def perform_translation(task_id: int, text: str, languages: list, db: Session):
    translations = {}
    
    try:
        for lang in languages:
            try:
                response = openai.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {"role": "system", "content": f"You are a helpful assistant who translates text into {lang}."},
                        {"role": "user", "content": text}
                    ]
                )
                translated_text = response.choices[0].message.content.strip()
                translations[lang] = translated_text
            except Exception as e:
                print(f"Error translating to {lang}: {e}")
                translations[lang] = f"Error: {e}"

        update_translation_task(db, task_id, translations)

    except Exception as e:
        print(f"Error updating task {task_id} with translations: {e}")

    finally:
        db.close()
