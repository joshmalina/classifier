import os
import subprocess

FAST_TEXT = os.environ['FASTTEXT']
MODEL = os.environ['MODEL']

def classify_review(review_text):
    return call_fasttext(review_text)

def call_fasttext(review_text):
    print(review_text)
    bashCommand = FAST_TEXT + " test  --model " + MODEL 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output