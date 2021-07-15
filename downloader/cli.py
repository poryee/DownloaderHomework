import sys
import argparse
from pathlib import Path
from downloader.download_helper import DownloadHelper


def valid_directory(dir_val):
    # if path not valid give downloads as default
    if not Path(dir_val).exists():
        return '/downloads'
    return dir_val

def getOutputDir(output_dir):
    # pathlib able handle windows or unix path
    path=Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path.resolve()

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_url', type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin, help='File containing urls')
    parser.add_argument('-o', '--output_directory', required=True, type=valid_directory, help='Output directory')
    return parser.parse_args()


def main():
    # get cli arg
    args = parseArgs()

    # converting url within file to array or urls
    urls = [url.strip() for url in args.file_url.readlines()]
    # valid directory provided

    # make /download
    output_directory = getOutputDir(args.output_directory)

    # pass valid cli input to downloader
    download_manager = DownloadHelper(urls, output_directory)
    download_manager.process()
