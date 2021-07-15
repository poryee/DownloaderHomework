from urllib.parse import urlparse

from downloader.ftp_downloader import FtpDownloader
from downloader.http_downloader import HttpDownloader
from downloader.sftp_downloader import SftpDownloader


class DownloaderFactory(object):
    @staticmethod
    def getDownloader(url):
        parsed_url = urlparse(url)
        protocol = parsed_url.scheme
        if protocol == "http":
            return HttpDownloader
        elif protocol == "https":
            return HttpDownloader
        elif protocol == "ftp":
            return FtpDownloader
        elif protocol == "sftp":
            return SftpDownloader
        else:
            raise NotImplementedError('No {0} downloader'.format(protocol))
