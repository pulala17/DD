# 导入所需模块
import sys
import pygame
from pygame.sprite import Group 
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #指定游戏窗口尺寸（像素）
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编程
    bullets = Group() # 这个group是在while外创建的，无需每次运行时都创建一个新group

    #设置背景色
    bg_color = (230, 230, 230)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update(ai_settings, screen)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game()                
