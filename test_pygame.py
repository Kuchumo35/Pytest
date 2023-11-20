import unittest
import pygame
import mygame
import random

class TestGame(unittest.TestCase):

  def setUp(self):
      pygame.init()
      self.screen = pygame.display.set_mode((800, 600))
      self.background = pygame.image.load('bg.jpg')

      self.playerImg = pygame.image.load('player.png')
      self.playerX = 370
      self.playerY = 480
      self.playerX_change = 0

      self.meatImg = []
      self.meatX = []
      self.meatY = []
      self.meatX_change = []
      self.meatY_change = []
      self.num_of_meats = 1

      for i in range(self.num_of_meats):
          self.meatImg.append(pygame.image.load('meat.png')) 
          self.meatX.append(random.randint(0, 735))
          self.meatY.append(random.randint(50, 150)) 
          self.meatX_change.append(40)
          self.meatY_change.append(0.2) 

      self.shootImg = pygame.image.load('star.png')
      self.shootX = 0
      self.shootY = 480
      self.shootX_change = 0
      self.shootY_change = 5
      self.shoot_state = "ready"

      self.score_value = 0
      self.font = pygame.font.Font('freesansbold.ttf', 32)
      self.textX = 10
      self.textY = 10

      self.gameover_font = pygame.font.Font('freesansbold.ttf', 64)
    
    

  def test_screen_size(self):
      self.assertEqual(self.screen.get_size(), (800, 600))

  def test_background_image(self):
      self.assertIsNotNone(self.background)

  def test_player_image(self):
      self.assertIsNotNone(self.playerImg)

  def test_player_position(self):
      self.assertEqual(self.playerX, 370)
      self.assertEqual(self.playerY, 480)

  def test_meat_image(self):
      self.assertIsNotNone(self.meatImg[0])

  def test_meat_position(self):
      self.assertEqual(len(self.meatX), self.num_of_meats)

  def test_shoot_image(self):
    self.assertIsNotNone(self.shootImg)

  def test_shoot_position(self):
    self.assertEqual(self.shootX, 0)
    self.assertEqual(self.shootY, 480)

  def test_shoot_state(self):
    self.assertEqual(self.shoot_state, "ready")

  def test_score_value(self):
    self.assertEqual(self.score_value, 0)

  def test_font(self):
    self.assertIsNotNone(self.font)

  def test_text_position(self):
    self.assertEqual(self.textX, 10)
    self.assertEqual(self.textY, 10)

  def test_gameover_font(self):
    self.assertIsNotNone(self.gameover_font)

  def tearDown(self):
      pygame.quit()

if __name__ == '__main__':
  unittest.main()