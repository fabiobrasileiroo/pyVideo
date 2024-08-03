from moviepy.editor import VideoFileClip

# Caminho para o arquivo de vídeo
video_path = '/home/fabiopc/Vídeos/2024-08-03 00-04-10.mkv'
# Caminho para salvar o áudio
audio_output_path = 'audioManga.mp3'

try:
    # Carrega o arquivo de vídeo
    video_clip = VideoFileClip(video_path)

    # Extrai o áudio
    audio_clip = video_clip.audio

    # Salva o áudio extraído com uma taxa de bits específica (exemplo: 320 kbps)
    audio_clip.write_audiofile(audio_output_path, bitrate='320k')

    # Fecha o vídeo e o áudio clips
    video_clip.close()
    audio_clip.close()

except Exception as e:
    print(f"Erro ao processar o vídeo: {e}")
