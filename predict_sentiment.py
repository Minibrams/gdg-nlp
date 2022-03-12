import numpy as np

def predict_sentiment(text):
    return np.random.rand()


if __name__ == '__main__':
    text = input('Please enter the text to analyse: ')
    sentiment = predict_sentiment(text)
    print(f'Predicted sentiment score: {sentiment}')
