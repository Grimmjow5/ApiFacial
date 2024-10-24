import cv2
import os
import imutils

class CaturaFotos:
  def __init__(self,nickname):
      self.nickname = nickname

  def imprimir(self):
    print(f"Los nombres ====>{self.nickname}")
