from pathlib import Path

import pandas as pd

from src.reporter import DataFrameReporter

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'data' / 'payments.csv'


def main():
    data = pd.read_csv(DATA_PATH)

    reporter = DataFrameReporter(
        float_format='0.05f',
        percent_format='0.02%',
        include_all=True,
    )

    reporter.show_report(data, 'Отчёт по датафрейму payments:')


if __name__ == '__main__':
    main()