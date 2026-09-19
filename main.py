from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__, template_folder='frontend', static_folder='frontend', static_url_path='/static')

def get_sentiment(text):
    # Analyze the text and return polarity, subjectivity, and classification.
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Classifying based on the polarity
    if polarity > 0:
        classification = "Positive"
    elif polarity < 0:
        classification = "Negative"
    else:
        classification = "Neutral"
    
    # Rounding of the scores for cleaner display
    return {
        'polarity': round(polarity, 2),
        'subjectivity': round(subjectivity, 2),
        'classification': classification
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_text = ""
    
    if request.method == 'POST':
        user_text = request.form.get('text', '')
        if user_text.strip():  # Only analyze if text is not empty
            result = get_sentiment(user_text)
    
    return render_template('webpage.html', result=result, user_text=user_text)

if __name__ == '__main__':
    app.run(debug=True)