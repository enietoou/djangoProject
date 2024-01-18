import pandas as pd

profession_names = ['Python-программист', 'Python-разработчик',
                    'Пайтон-программист', 'Пайтон-разработчик',
                    'Пайтон-программист', 'Пайтон-разработчик',
                    'Разработчик на Python', 'Python-инженер',
                    'Программист Python', 'Python-специалист'
                    'Разработчик Python-приложений', 'Python-девелопер'
                    'Python-кодер']

def filter_csv(csv_file: str, output_file: str):
    dtype_mapping = {'name': str, 'key_skills': str, 'salary_from': float, 'salary_to': float, 'salary_currency': str,
                     'area_name': str, 'published_at': str}

    df = pd.read_csv(csv_file, dtype=dtype_mapping)

    filtered_df = df[df['name'].str.contains('|'.join(profession_names), case=False, regex=True)]

    filtered_df.to_csv(output_file, index=False)


def main():
    csv_file_path = 'vacancies.csv'
    csv_output = 'python_vacancies.csv'
    filter_csv(csv_file_path, csv_output)

if __name__ == '__main__':
    main()