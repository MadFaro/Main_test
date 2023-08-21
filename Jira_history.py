from transformers import WhisperFeatureExtractor

feature_extractor = WhisperFeatureExtractor.from_pretrained("openai/whisper-base.en")
# don't normalise
input_features = feature_extractor(audio, do_normalise=False).input_features[0]
# do normalise
input_features = feature_extractor(audio, do_normalise=True).input_features[0]
