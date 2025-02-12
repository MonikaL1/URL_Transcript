from flask import Flask, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
from nltk.tokenize import sent_tokenize

app = Flask(__name__)

nltk.download('punkt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['GET'])
def transcribe():
    url = request.args.get('url')
    try:
        video_id = url.split("=")[1]

        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        transcript_text = ""
        for segment in transcript_list:
            if 'text' in segment:
                transcript_text += segment['text'] + " "

        transcribed_text = transcript_text

        return transcribed_text

    except Exception as e:
        return f"False: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
