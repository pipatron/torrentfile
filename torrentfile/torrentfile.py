#! /usr/bin/python3
# -*- coding: utf-8 -*-

#####################################################################
# THE SOFTWARE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#####################################################################

"""
Main script entrypoint for creating .torrent files.

This module provides the primary command line argument parser for
the torrentfile package.  The main_script function is automatically
invoked when called from command line, and parses accompanying arguments.

Functions:
    main_script: process command line arguments and run program.
"""

import sys
from argparse import ArgumentParser
import torrentfile
from .exceptions import MissingPathError
from .metafile import TorrentFile
from .metafileV2 import TorrentFileV2


def main_script(args=None):
    """Initialize Command Line Interface for torrentfile.

    usage: torrentfile --path /path/to/content [-o /path/to/output.torrent]
           [--piece-length n] [--private] [-t https://tracker.url/announce]
           [--v2] [--source x] [--announce-list tracker.url2 tracker.url3]
           [-h]
    """
    if not args:
        args = sys.argv[1:]

    usage = """torrentfile --path /path/to/content [-o /path/to/output.torrent]
            [--piece-length 0000] [--private] [-t https://tracker.url/announce]
            [--v2] [--source x] [--announce-list tracker.url2 tracker.url3]"""

    d = "Create .torrent files for Bittorrent v1 or v2."
    parser = ArgumentParser("torrentfile", description=d, prefix_chars="-",
                            usage=usage, allow_abbrev=False)

    parser.add_argument(
        "--version",
        action="version",
        version=f"torrentfile v{torrentfile.__version__}",
        help="show program version and exit\n",
    )

    parser.add_argument(
        "-p",
        "--path",
        action="store",
        dest="path",
        metavar="<path>",
        help="(required) path to torrent content",
    )

    parser.add_argument(
        "-a",
        "--announce",
        action="store",
        dest="announce",
        metavar="<url>",
        help="tracker's announce url",
    )

    parser.add_argument(
        "--piece-length",
        action="store",
        dest="piece_length",
        metavar="<number>",
        help="specify size in bytes of packets of data to transfer",
    )

    parser.add_argument(
        "--private",
        action="store_true",
        dest="private",
        help="use if torrent is for private tracker",
    )

    parser.add_argument(
        "-o", "--out",
        action="store",
        help="specify path for .torrent file",
        dest="outfile",
        metavar="<path>",
    )

    parser.add_argument(
        "--v2",
        "--meta-version2",
        action="store_true",
        dest="v2",
        help="use if bittorrent v2 file is wanted",
    )

    parser.add_argument(
        "--comment",
        action="store",
        dest="comment",
        metavar="<comment>",
        help="include a comment in .torrent file",
    )

    parser.add_argument(
        "--source",
        action="store",
        dest="source",
        metavar="<source>",
        help="ignore unless instructed otherwise",
    )

    parser.add_argument(
        "--announce-list",
        action="append",
        dest="announce_list",
        nargs="*",
        metavar="<url>",
        help="for any additional trackers"
    )
    if not args:
        args = ["-h"]

    flags = parser.parse_args(args)

    if not flags.path:
        raise MissingPathError(flags)

    kwargs = {
        "flags": flags,
        "path": flags.path,
        "announce": flags.announce,
        "announce_list": flags.announce_list,
        "piece_length": flags.piece_length,
        "source": flags.source,
        "private": flags.private,
        "outfile": flags.outfile,
        "comment": flags.comment,
    }

    if flags.v2:
        torrent = TorrentFileV2(flags)
    else:
        torrent = TorrentFile(flags)
    torrent.assemble()
    outfile, meta = torrent.write()
    parser.kwargs = kwargs
    parser.meta = meta
    parser.outfile = outfile
    return parser


def main():
    """Initiate main function for CLI script."""
    return main_script()


if __name__ == "__main__":
    main()
