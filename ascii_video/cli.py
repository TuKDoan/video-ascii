"""This module contains a CLI interface"""

from . import player

def main():
    import argparse

    CLI_DESC = "Convert you videos to ASCII output"
    EPILOG = ("\033[1;37mThank you for trying this out!\033[0m")

    PARSER = argparse.ArgumentParser(prog='ascii-video', description=CLI_DESC, epilog=EPILOG)
    PARSER.add_argument('-f', '--file', type=str, dest='file', help='input video file', action='store', required=True)
    PARSER.add_argument('--strategy', default='ascii-color', type=str, dest='strategy',
        choices=["ascii-color", "just-ascii", "filled-ascii"], help='choose an strategy to render the output', action='store')
    PARSER.add_argument('-o', '--output', type=str, dest='output', help='output file to export', action='store')
    PARSER.add_argument('-a','--with-audio', dest='with_audio', help='play audio track', action='store_true')

    ARGS = PARSER.parse_args()

    player.play(ARGS.file, strategy=ARGS.strategy, output=ARGS.output, play_audio=ARGS.with_audio)


if __name__ == '__main__':
    main()