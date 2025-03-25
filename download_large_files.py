import owncloud
import os
from os.path import join

def download_data(path = 'data') -> None:
    if not os.path.exists(path):
        print('Creating directory for data')
        os.mkdir(path)
        if not os.path.exists(join(path, 'ses-715093703')):
            os.mkdir('data/ses-715093703')
        if not os.path.exists(join(path, 'meta_data')):
            os.mkdir('data/meta_data')

    if not os.path.exists(join(path,'ses-715093703/units.parquet')):
        print('Downloading units data')
        owncloud.Client.from_public_link('https://uni-bonn.sciebo.de/s/y9FtA26NOUxVeTt').get_file('/', join(path, 'ses-715093703/units.parquet'))
        print('Downloading units data finished')
    else:
        print('Session units data already downloaded')

    if not os.path.exists(join(path,'meta_data/units.csv')):
        print('Downloading meta data')
        owncloud.Client.from_public_link('https://uni-bonn.sciebo.de/s/UUpOWgX8Chep9cZ').get_file('/', join(path, 'meta_data/units.csv'))
        print('Downloading meta data finished')
    else:
        print('Units meta data already downloaded')


if  __name__ == '__main__':
    download_data('data')