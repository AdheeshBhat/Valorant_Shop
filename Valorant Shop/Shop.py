from inspect import classify_class_attrs
from re import X
import pygame
import buy_weapons
from pygame.locals import *
pygame.init()
global shop_x
global shop_y
shop_x = 0
shop_y = 0
shop_gui = pygame.image.load("valorant_gun_shop.jpg")
shop_gui = pygame.transform.smoothscale(shop_gui, (1200,600))
screen = pygame.display.set_mode((1200,600))
main_weapon = False
secondary_weapon = False
secondary_weapon_list = ["classic", "shorty", "frenzy", "ghost", "sheriff"]
main_weapon_list = ["stinger","spectre","bucky","judge","bulldog","guardian","phantom","vandal","marshal","operator","ares","odin"]
last_bought_main = ""
last_bought_secondary = ""
clock = pygame.time.Clock()
shop = {"classic" : 0, "shorty" : 200, "frenzy" : 400, "ghost" : 500,
"sheriff" : 800, "stinger" : 1000, "spectre" : 1600, "bucky" : 900,
"judge" : 1500, "bulldog" : 2100, "guardian" : 2700, "phantom" : 2900,
"vandal" : 2900, "marshal" : 1100, "operator" : 4500, "ares" : 1600, "odin": 3500}
bought_items = []
budget = 9000

def shop_gui_position(shop_x, shop_y, shop_gui):
    screen.blit(shop_gui,(shop_x,shop_y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if 6 < x < 157 and 32 < y < 139:
                item = "classic"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)
            if 6 < x < 156 and 146 < y < 252:
                item = "shorty"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 8 < x < 157 and 257 < y < 365:
                item = "frenzy"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)
            
            if 6 < x < 159 and 369 < y < 478:
                item = "ghost"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 8 < x < 158 and 484 < y < 592:
                item = "sheriff"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 191 < x < 410 and 30 < y < 160:
                item = "stinger"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary= buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 192 < x < 412 and 167 < y < 297:
                item = "spectre"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 190 < x < 413 and 340 < y < 464:
                item = "bucky"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 190 < x < 413 and 467 < y < 590:
                item = "judge"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 418 < x < 684 and 31 < y < 167:
                item = "bulldog"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 418 < x < 684 and 173 < y < 310:
                item = "guardian"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 418 < x < 684 and 315 < y < 451:
                item = "phantom"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 418 < x < 684 and 456 < y < 593:
                item = "vandal"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 692 < x < 1006 and 29 < y < 161:
                item = "marshal"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 692 < x < 1006 and 168 < y < 300:
                item = "operator"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 692 < x < 1006 and 341 < y < 463:
                item = "ares"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

            if 692 < x < 1006 and 470 < y < 592:
                item = "odin"
                budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary = buy_weapons.buy(shop, budget,
                item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list)
                print (item)
                print (budget)

    shop_gui_position(shop_x, shop_y, shop_gui)
    pygame.display.update()
    clock.tick(60)

    