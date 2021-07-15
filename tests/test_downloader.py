import pytest
import os

from downloader.cli import getOutputDir
from downloader.download_helper import DownloadHelper


@pytest.mark.parametrize('url, expected_file_name', [(["http://speedtest.ftp.otenet.gr/files/test100k.db"], "test100k.db")])
def test_downloadHttp(url, expected_file_name):
    output_directory = getOutputDir('/downloads')
    local_file_name = DownloadHelper(url, output_directory).process()
    expected = os.path.join(output_directory,expected_file_name)

    assert local_file_name == expected
    # clean up test
    os.remove(expected)

@pytest.mark.parametrize('url, expected_file_name', [(["https://www.gardeningknowhow.com/wp-content/uploads/2019/08/flower-color.jpg"], "flower-color.jpg")])
def test_downloadHttps(url, expected_file_name):
    output_directory = getOutputDir('/downloads')
    local_file_name = DownloadHelper(url, output_directory).process()
    expected = os.path.join(output_directory,expected_file_name)

    assert local_file_name == expected
    # clean up test
    os.remove(expected)

# bigger file
@pytest.mark.parametrize('url, expected_file_name',[(['ftp://speedtest:speedtest@ftp.otenet.gr/test10Mb.db'],'test10Mb.db')])
def test_download_ftp(url, expected_file_name):
    output_directory = getOutputDir('/downloads')
    local_file_name = DownloadHelper(url, output_directory).process()
    expected = os.path.join(output_directory,expected_file_name)

    assert local_file_name == expected
    # clean up test
    os.remove(expected)

@pytest.mark.parametrize('url, expected_file_name', [(['sftp://demo:password@test.rebex.net:22/readme.txt'],'readme.txt')])
def test_download_sftp(url, expected_file_name):
    output_directory = getOutputDir('/downloads')
    local_file_name = DownloadHelper(url, output_directory).process()
    expected = os.path.join(output_directory,expected_file_name)

    assert local_file_name == expected
    # clean up test
    os.remove(expected)
