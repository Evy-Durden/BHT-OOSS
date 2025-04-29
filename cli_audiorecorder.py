import datetime
import urllib.request
import argparse
import os


STREAM_URL = 'https://st01.sslstream.dlf.de/dlf/01/128/mp3/stream.mp3'

def get_parser_arguments():
    """
    It parses the arguments and returns them.
    """
    #instance of ArgumentParser
    parser = argparse.ArgumentParser(
        prog='Audio Recorder',
        description='It will record 10 seconds of an audio stream and save it in a mp3 file',
        epilog='Linux Rules'
    )

    # add arguments for the parser
    # positional argument
    parser.add_argument('url')
    # '--' will make the argument optional
    parser.add_argument('-f', '--filename', default='recording.mp3')
    parser.add_argument('-d', '--duration', default=10, 
                        help='Duration of the recording in seconds, default: %(default)s seconds')
    parser.add_argument('-bl', '--blocksize', default=128, 
                        help='block size for read/write in bytes default: %(default)s bits')
    parser.add_argument('--allstreams', help='This will show all saved stream recordings',
                        action='store_true')
    # the actual parsing taking place
    args = parser.parse_args()

    return args

def record_audio(url, filename, duration, blocksize):

    """
    Creates an audio file.
    """
    f_name, _ = os.path.splitext(filename)
    f_name += '.mp3'

    start_time = datetime.datetime.now()

    with urllib.request.urlopen(url) as stream:
        with open(f_name, 'wb')  as audio_file:
            while True:
                diff = (datetime.datetime.now() - start_time).seconds
                render_progress_bar(int(diff), int(duration))
                if diff >= int(duration):
                    break
                audio_file.write(stream.read(int(blocksize)))
            # Final new line after completion
            print()

def show_all_streams():
    stream_files = os.listdir()
    for file in stream_files:
        name, f_extenstion = os.path.splitext(file)
        if f_extenstion == '.mp3':
            print(file)


def main():
    args = get_parser_arguments()
    if args.allstreams:
        show_all_streams()
    else:   
        record_audio(args.url, args.filename, args.duration, args.blocksize)

def render_progress_bar(value, max_value):
    """
    Renders a progress bar on the terminal
    """
    progress = int((value / max_value) * 50)
    p_sign = '=' * progress
    trailing_sign = '-' * (50 - progress)
    
    bar = '|' + p_sign + trailing_sign + '|'

    print(bar, end='\r', flush=True)



if __name__ == '__main__':
    main()