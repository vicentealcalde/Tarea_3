import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.books.models import Author, Book, Rating  # Ajusta la importación según la ubicación real de tus modelos
from pathlib import Path

# Configura la conexión a la base de datos
usuario = "postgres"  # Valor de POSTGRES_USER
contraseña = "postgres"  # Valor de POSTGRES_PASSWORD
host = "db"  # Nombre de servicio
nombre_de_la_db = "postgres"  # Nombre de la base de datos

DATABASE_URL = f"postgresql://{usuario}:{contraseña}@{host}/{nombre_de_la_db}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Ruta a los archivos CSV
csv_folder = Path("database_files")

def load_authors():
    with open(csv_folder / "authors.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            author = Author(name=row["name"], openlibrary_key=row["key"])
            session.add(author)
    session.commit()

def load_books():
    with open(csv_folder / "books.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            author = session.query(Author).filter_by(openlibrary_key=row["author"]).first()
            book = Book(
                title=row["title"],
                openlibrary_key=row["key"],
                author=author,
                description=row["description"]
            )
            session.add(book)
    session.commit()

def load_ratings():
    with open(csv_folder / "ratings.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            book = session.query(Book).filter_by(openlibrary_key=row["work"]).first()
            rating = Rating(book=book, score=row["score"])
            session.add(rating)
    session.commit()

if __name__ == "__main__":
    load_authors()
    load_books()
    load_ratings()
