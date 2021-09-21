import os
import pytest
from torrentfile.metafileV2 import TorrentFileV2
from torrentfile.metafile import TorrentFile, Checker
from tests.context import tempdir, tempfile, rmpaths, Flags


def maketorrent(args, v2=False):
    flags = Flags(**args)
    if v2:
        torrent = TorrentFileV2(flags)
    else:
        torrent = TorrentFile(flags)
    torrent.assemble()
    return torrent.write()

@pytest.fixture(scope="module")
def tdir():
    return tempdir()

@pytest.fixture(scope="module")
def tfile():
    return tempfile()

@pytest.fixture(scope="module")
def metav2f(tfile):
    args = {"private": True,
            "path": tfile,
            "announce": "http://announce.com/announce"}
    outfile, meta = maketorrent(args, v2 = True)
    yield outfile, meta
    rmpaths([tfile, outfile])


@pytest.fixture(scope="module")
def metav2d(tdir):
    args = {
        "private": True,
        "path": tdir,
        "announce": "http://announce.com/announce",
        "source": "tracker",
        "comment": "content details and purpose",
    }
    outfile, meta = maketorrent(args, v2=True)
    yield outfile, meta
    rmpaths([tdir, outfile])

@pytest.fixture(scope="module")
def metav1d(tdir):
    args = {
        "private": True,
        "path": tdir,
        "announce": "http://announce.com/announce",
        "source": "tracker",
        "comment": "content details and purpose",
    }
    outfile, meta = maketorrent(args)
    yield outfile, meta
    rmpaths([tdir, outfile])


@pytest.fixture(scope="module")
def metav1f(tfile):
    args = {"private": True,
            "path": tfile,
            "announce": "http://announce.com/announce"}
    outfile, meta = maketorrent(args)
    yield outfile, meta
    rmpaths([tfile, outfile])


@pytest.fixture(scope="module")
def tfilemeta(tfile):
    args = {"private": True,
            "path": tfile,
            "announce": "http://announce.com/announce"}
    outfile, _ = maketorrent(args)
    yield outfile, tfile
    rmpaths([tfile, outfile])


@pytest.fixture(scope="module")
def tdirmeta(tdir):
    args = {"private": True,
            "path": tdir,
            "announce": "http://announce.com/announce"}
    outfile, _ = maketorrent(args)
    yield outfile, tdir
    rmpaths([tdir, outfile])


def test_v2_meta_keys(metav2f):
    outfile, meta = metav2f
    for key in ["announce", "info", "piece layers",
                "creation date", "created by"]:
        assert key in meta
    assert os.path.exists(outfile)


def test_v2_info_keys_file(metav2f):
    outfile, meta = metav2f
    for key in [
        "length",
        "piece length",
        "meta version",
        "file tree",
        "name",
        "private",
    ]:
        assert key in meta["info"]
    assert os.path.exists(outfile)


def test_v2_info_keys_dir(metav2d):
    outfile, meta = metav2d
    for key in [
        "piece length",
        "meta version",
        "file tree",
        "name",
        "private",
        "source",
        "comment",
    ]:
        assert key in meta["info"]
    assert os.path.exists(outfile)


def test_v1_meta_keys(metav1f):
    outfile, meta = metav1f
    for key in ["announce", "info", "creation date", "created by"]:
        assert key in meta
    assert os.path.exists(outfile)


def test_v1_info_keys_file(metav1f):
    outfile, meta = metav1f
    for key in [
        "length",
        "piece length",
        "pieces",
        "name",
        "private",
    ]:
        assert key in meta["info"]
    assert os.path.exists(outfile)


def test_v1_info_keys_dir(metav1d):
    outfile, meta = metav1d
    for key in [
        "piece length",
        "pieces",
        "name",
        "private",
        "source",
        "comment",
    ]:
        assert key in meta["info"]
    assert os.path.exists(outfile)


def test_metafile_checker_v1_file(tfilemeta):
    outfile, tfile = tfilemeta
    checker = Checker(outfile, tfile)
    status = checker.check()
    assert status == "100%"

def test_metafile_checker_v1_dir(tdirmeta):
    outfile, tdir = tdirmeta
    checker = Checker(outfile, tdir)
    status = checker.check()
    assert status == "100%"
