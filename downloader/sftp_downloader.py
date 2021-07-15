import os
from urllib.parse import urlparse
import paramiko
import shutil


class SftpDownloader():

    def __init__(self, url, downloaded_dir):
        self._file_downloaded_length = 0
        self._transport = None
        self._sftp = None
        self.url = url
        self.download_dir = downloaded_dir

    def _connect(self):
        parsed_url = urlparse(self.url)
        hostname = parsed_url.hostname
        port = parsed_url.port or 0
        username = parsed_url.username
        password = parsed_url.password

        try:
            self._transport = paramiko.Transport((hostname, port))
            self._transport.connect(username=username, password=password)
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        except:
            print("sftp login error for {0}".format(self.url))
            if self._sftp:
                self._sftp.close()
            if self.transport:
                self.transport.close()


    def startDownload(self):
        parsed_url = urlparse(self.url)
        path = parsed_url.path

        file_name = os.path.basename(path)
        local_filename = os.path.join(self.download_dir, file_name)

        self._connect()

        try:
            self._sftp.get(path, local_filename)
            return local_filename
        except Exception as e:
            os.remove(local_filename) # Cleanup
            return None
        finally:
            # proper teardown of connection
            if self._sftp:
                self._sftp.close()
            if self._transport:
                self._transport.close()

