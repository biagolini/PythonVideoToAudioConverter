import warnings
import json
from pydub import AudioSegment
import numpy as np
import os
import glob

# Ignora warnings desnecessários
warnings.filterwarnings("ignore")

# Define pastas de entrada e saída
input_folder = 'input'
output_folder = 'output'

# Cria a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Encontra todos os arquivos .mp4 na pasta de entrada
mp4_files = glob.glob(os.path.join(input_folder, '*.mp4'))

# Processa cada arquivo
for mp4_file in mp4_files:
    try:
        # Extrai o nome base do arquivo (sem extensão)
        base_name = os.path.splitext(os.path.basename(mp4_file))[0]
        
        # Define o caminho do arquivo de saída .wav
        wav_output_path = os.path.join(output_folder, f"{base_name}.wav")
        
        # Converte o vídeo em áudio
        video = AudioSegment.from_file(mp4_file, format="mp4")
        video.export(wav_output_path, format="wav")
        
        print(f"Arquivo convertido com sucesso: {wav_output_path}")
    
    except Exception as e:
        print(f"Erro ao converter '{mp4_file}': {e}")
