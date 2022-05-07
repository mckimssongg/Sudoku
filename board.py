import pygame
import sys
pygame.init()

#Creando ventana
pantalla=pygame.display.set_mode((700,600)) 
pygame.display.set_caption("SUDOKU")

#áñeta de colores utilizados
celesteclaro=(174, 214, 241)
lineacolor=(52, 152, 219)
color3x3=(249, 231, 159 )

#grosor de la línea del tablero
grosor_de_linea=5

#relleno de color a la pantalla
pantalla.fill(celesteclaro)

#color para cuadros 3x3

pygame.draw.rect(pantalla,color3x3,(50,10,121,183))
pygame.draw.rect(pantalla,color3x3,(296,10,121,183))
pygame.draw.rect(pantalla,color3x3,(175,188,121,183))
pygame.draw.rect(pantalla,color3x3,(50,370,121,183))
pygame.draw.rect(pantalla,color3x3,(296,370,121,183))

#Creando líneas del tablero
def draw_lines():
  #líneas horizontales
  pygame.draw.line(pantalla,lineacolor,(50,10),(420,10),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(50,70),(420,70),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(50,130),(420,130),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(50,190),(420,190),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(50,250),(420,250),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(50,310),(420,310),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(50,370),(420,370),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(50,430),(420,430),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(50,490),(420,490),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(50,550),(420,550),grosor_de_linea)

  #líneas verticales
  pygame.draw.line(pantalla,lineacolor,(50,8),(50,552),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(91,8),(91,552),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(132,8),(132,552),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(173,8),(173,552),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(214,8),(214,552),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(255,8),(255,552),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(296,8),(296,552),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(337,8),(337,552),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(378,8),(378,552),grosor_de_linea)
  pygame.draw.line(pantalla,lineacolor,(419,8),(419,552),grosor_de_linea)
draw_lines()

while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
    pygame.display.update()