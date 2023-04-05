#-----------------------------------------------------------------------------------------#
#tocando musicas 
import pygame
pygame.init()
pygame.mixer.load('sample.mp3')#aqui vc coloca a musica em arquivo mp3 com nomes pequenos pra facilitar a leitura do programa 
pygame.mixer.music.play #aqui usa função mixer para que ele possa administrar a pausa no carregamento da musica 
pygame.event.wait() #comando para que se reproduza a musica armazenada
#------------------------------------------------------------------------------------------- 