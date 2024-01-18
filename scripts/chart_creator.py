import pandas as pd
import matplotlib.pyplot as plt


def chart_creator(csv_path, output_path):
    df = pd.read_csv(csv_path)
    plt.figure(figsize=(15, 6))
    plt.plot(df['area_name'], df['percent'], marker='o', linestyle='-', color='b')
    plt.title('Доля вакансий по городам Python-программист')
    plt.xlabel('Город')
    plt.ylabel('Доля вакансий (%)')
    plt.grid(True)
    plt.show()


def main():
    chart_creator('result_files/geography/python_vacs_by_city.csv',
                  'result_files/geography/python_vacs_by_city.png')

if __name__ == '__main__':
    main()