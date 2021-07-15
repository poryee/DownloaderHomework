import math
import os

import requests
from tqdm import tqdm


class HttpDownloader():

    def __init__(self, url, downloaded_dir):

        self._request = None
        self._chunk_size = 1024
        self.url = url
        self.download_dir = downloaded_dir

    def startDownload(self):
        try:
            self._request = requests.get(self.url, stream=True)
            file_name = os.path.basename(self.url)
            local_filename = os.path.join(self.download_dir, file_name)
            # so we know if the download is complete
            total_size = int(self._request.headers.get('content-length', 0))
            wrote = 0
            with open(local_filename, 'wb') as f:
                # update progress in terminal
                for data in tqdm(self._request.iter_content(self._chunk_size), total=math.ceil(total_size // self._chunk_size), unit='KB', unit_scale=True):
                    wrote = wrote + len(data)
                    f.write(data)
            if total_size != 0 and wrote != total_size:
                # Cleanup
                os.remove(local_filename)
                return None
            return local_filename
        except Exception as e:
            os.remove(local_filename) # Cleanup
            return None
        finally:
            # proper teardown of connection
            if self._request:
                self._request.close()