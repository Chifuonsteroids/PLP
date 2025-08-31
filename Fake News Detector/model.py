from transformers import pipeline

# Load a pretrained fake news classification model from HuggingFace
# Small model = faster to run in hackathon demo
classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")


def predict_fake_news(text: str):
    """
    Classify news text as FAKE / TRUE with confidence score.
    """
    result = classifier(text)[0]   # Model returns list of predictions
    label = result['label']
    score = round(result['score'] * 100, 2)
    return label, score
