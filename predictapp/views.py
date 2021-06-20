from django.shortcuts import render
from .apps import PredictappConfig
from django.http import JsonResponse
from rest_framework.views import APIView


class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            # get grievance title from request
            title = request.GET.get('title')

            # vectorize grievance title
            vector = PredictappConfig.vectorizer.transform([title])
            # predict based on vector
            prediction = PredictappConfig.regressor.predict(vector)[0]
            # build response
            response = {'department': str(prediction)}
            # return response
            return JsonResponse(response)