# Train models to predict cost overrun

import pickle
import random

def random_model():
    cats = ['Near/Under', 'Moderate', 'High']
    return random.choice(cats)

def create_train_test():
    print('train-test made')

class ml_model:
    def __init__(self):
        self.model_name = 'ml_example'

    def get_training_data(self):
        print('got le data')

    def train(self,train_data):
        """
        Train a scikit model and return the model object
        """
        print('model trained')

    def save_model(self,filename):
        """
        pickle the model object
        """
        print(f'model saved as {filename}')

    def test(self,test_data):
        """
        Test loaded model against test data and
        output prf1 or other metrics
        """