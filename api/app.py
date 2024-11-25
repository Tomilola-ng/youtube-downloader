""" YouTube Video Download """
import os

from flask import Flask, render_template, request, send_file
from pytube import YouTube
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'downloads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    """ Main Function """
    if request.method == 'POST':
        try:
            video_url = request.form.get('video_url')
            if not video_url:
                return render_template('index.html', error="Please enter a YouTube URL")

            yt = YouTube(video_url)
            stream = yt.get_highest_resolution()

            if not stream:
                return render_template('index.html', error="No suitable video stream found")

            filename = secure_filename(f"{yt.title}.mp4")
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            stream.download(output_path=app.config['UPLOAD_FOLDER'], filename=filename)

            return send_file(output_path, as_attachment=True)

        except Exception as e:
            return render_template('index.html', error=f"An error occurred: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

