import csv
from datetime import datetime
from mainapp.models import Vacancy

def load_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vacancy = Vacancy(
                name=row['name'],
                key_skills=row['key_skills'] if row['key_skills'] else None,
                salary_from=float(row['salary_from']) if row['salary_from'] else None,
                salary_to=float(row['salary_to']) if row['salary_to'] else None,
                salary_currency=row['salary_currency'] if row['salary_currency'] else None,
                area_name=row['area_name'] if row['area_name'] else None,
                published_at=datetime.strptime(row['published_at'], '%Y-%m-%dT%H:%M:%S%z') if row['published_at'] else None
            )
            vacancy.save()

def run():
    csv_file_path = 'vacancies.csv'

    load_data_from_csv(csv_file_path)