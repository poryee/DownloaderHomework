import os
from ftplib import FTP
from urllib.parse import urlparse
from tqdm import tqdm

class FtpDownloader():

    def __init__(self, url, downloaded_dir):
        self._file_downloaded_length = 0
        self._chunk_size = 1024
        self._ftp = FTP()
        self.url = url
        self.download_dir = downloaded_dir

    def _connect(self):
        parsed_url = urlparse(self.url)
        hostname = parsed_url.hostname
        port = parsed_url.port or 0
        username = parsed_url.username
        password = parsed_url.password

        try:
            self._ftp.connect(host=hostname, port=port)
            self._ftp.login(username, password)
        except:
            print("ftp login error for {0}".format(self.url))


    def startDownload(self):

        parsed_url = urlparse(self.url)
        path = parsed_url.path
        dirname = os.path.dirname(path)

        file_name = os.path.basename(path)
        local_filename = os.path.join(self.download_dir, file_name)
        try:
            # init ftp connection
            self._connect()
            if dirname:
                self._ftp.cwd(dirname)

            total_size = self._ftp.size(path)
            remote_filename = os.path.basename(path)

            with open(local_filename, 'wb') as f:

                with tqdm(total=total_size,unit='B', unit_scale=True, unit_divisor=self._chunk_size, disable=False) as pbar:
                    res = self._ftp.retrbinary("RETR " + remote_filename, lambda data: self.writeDataToFile(f, data, pbar))
                    if not res.startswith('226'):
                        # clean up
                        os.remove(local_filename)
            return local_filename

        except Exception as e:
            os.remove(local_filename)
            return None
        finally:
            # proper teardown of connection
            if self._ftp:
                self._ftp.close()


    def writeDataToFile(self, f, data, pbar):
        self._file_downloaded_length += len(data)
        pbar.update(len(data))
        f.write(data)