import pygame
from gtts import gTTS
import time
import io
import importlib

def speak_and_display(text, lang='en', wait_time=15):
    # Convertir texto a voz
    tts = gTTS(text=text, lang=lang)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    # Inicializar pygame
    pygame.init()
    screen = pygame.display.set_mode((1080, 900))
    pygame.display.set_caption("Text-to-Speech Display")
    font = pygame.font.Font(None, 74)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text_surface, (100, 250))
    pygame.display.flip()

    # Reproducir el audio
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()

    # Esperar a que termine la reproducción del audio
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    # Contador de espera
    for i in range(wait_time, 0, -1):
        screen.fill((0, 0, 0))
        text_surface = font.render(f"{text} - {i}", True, (255, 255, 255))
        screen.blit(text_surface, (100, 250))
        pygame.display.flip()
        time.sleep(1)

# Ejemplo de uso
if __name__ == "__main__":
    # Nombre del conjunto de frases a utilizar
    phrases_set_name = 'phrases'  # Cambia esto al nombre del conjunto que desees usar

    # Importar dinámicamente el módulo de frases
    phrases_module = importlib.import_module('phrases')
    
    # Obtener el conjunto de frases por su nombre
    phrases_set = getattr(phrases_module, phrases_set_name)
    
    # Usar el conjunto de frases seleccionado
    for phrase, lang in phrases_set:
        speak_and_display(phrase, lang)
    
    pygame.quit()
