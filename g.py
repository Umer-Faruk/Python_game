""" Answer catching game
    """

import pygame
import random
import sys
import time
pygame.init()

screen = pygame.display.set_mode((640, 480))
quastion = ""
optiona = ""
optionb = ""
optionc = ""
optiond = ""
answer = ""
points = 0
clr1 = 1
clr2 = 1
clr3 = 1
# import Read


class Read:
    q_list = []

    def __init__(self):
        self.f = open("1.txt")

    def readfile(self):
        global quastion, optiona, optionb, optionc, optiond, answer

        # time.sleep(3)
        try:
            self.f_line = self.f.readline()

            self.q_list = self.f_line.split(":")  # print(self.q_list)

            quastion = self.q_list[0]

            optiona, optionb, optionc, optiond = self.q_list[
                1], self.q_list[2], self.q_list[3], self.q_list[4]
        except Exception as e:
            pygame.quit()
            print("Game over")
            print("Your score", points)

    # print(self.q_list)


fp = Read()


class Catch(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("plane.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndYay = pygame.mixer.Sound("yay.ogg")
            self.sndThunder = pygame.mixer.Sound("thunder.ogg")
            self.sndEngine = pygame.mixer.Sound("engine.ogg")
            self.sndEngine.play(-1)

    def update(self):
        # readfile()
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, 430)

    #self.image = pygame.transform.flip(self.image, 100, 0)


class Ans(pygame.sprite.Sprite):
    opt = ""

    def __init__(self, opt):
        pygame.sprite.Sprite.__init__(self)
        global optiona, optionb, optionc, optiond
        if opt == "a":
            self.text = optiona
            self.opt = opt
        if opt == "b":
            self.text = optionb
            self.opt = opt
        if opt == "c":
            self.text = optionc
            self.opt = opt

        self.font = pygame.font.SysFont("None", 50)
        self.image = self.font.render(self.text, 1, (clr1, clr2, clr3))
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-20, -20)
        self.reset()

    def update(self):
        global fp, clr
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()

        global optiona, optionb, optionc
        if self.opt == "a":
            self.text = optiona
        if self.opt == "b":
            self.text = optionb
        if self.opt == "c":
            self.text = optionc

        self.image = self.font.render(self.text, 1, (clr1, clr2, clr3))
        self.rect = self.image.get_rect()

    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(0, 5)


class Ocean(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ocean.gif")
        self.rect = self.image.get_rect()
        self.dy = 5
        self.reset()

    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1440:
            self.reset()

    def reset(self):
        self.rect.top = -960
# 3


class Question(pygame.sprite.Sprite):
    global fp

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.SysFont("None", 20)

    def update(self):
        global fp, clr
        # time.sleep(3)

        self.text = "Quastion: %s" % (fp.q_list[0])

        self.image = self.font.render(self.text, 1, (clr1, clr2, clr3))
        self.rect = self.image.get_rect()
###############################################################


class Score(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.SysFont("None", 30)

    def update(self):
        global points
        # time.sleep(3)

       # self.text = "Quastion: %s" % (fp.q_list[0])
    self.text = "score: %d" % points
    self.image = self.font.render(self.text, 1, (clr1, clr2, clr3))
    # print(help(self.image.get_rect))
    self.rect = self.image.get_rect(left=1, top=450)
    # self.rect.move(50,50)
    # Sprint(help(self.rect))
#############################################################


class Answer(pygame.sprite.Sprite):
    opt = ""

    def __init__(self, opt):
        pygame.sprite.Sprite.__init__(self)
        global optiond

        if opt == "d":
            self.text = optiond
            self.opt = opt
            self.font = pygame.font.SysFont("None", 50)
            self.image = self.font.render(self.text, 1, (clr1, clr2, clr3))
            self.rect = self.image.get_rect()
            self.rect.inflate_ip(-20, -20)
            self.reset()

    def update(self):
        global fp
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()

        global optiond

        if self.opt == "d":
            self.text = optiond
            self.image = self.font.render(self.text, 1, (clr1, clr2, clr3))
            self.rect = self.image.get_rect()

    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(0, 2)
####################################################################


def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Answer Catch Game")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    fp.readfile()
    catch = Catch()

    ans1 = Ans("a")
    ans2 = Ans("b")
    ans3 = Ans("c")
    ans4 = Answer("d")
    ocean = Ocean()
    question = Question()
    score = Score()

    friendSprites = pygame.sprite.Group(ocean, catch)
    questionSprite = pygame.sprite.Group(question)
    scoreSprite = pygame.sprite.Group(score)
   # print(help(scoreSprite))

    ansSprites = pygame.sprite.Group(ans1, ans2, ans3)
    asp = pygame.sprite.Group(ans4)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                keepGoing = False

        hitAnss = pygame.sprite.spritecollide(catch, ansSprites, False)
        hit1 = pygame.sprite.spritecollide(catch, asp, False)
        if hitAnss:

            catch.sndThunder.play()
           # print(hitAnss)
           # if question.lives <= 0:
            # print "Game over!"

            for theAns in hitAnss:
                print("nooooooooooooooooooooon")
        # print(theAns)
        #global fp
        # fp.readfile()
                points -= 1
                theAns.reset()
        elif hit1:
            for theAns in hit1:
                print("yesssssssssssssssssssssss")
                # print(theAns)
                global fp, points, clr1, clr2, clr3
                points += 1
                clr1 = 255
                clr2 += 10
                clr3 += 10
                fp.readfile()
                theAns.reset()

        friendSprites.update()

        questionSprite.update()
    asp.update()
    ansSprites.update()
    scoreSprite.update()

    friendSprites.draw(screen)
    ansSprites.draw(screen)
    asp.draw(screen)
    questionSprite.draw(screen)
    scoreSprite.draw(screen)
    pygame.display.flip()

    # return mouse cursor
    pygame.mouse.set_visible(True)
    catch.sndEngine.stop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
