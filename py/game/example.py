import pygame
import time
import threading


class Game:
    def __init__(self):
        self.colors = ['red', 'green']
        self.curColorIndex = 0
        self.speed = 1
        self.start = None
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

    def shouldStop(self):
        if not self.start:
            return False
        return time.time() - self.start > 60

    def showColor(self, color):
        self.screen.fill(color)
        pygame.display.flip()

    def flash(self):
        while True:
            if self.shouldStop():
                break
            color = self.colors[self.curColorIndex]
            self.curColorIndex += 1
            self.curColorIndex %= len(self.colors)
            self.showColor(color)
            time.sleep(self.speed)
        pygame.quit()

    def readKey(self):
        wordAmount = 0
        inp = ""
        inpStart = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    newSpeed = 1 if (inpStart is None) else (time.time() - inpStart)
                    self.speed = min(1, newSpeed)
                    inpStart = time.time()
                    char = event.__dict__['unicode']
                    if not char:
                        continue
                    if char == " ":
                        if inp:
                            wordAmount += 1
                            inp = ""
                            inpStart = None
                    else:
                        self.start = self.start or time.time()
                        inp += event.__dict__['unicode']
            if self.shouldStop():
                break
        print("word amunt is", wordAmount)


if __name__ == "__main__":
    g = Game()
    threads = []
    threads.append(threading.Thread(target=g.flash))
    threads.append(threading.Thread(target=g.readKey))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
