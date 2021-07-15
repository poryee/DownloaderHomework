import os
import pytest
import uuid


@pytest.fixture(scope='session')
def url_file(test_urls):
    url_file_name = str(uuid.uuid4())

    # simulate url given in file
    with open(url_file_name, 'w') as f:
        for url in test_urls:
            f.write(url + '\n')

    yield os.path.abspath(url_file_name)
    # at the end of test remove tmp url file
    os.remove(url_file_name)


@pytest.fixture(scope='session')
def test_urls(http_url, ftp_url, https_url, sftp_url):
    return [http_url, ftp_url, https_url, sftp_url]


@pytest.fixture(scope='session')
def http_url():
    return 'http://speedtest.ftp.otenet.gr/files/test100k.db'

@pytest.fixture(scope='session')
def https_url():
    return 'https://www.wikihow.com/images/f/fc/Convert-JPG-to-PNG-Step-20.jpg'

@pytest.fixture(scope='session')
def ftp_url():
    return 'ftp://speedtest:speedtest@ftp.otenet.gr/test10Mb.db'

@pytest.fixture(scope='session')
def sftp_url():
    return 'sftp://demo:password@test.rebex.net:22/readme.txt'