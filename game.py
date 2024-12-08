import pygame
import random
import sys

import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
TILE_SIZE = WIDTH // 10
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

font = pygame.font.SysFont("Arial", 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra")

class Game:
    def __init__(self, player_name):
        self.map_size = 10
        self.map = [["?" for _ in range(self.map_size)] for _ in range(self.map_size)]
        self.player_pos = [0, 0]
        self.map[0][0] = "S"
        self.player_name = player_name
        self.player_stats = {
            "health": 100,
            "attack": 10,
            "defense": 5,
            "experience": 0,
            "level": 1
        }
        self.inventory = []
        self.quests = []
        self.game_over = False
        self.chat_active = False
        self.chat_input = ""
        self.in_combat = False
        self.enemy_stats = {}
        self.current_quest = None

    def draw_map(self):
        for x in range(self.map_size):
            for y in range(self.map_size):
                rect = pygame.Rect(y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if [x, y] == self.player_pos:
                    pygame.draw.rect(screen, GREEN, rect)
                elif self.map[x][y] == "S":
                    pygame.draw.rect(screen, BLUE, rect)
                elif self.map[x][y] == "X":
                    pygame.draw.rect(screen, WHITE, rect)
                elif self.map[x][y] == "Q":
                    pygame.draw.rect(screen, YELLOW, rect)
                else:
                    pygame.draw.rect(screen, BLACK, rect)
                pygame.draw.rect(screen, WHITE, rect, 1)

    def draw_chat(self):
        chat_box = pygame.Surface((WIDTH, 100))
        chat_box.fill(BLACK)
        pygame.draw.rect(chat_box, WHITE, (0, 0, WIDTH, 100), 2)
        text = font.render(self.chat_input, True, WHITE)
        chat_box.blit(text, (10, 10))
        screen.blit(chat_box, (0, HEIGHT - 100))

    def draw_combat(self):
        combat_box = pygame.Surface((WIDTH, HEIGHT))
        combat_box.fill(BLACK)
        text = [
            "Statystyki wroga:",
            f"Zdrowie: {self.enemy_stats['health']}",
            f"Atak: {self.enemy_stats['attack']}",
            f"Obrona: {self.enemy_stats['defense']}",
            f"Poziom: {self.enemy_stats['level']}",
            "---------------------------------",
            "Twoje statystyki:",
            f"Zdrowie: {self.player_stats['health']}",
            f"Atak: {self.player_stats['attack']}",
            f"Obrona: {self.player_stats['defense']}",
            f"Poziom: {self.player_stats['level']}",
            "---------------------------------",
            "Naciśnij 'A', aby zaatakować, lub 'R', aby uciec."
        ]
        for i, line in enumerate(text):
            combat_text = font.render(line, True, WHITE)
            combat_box.blit(combat_text, (20, 50 + i * 40))
        screen.blit(combat_box, (0, 0))

    def execute_command(self, command):
        if command == "stats":
            self.show_stats()
        elif command.startswith("use"):
            if len(command.split(" ")) > 1:
                item = command.split(" ", 1)[1]
                self.use_item(item)
        elif command.startswith("shop"):
            self.open_shop()

    def move_player(self, direction):
        if self.in_combat:
            return
        x, y = self.player_pos
        if direction == "up" and x > 0:
            x -= 1
        elif direction == "down" and x < self.map_size - 1:
            x += 1
        elif direction == "left" and y > 0:
            y -= 1
        elif direction == "right" and y < self.map_size - 1:
            y += 1
        else:
            return
        px, py = self.player_pos
        self.player_pos = [x, y]
        if self.map[x][y] == "?":
            self.map[x][y] = "X"
            if self.map[px][py] != "S":
                self.map[px][py] = "X"
            self.trigger_event()

    def trigger_event(self):
        event = random.choice(["enemy", "item", "quest", "empty"])
        if event == "enemy":
            self.start_combat()
        elif event == "item":
            self.find_item()

    def start_combat(self):
        self.in_combat = True
        health = abs(random.randint(self.player_stats["health"] - 20, self.player_stats["health"] + 10) + 1)
        attack = abs(random.randint(self.player_stats["defense"], self.player_stats["defense"] + 12) + 1)
        defense = abs(random.randint(self.player_stats["defense"] - 2, self.player_stats["defense"] + 2) + 1)
        level = math.floor((health + (attack * 3) + (defense * 10)) / 100)
        if level <= 0:
            level = 1
        self.enemy_stats = {
            "health": health,
            "attack": attack,
            "defense": defense,
            "level": level
        }

    def combat_turn(self, action):
        if action == "attack":
            damage = max(0, self.player_stats["attack"] - self.enemy_stats["defense"])
            self.enemy_stats["health"] -= damage
            if self.enemy_stats["health"] > 0:
                enemy_damage = max(0, self.enemy_stats["attack"] - self.player_stats["defense"])
                self.player_stats["health"] -= enemy_damage
                if self.player_stats["health"] <= 0:
                    self.game_over = True
            else:
                self.in_combat = False
                self.player_stats["experience"] += random.randint(30, 100)
        elif action == "run":
            self.in_combat = False

    def find_item(self):
        item = random.choice(["mikstura leczenia", "mocniejsza bron", "zbroja", "magiczny pierscien"])
        self.inventory.append(item)
        print("\nZnalazłeś: " + item)

    def use_item(self, item):
        if item in self.inventory:
            if item == "mikstura leczenia":
                self.player_stats["health"] = min(100, self.player_stats["health"] + 30)
                self.inventory.remove(item)
                print("\nUżyłeś: " + item)
            elif item == "mocniejsza bron":
                self.player_stats["attack"] += 5
                self.inventory.remove(item)
                print("\nUżyłeś: " + item)
            elif item == "zbroja":
                self.player_stats["defense"] += 3
                self.inventory.remove(item)
                print("\nUżyłeś: " + item)
            elif item == "magiczny pierscien":
                self.player_stats["health"] += 10
                self.inventory.remove(item)
                print("\nUżyłeś: " + item)
        else:
            print("Nie posiadasz takiego przedmiotu!")
            
    def open_shop(self):
        shop_open = True
        while shop_open:
            screen.fill(BLACK)
            shop_text = [
                "Sklep:",
                "1. Mikstura leczenia (80 EXP) - Wpisz 'buy potion'",
                "2. Mocniejsza bron (40 EXP) - Wpisz 'buy weapon'",
                "3. Zbroja (50 EXP) - Wpisz 'buy armor'",
                "4. Magiczny pierscien (70 EXP) - Wpisz 'buy ring'",
                "5. Wyjdź ze sklepu - Wpisz 'exit'"
            ]
            for i, line in enumerate(shop_text):
                text = font.render(line, True, WHITE)
                screen.blit(text, (20, 50 + i * 50))

            input_text = font.render(f"Wpisz komendę: {self.chat_input}", True, YELLOW)
            screen.blit(input_text, (20, HEIGHT - 50))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        command = self.chat_input.strip().lower()
                        self.chat_input = ""
                        if command == "buy potion" and self.player_stats["experience"] >= 80:
                            self.inventory.append("mikstura leczenia")
                            self.player_stats["experience"] -= 80
                            print("Pomyślnie kupiono: mikstura leczenia")
                        elif command == "buy weapon" and self.player_stats["experience"] >= 40:
                            self.inventory.append("mocniejsza bron")
                            self.player_stats["experience"] -= 40
                            print("Pomyślnie kupiono: mocniejsza bron")
                        elif command == "buy armor" and self.player_stats["experience"] >= 50:
                            self.inventory.append("zbroja")
                            self.player_stats["experience"] -= 50
                            print("Pomyślnie kupiono: zbroja")
                        elif command == "buy ring" and self.player_stats["experience"] >= 70:
                            self.inventory.append("magiczny pierscien")
                            self.player_stats["experience"] -= 70
                            print("Pomyślnie kupiono: magiczny pierscien")
                        elif command == "exit":
                            shop_open = False
                        else:
                            continue
                    elif event.key == pygame.K_BACKSPACE:
                        self.chat_input = self.chat_input[:-1]
                    else:
                        self.chat_input += event.unicode


    def show_stats(self):
        print(f"Zdrowie: {self.player_stats['health']}")
        print(f"Atak: {self.player_stats['attack']}")
        print(f"Obrona: {self.player_stats['defense']}")
        print(f"Poziom: {self.player_stats['level']}")
        print(f"Doświadczenie: {self.player_stats['experience']}")
        print(f"Ekwipunek: {', '.join(self.inventory) if self.inventory else 'Brak przedmiotów'}")

    def play(self):
        clock = pygame.time.Clock()
        while not self.game_over:
            screen.fill(BLACK)
            if self.in_combat:
                self.draw_combat()
            else:
                self.draw_map()
                if self.chat_active:
                    self.draw_chat()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if self.chat_active:
                        if event.key == pygame.K_RETURN:
                            self.execute_command(self.chat_input)
                            self.chat_input = ""
                            self.chat_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.chat_input = self.chat_input[:-1]
                        else:
                            self.chat_input += event.unicode
                    elif self.in_combat:
                        if event.key == pygame.K_a:
                            self.combat_turn("attack")
                        elif event.key == pygame.K_r:
                            self.combat_turn("run")
                    else:
                        if event.key == pygame.K_SLASH:
                            self.chat_active = True
                        elif event.key == pygame.K_UP:
                            self.move_player("up")
                        elif event.key == pygame.K_DOWN:
                            self.move_player("down")
                        elif event.key == pygame.K_LEFT:
                            self.move_player("left")
                        elif event.key == pygame.K_RIGHT:
                            self.move_player("right")
            pl = math.floor((self.player_stats["health"] + (self.player_stats["attack"] * 3) + (self.player_stats["defense"] * 10)) / 100)
            if pl >= 1:
                self.player_stats['level'] = pl
            else:
                self.player_stats['level'] = 1

            if all(all(cell != "?" for cell in row) for row in self.map):
                self.game_over = True
                screen.fill(BLACK)
                end_text = [
                    "\nGra zakończona!",
                    f"Imię gracza: {self.player_name}",
                    f"Zdrowie: {self.player_stats['health']}",
                    f"Atak: {self.player_stats['attack']}",
                    f"Obrona: {self.player_stats['defense']}",
                    f"Poziom: {self.player_stats['level']}",
                    f"Doświadczenie: {self.player_stats['experience']}",
                    f"Ekwipunek: {', '.join(self.inventory) if self.inventory else 'Brak przedmiotów'}",
                    "\nGratulację!"
                ]
                for el in end_text:
                    print(el)
                pygame.quit()
                sys.exit()


            pygame.display.flip()
            clock.tick(FPS)

if __name__ == "__main__":
    name = input("Podaj swoje imię: ").strip()
    if not name:
        name = "Bohater"
    game = Game(name)
    game.play()
