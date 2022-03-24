"""
    This Module creates an IBM Watson translaction service instance to conduct
    language translation
"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2022-01-01',
    authenticator=authenticator
)
translator.set_service_url(url)


def english_to_french(english_text):
    """
    This function takes in an english text and returns it in french using 
    the IBM Watson translation service
    """
    translation = translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    This function takes in a french text and returns it in english using 
    the IBM Watson translation service
    """
    translation = translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
