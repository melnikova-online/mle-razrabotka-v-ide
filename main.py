import pandas as pd

from src.reporter import DataFrameReporter


def main():
    data = pd.read_csv('data/payments.csv')

    reporter = DataFrameReporter(
        float_format='0.05f',
        percent_format='0.02%',
        include_all=True,
    )

    reporter.show_report(data, 'Отчёт по датафрейму payments:')


if __name__ == '__main__':
    main()