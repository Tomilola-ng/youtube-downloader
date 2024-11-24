from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def main():
    """ Main Function """
    video_url = request.args.get('video-url')
    yt = YouTube(video_url)
    yt.streams().download()

    return 'Hey there, your video is being download'
