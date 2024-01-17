import csv
from datetime import datetime
from mainapp.models import CurrencyRate

def load_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Преобразование данных и сохранение в базе данных
            date = datetime.strptime(row['date'], '%Y-%m')
            rate = CurrencyRate(
                date=date,
                BYR=float(row['BYR']) if row['BYR'] else None,
                USD=float(row['USD']) if row['USD'] else None,
                EUR=float(row['EUR']) if row['EUR'] else None,
                KZT=float(row['KZT']) if row['KZT'] else None,
                UAH=float(row['UAH']) if row['UAH'] else None,
                AZN=float(row['AZN']) if row['AZN'] else None,
                KGS=float(row['KGS']) if row['KGS'] else None,
                UZS=float(row['UZS']) if row['UZS'] else None,
                GEL=float(row['GEL']) if row['GEL'] else None,
            )
            rate.save()

def run():
    csv_file_path = 'currency.csv'

    load_data_from_csv(csv_file_path)