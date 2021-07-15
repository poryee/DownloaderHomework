import pytest

from downloader.download_factory import DownloaderFactory
from downloader.ftp_downloader import FtpDownloader
from downloader.http_downloader import HttpDownloader
from downloader.sftp_downloader import SftpDownloader


@pytest.mark.parametrize('input_url, expected', [
    ('ftp://speedtest.tele2.net/1MB.zip', FtpDownloader),
    ('http://user:password@speedtest.com/dir/file2.txt', HttpDownloader),
    ('sftp://user:password@speedtest.com:8820/dir/file3.txt', SftpDownloader),
])
def test_downloaderFactory(input_url, expected):
    return_downloader = DownloaderFactory.getDownloader(input_url)
    assert return_downloader == expected


def test_downloader_factory_unsupport_url():
    with pytest.raises(NotImplementedError):
        DownloaderFactory.getDownloader('invalid://protocol')

