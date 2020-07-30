import csv
import random
from time import time
from decimal import Decimal
from faker import Faker

RECORD_COUNT = 1000
fake = Faker()


def create_csv_file():
    with open('../Fake_Data/snack_ncf_fake.csv', 'w', newline='') as csvfile:
        fieldnames = ['userID', 'itemID', 'rating', 'timestamp', 'products']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        products = (
            'Snakku',
            'Love With Food',
            'Candy Club',
            'NatureBox',
            'SnackNation',
            'ZenPop',
            'Yummy Bazaar World Sampler',
            'FitSnack',
            'Bokksu',
            'MunchPak',
            'Universal Yums',
            'Vegan Cuts Snack Box',
            'TokyoTreat',
            'Try the World Snacks'
        )

        writer.writeheader()
        for i in range(RECORD_COUNT):
            itemIndex = fake.random_int(min=0, max=13)
            writer.writerow(
                {
                    'userID': fake.random_int(min=1, max=100),
                    'itemID': itemIndex,
                    'rating': fake.random_int(min=1, max=10),
                    'timestamp': fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None),
                    'products': products[itemIndex],
                }
            )


if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file time: {}'.format(elapsed))
