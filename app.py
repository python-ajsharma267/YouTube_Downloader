from flask import Flask, render_template, request
from pytube import YouTube
import os

pics_folder = os.path.join('static', 'pics')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = pics_folder 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the YouTube video URL from the form
        url = request.form['url']

        # Create a YouTube object
        yt = YouTube(url)

        # Print the available streams for the video
        print("Available streams:")
        for stream in yt.streams:
            print(stream)

        # Get the first stream (highest resolution)
        stream = yt.streams.get_by_itag(22)

        # Download the stream
        print("Downloading...")
        # Download at downloads 
        stream.download(r'C:\Users\ajsha\Downloads')
        print("Download complete!")

        return "Download complete!"
    else:
        backgroud = os.path.join(app.config['UPLOAD_FOLDER'], 'youtube.png')
        first = os.path.join(app.config['UPLOAD_FOLDER'], '1st.jpg')
        second = os.path.join(app.config['UPLOAD_FOLDER'], '2nd.png')
        third = os.path.join(app.config['UPLOAD_FOLDER'], '3rd.png')

        # Render the HTML form
        return render_template('index.html',bg = backgroud, first_pic = first, second_pic = second ,third_pic = third)

app.run(debug=True)
