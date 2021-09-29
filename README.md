# torrentfile

![torrentfile](https://github.com/alexpdev/torrentfile/blob/master/assets/torrentfile.png?raw=true)

------

## Bittorrent File Creator (.torrent)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2da47ec1b5904538a40230f049a02be4)](https://www.codacy.com/gh/alexpdev/torrentfile/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexpdev/torrentfile&utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/2da47ec1b5904538a40230f049a02be4)](https://www.codacy.com/gh/alexpdev/torrentfile/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexpdev/torrentfile&utm_campaign=Badge_Coverage)
![GitHub repo size](https://img.shields.io/github/repo-size/alexpdev/torrentfile?style=plastic)
![GitHub](https://img.shields.io/github/license/alexpdev/torrentfile?style=plastic)

_Torrentfile_ is a CLI for creating .torrent files for bittorrent clients.

## Features

- Simple interface
- Create files for Bittorrent v1
- Create files for Bittorrent v2
- Create files with multiple trackers
- Optionally specify size of individual packets of data for transfer
- Flag torrent file as private for private trackers.
- Check torrentfile against file or directory for match.
- Optional GUI can be found at [https://github.com/Torrentfile-GUI](https://github.com/Torrentfile-GUI)

## Documentation

Documentation can be found by opening your webrowser in the `docs` directory
or by visiting [https://alexpdev.github.io/torrentfile](https://alexpdev.github.io/torrentfile).

## Installation

### via PyPi

`> pip install torrentfile`

### via Git

`> git clone https://github.com/alexpdev/torrentfile.git`

### download

Or download the latest release from the Release page on github.
[https://github.com/alexpdev/torrentfile/releases](https://github.com/alexpdev/torrentfile/releases)

## Using

    usage: torrentfile -p <path> [-h] [--version] [-a <url>]
        [--piece-length <number>] [--private] [-o <path>] [--v2]
        [--created-by <app>] [--comment <comment>] [--source <source>]
        [--announce-list [<url> ...]]

    Create .torrent files for Bittorrent v1 or v2.

    arguments:
    -h, --help            show this help message and exit
    --version             show program version and exit
    -p <path>, --path <path>
                            (required) path to torrent content
    -a <url>, --announce <url>
                            announce url for tracker
    --piece-length <number>
                            specify size in bytes for data transfer
    --private             use if torrent is for private tracker
    -o <path>, --out <path>
                            specify path for .torrent file
    --v2, --meta-version2
                            use if bittorrent v2 file is wanted
    --created-by <app>
    --comment <comment>   include a comment in .torrent file
    --source <source>     ignore unless instructed otherwise
    --announce-list [<url> ...]
                            for any additional trackers

## License

Distributed under the GNU LGPL v3 license. See `LICENSE` for more information.

[https://github.com/alexpdev](https://github.com/alexpdev/)
