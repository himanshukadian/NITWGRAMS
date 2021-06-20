from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class PredictappConfig(AppConfig):
    # create path to models
    name = 'predictapp'
    path = os.path.join(settings.MODELS, 'models.p')

    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    regressor = data['regressor']
    vectorizer = data['vectorizer']