from io import StringIO

import pytest
from downloader.cli import parseArgs, main
SYSARG='sys.argv'


# variable url and tmpdir from fixture
def test_parseArgs(monkeypatch, url_file, tmpdir):
    # overwrite system arg using monkey patch for testing
    monkeypatch.setattr(SYSARG, ['downloader', '-f', url_file, '-o', str(tmpdir)])
    args = parseArgs()
    assert args.file_url.name == url_file
    assert args.output_directory == str(tmpdir)


def test_parseArgsMissingParam(monkeypatch, url_file):
    args = [['downloader', '-f'], ['downloader', '-o']]
    for arg in args:
        monkeypatch.setattr(SYSARG, arg)
        with pytest.raises(SystemExit):
            parseArgs()


def test_parseArgsInvalidParams(monkeypatch, url_file, tmpdir):
    arg = ['downloader', '-f', 'lol']
    monkeypatch.setattr(SYSARG, arg)
    with pytest.raises(SystemExit):
        parseArgs()


def test_parseArgsInvalidDirectory(monkeypatch, url_file):
    args = [['downloader', '-f', url_file, '-o', 'wth'], ['downloader', '-f', url_file, '-o', '/root']]
    for arg in args:
        monkeypatch.setattr(SYSARG, arg)
        # check if invalid path will generate download folder instead
        assert "downloads" in parseArgs().output_directory


@pytest.mark.endtoend
def test_runCli(monkeypatch, url_file, tmpdir):
    monkeypatch.setattr(SYSARG, ['downloader', '-f', url_file, '-o', str(tmpdir)])
    main()


@pytest.mark.endtoend
def test_runCliStdin(monkeypatch, url_file, tmpdir):
    with open(url_file) as f:
        stdin = StringIO(f.read())

    monkeypatch.setattr('sys.stdin', stdin)
    monkeypatch.setattr(SYSARG, ['downloader', '-o', str(tmpdir)])
    main()
