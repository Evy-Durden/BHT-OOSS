import datetime
import urllib.request

start_time = datetime.datetime.now()

with urllib.request.urlopen('https://st01.sslstream.dlf.de/dlf/01/128/mp3/stream.mp3') as stream:
    with open('recording.mp3', 'wb')  as audio_file:
        while (datetime.datetime.now() - start_time).seconds < 10:
            audio_file.write(stream.read(128)) 