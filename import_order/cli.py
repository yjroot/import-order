import optparse

from .inspect import inspect_order
from .version import VERSION


parser = optparse.OptionParser(
    usage='%prog [options] [local package ...] [file ...] [directory ...]',
    version='%prog {}'.format(VERSION))
parser.add_option('-d', '--debug', action='store_true', default=False,
                  help='Debug mode.')
parser.add_option('--only-file', action='store_true', default=False,
                  help='Inspect only files not packages')
parser.add_option('--exclude', action='append', default=[],
                  help='Ignore specific file or directory.')


def main():
    options, args = parser.parse_args()
    inspect_order(args, options.debug, options.only_file, options.exclude)
