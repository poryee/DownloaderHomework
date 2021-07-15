import os
from tqdm import tqdm
import sys

from downloader.download_factory import DownloaderFactory



class DownloadHelper(object):
    def __init__(self, urls, output_directory):
        self.output_directory = output_directory

        self._urls = urls


    def process(self):
        try:
            for url in self._urls:
                downloadWorker = self.processUrl(url)
                # worker for the right protocol exist
                if downloadWorker:
                    # return download result
                    return downloadWorker.startDownload()

        except KeyboardInterrupt:
            tqdm.write('')
            sys.exit("Keyboard Interrupt - Cancel downloading tasks")


    def processUrl(self, url):
        try:
            downloader = DownloaderFactory().getDownloader(url)
        except NotImplementedError as e:
            print('{}: skipping {}'.format(e, url))
            return None

        output = os.path.join(self.output_directory)
        download_process = downloader(url, output)
        return download_process
