# @see https://huggingface.co/classla/wav2vec2-xls-r-parlaspeech-hr

from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import soundfile as sf
import torch
import os

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# load model and tokenizer
processor = Wav2Vec2Processor.from_pretrained(
    "classla/wav2vec2-xls-r-parlaspeech-hr")
model = Wav2Vec2ForCTC.from_pretrained("classla/wav2vec2-xls-r-parlaspeech-hr")

transcripts = []

# Zamijeniti sa path_to_veprad_audio_files na vlastitom računalu
audio_dir = "../kcs/projekt/veprad_short/wav_sm04/"

audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]

transcript_file = "transcripts.txt"
file = open(transcript_file,'w' , encoding="utf-8")

print(f"Transcirption audio files found in {audio_dir}")
for i, audio_file in enumerate(audio_files):
    base_name = os.path.splitext(audio_file)[0]
    
    # read the wav file
    speech, sr = sf.read(os.path.join(audio_dir, audio_file))
    input_values = processor(speech, sampling_rate=sr, return_tensors="pt").input_values.to(device)
    
    # retrieve logits
    logits = model.to(device)(input_values).logits

    # take argmax and decode
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0]).lower()

    transcripts.append(transcription)
    print(f"Transcripted {audio_file} to '{transcription}' ({i}/{len(audio_files)})")
    file.write(transcription+"\n")

file.close()


