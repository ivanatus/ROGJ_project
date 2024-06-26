# from phonemizer import phonemize

# Example text and language specification
text = "umjeren do jak jugozapadni vjetar more umjereno valovito i valovito"
language = "hr"

# Phonemize requires a lot of preinstalled stuff so skipping

# # Generate phonemes
# phonemes = phonemize(text, language=language)
# print(phonemes)

import pocketsphinx
from pocketsphinx import get_model_path

print(get_model_path())

lmpath = "./zuzic_bres/my_db_pruned.lm.DMP" #"my_db_pruned.lm.DMP"
hmmpath = "./zuzic_bres/acoustic_model" #"tutorial3/model_parameters/my_db.cd_cont_200"
dictpath = "./zuzic_bres/zuzic_bres_dict.dic"

audio_config = {
    'verbose': False,
    'audio_file': '../kcs/veprad - Copy/wav_sm04/sm04010103201.wav',
    'hmm': hmmpath,
    'lm': lmpath,
    'dict': dictpath
}

# my_config = pocketsphinx.Config(audio_config)
# my_decoder = pocketsphinx.Decoder(my_config)

audio_file = pocketsphinx.AudioFile(**audio_config)

for phrase in audio_file:
            print(f"phrase: {phrase}")
            for s in phrase.seg():
                print(f"s: {s.word}")