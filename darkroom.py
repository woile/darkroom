#!/usr/bin/python3

import argparse
import subprocess
import os

APP_DESCRIPTION = ('Tool to automatically apply different effects to your photos and choose those '
                   'you prefer the most.')

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
SCRIPTS_DIR = 'scripts/'

DEFAULT_PATTERN = '*.JPG'

ARGS = [
    {
        'name': 'pattern',
        'default': DEFAULT_PATTERN,
        'help': 'Images selection pattern'
    }
]

COMMANDS = (
    {
        'script': 'init',
        'help': 'starts corresponding folders',
        'args': []
    },
    {
        'script': 'auto_levels',
        'help': 'auto White Balance / Contrast Stretch / HSV Stretch',
        'args': ARGS
    },
    {
        'script': 'natgeo',
        'help': 'national geographic effect on your pictures',
        'args': ARGS
    },
    {
        'script': 'color_enhance',
        'help': 'Improve quality color of pictures',
        'args': ARGS
    }
)


def run_command(command, pattern=''):
    subprocess.call([os.path.join(ROOT_DIR, SCRIPTS_DIR, command), '%s' % pattern])


def get_arguments():
    formater = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='darkroom', description=APP_DESCRIPTION,
                                     formatter_class=formater)
    subparsers = parser.add_subparsers()

    for cmd in COMMANDS:
        auto_levels = subparsers.add_parser(cmd['script'], help=cmd['help'])
        for arg in cmd['args']:
            auto_levels.add_argument(arg['name'], default=arg['default'],
                                     help=arg['help'])
        auto_levels.set_defaults(func=run_command, cmd=cmd['script'])

    return parser.parse_args()


def main():
    args = get_arguments()

    try:
        args.func(args.cmd, args.pattern)
    except AttributeError:
        args.func(args.cmd)


if '__main__' == __name__:
    main()
