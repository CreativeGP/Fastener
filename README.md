# ![](https://github.com/CreativeGP/Fastener/blob/images/fastener-logo.png "Fastener")

A simple hackable task automizer.

## Description
CGP Fastener is a simple task automizer. You can watch event and run your task automatically.

The supported events are as follows now:
- File changing, creation, deleting.

## Requirement
- Python2.x
- Python packages
    - [watchdog](https://pypi.python.org/pypi/watchdog)
    - [argparse](https://pypi.python.org/pypi/argparse)

## Usage
`python fastener.py basedir mode [--recursive] [--silent]`

`basedir` is a directory path where you want to watch.

`mode` is name you configured your tasks.

`--recursive` `-r`: Watch recursively.

`--silent` `-s`: Do not show the results of your tasks.


## Install
Just clone this repogitory.

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[CreativeGP](https://github.com/CreativeGP)
