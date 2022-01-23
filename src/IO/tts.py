import pyttsx3, json, os
from ibm_watson import TextToSpeechV1, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from simpleSound import play

with open('config.json') as configFile:
    config = json.loads(configFile.read());

authenticator = IAMAuthenticator(config['IBM_WATSON_API_KEY']);
textToSpeechV1 = TextToSpeechV1(authenticator=authenticator);
textToSpeechV1.set_service_url(config['IBM_WATSON_SERVICE_URL']);

if (not os.path.exists('Temp')):
    os.mkdir('Temp');

def speak(text):
    if (config['IBM_WATSON_API_KEY'] and config['IBM_WATSON_SERVICE_URL']):
        with open('Temp/speech.mp3', 'wb') as speechFile:
            speechFile.write(textToSpeechV1.synthesize(text, voice='en-US_HenryV3Voice', accept = 'audio/mp3').get_result().content);

        play('Temp/Speech.mp3');

        return;

    pyttsx3.speak(text);