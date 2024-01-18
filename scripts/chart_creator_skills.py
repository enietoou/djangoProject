import pandas as pd
import matplotlib.pyplot as plt
import ast


def chart_creator(csv_path, output_path):
    df = pd.read_csv(csv_path)

    # Преобразование строки с навыками из формата строки Python в структуру данных Python
    df['key_skills'] = df['key_skills'].apply(ast.literal_eval)

    # Создание графика
    plt.figure(figsize=(25, 8))

    for i, row in df.iterrows():
        year = row['year']
        key_skills = dict(row['key_skills'])

        # Сортировка навыков по убыванию
        sorted_skills = sorted(key_skills.items(), key=lambda x: x[1], reverse=True)

        # Отображение 10 самых популярных навыков для каждого года
        plt.bar([f"{skill[0]} ({year})" for skill in sorted_skills[:10]], [skill[1] for skill in sorted_skills[:10]])


    plt.title('Топ популярных навыков по годам')
    plt.xlabel('Навык (Год)')
    plt.ylabel('Количество упоминаний')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Отображение графика
    plt.show()


def main():
    chart_creator('result_files/skills/python_skill_by_year.csv',
                  'result_files/skills/python_skill_by_year.png')

if __name__ == '__main__':
    main()