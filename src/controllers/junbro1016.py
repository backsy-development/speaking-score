from flask import Blueprint, request
from config.config import AppConfig
from transformers import pipeline
import numpy as np

junbro1016 = Blueprint('junbro1016', __name__)

completenessPipe = pipeline("audio-classification", model="junbro1016/pronunciation-scoring-completeness")
fluencyPipe = pipeline("audio-classification", model="junbro1016/pronunciation-scoring-fluency")

@junbro1016.route('/junbro1016/pronunciation-scoring-completeness', methods=['POST'])
def getPronounceScore():
  try: 
    audio_buffer = request.data
    result = completenessPipe(audio_buffer)
    return result
  except Exception as e:
    print(e)
    return {
      "message": "serverError"
    }, 500
  
@junbro1016.route('/junbro1016/pronunciation-scoring-fluency', methods=['POST'])
def getFluencyScore():
  try: 
    audio_buffer = request.data
    result = fluencyPipe(audio_buffer)
    return result
  except Exception as e:
    print(e)
    return {
      "message": "serverError"
    }, 500
  