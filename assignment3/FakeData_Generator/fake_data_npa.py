import csv
import random
from time import time
from decimal import Decimal
from faker import Faker

RECORD_COUNT_TRAIN = 1000
RECORD_COUNT_VALID = 100
CANDIDATE_SIZE = 3
fake = Faker()

# use this mapping to map properties into CNN wordembedding (no need for fakedata)
propertyMapping = ['Authentic', 'Japanese', 'beautifully', 'tasty', 'organic',
                   'gluten-free', 'GMO-free', 'all-natural', 'artificial-ingredient-free',
                   'classic', 'trendy', 'healthy']


def create_train_file():
    with open('../Fake_Data/snack_npa_train.csv', 'w', newline='') as csvfile:
        # in order to use the same Embedding binary data used by CNN model, we set the
        # fieldname to still be 'candidateNews' and 'clickedNews'.Even through it is better
        # to be named as 'candiateProperty' and 'clickedProperty' for snacks.
        fieldnames = ['id', 'ImpressionID',
                      'User', 'CandidateNews', 'ClickedNews']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT_TRAIN):
            candidateNews = []
            clickedNews = []
            for j in range(CANDIDATE_SIZE):
                candidateNews.append(fake.random_int(
                    min=1, max=(len(propertyMapping) - 1)))
                clickedNews.append(fake.random_int(
                    min=1, max=(len(propertyMapping) - 1)))
            writer.writerow(
                {
                    'id': i,
                    'ImpressionID': fake.random_int(min=1, max=100),
                    'User': fake.random_int(min=1, max=1000),
                    'CandidateNews': candidateNews,
                    'ClickedNews': clickedNews,
                }
            )


def create_valid_file():
    with open('../Fake_Data/snack_npa_valid.csv', 'w', newline='') as csvfile:
        # in order to use the same Embedding binary data used by CNN model, we set the
        # fieldname to still be 'candidateNews' and 'clickedNews'.Even through it is better
        # to be named as 'candiateProperty' and 'clickedProperty' for snacks.
        fieldnames = ['id', 'ImpressionID',
                      'User', 'CandidateNews', 'ClickedNews']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT_VALID):
            candidateNews = []
            clickedNews = []
            for j in range(CANDIDATE_SIZE):
                candidateNews.append(fake.random_int(
                    min=1, max=(len(propertyMapping) - 1)))
                clickedNews.append(fake.random_int(
                    min=1, max=(len(propertyMapping) - 1)))
            writer.writerow(
                {
                    'id': i,
                    'ImpressionID': fake.random_int(min=1, max=100),
                    'User': fake.random_int(min=1, max=1000),
                    'CandidateNews': candidateNews,
                    'ClickedNews': clickedNews,
                }
            )


if __name__ == '__main__':
    start = time()
    create_train_file()
    elapsed = time() - start
    print('created train file time: {}'.format(elapsed))

    start = time()
    create_valid_file()
    elapsed = time() - start
    print('created valid file time: {}'.format(elapsed))
