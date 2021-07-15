# downloader
A program that can be used to download data from multiple sources and protocols to local disk.
The list of sources will be given as input in the form of urls (e.g. http://my.file.com/file, ftp://other.file.com/other, sftp://and.also.this/ending etc)
The program should download all the sources, to a configurable location (file name should be uniquely determined from the URL) and then exit.

##### Current supported protocols
- http, https, ftp, sftp

## Installation
 `python setup.py install`


## How to use
First, list urls to download in a file

Example: 'links.txt' containing.

```
'http://speedtest.ftp.otenet.gr/files/test100k.db'
'https://www.wikihow.com/images/f/fc/Convert-JPG-to-PNG-Step-20.jpg'
'ftp://speedtest:speedtest@ftp.otenet.gr/test10Mb.db'
'sftp://demo:password@test.rebex.net:22/readme.txt'
```


To download the file from these URL to "C:\valid" use the command below.

`downloader -f link.txt -o C:\valid`

note: if output directory path is invalid (application will autogenerate and use downloads folder)



## How to run unit test
Go to package root directory then run test cases using pytest

1.`cd DownloaderHomework`

2.`pytest`