#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Movimenta no eixo X (horizontal)

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.moving_up = False  # Inicialmente, o inimigo está se movendo para baixo
        self.speed_y = ENTITY_SPEED[self.name]  # Velocidade inicial no eixo Y

    def move(self):
        # Movimento horizontal (da direita para a esquerda)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical (subindo e descendo)
        if self.moving_up:
            # Se estiver subindo, mova para cima
            self.rect.centery -= self.speed_y

            # Se atingir a borda superior, inverte o movimento para descer com o dobro da velocidade
            if self.rect.top <= 0:
                self.moving_up = False
                self.speed_y *= 2  # Desce com o dobro da velocidade
        else:
            # Se estiver descendo, mova para baixo
            self.rect.centery += self.speed_y

            # Se atingir a borda inferior, inverte o movimento para subir
            if self.rect.bottom >= WIN_HEIGHT:
                self.moving_up = True
                self.speed_y = ENTITY_SPEED[self.name]  # Volta para a velocidade normal ao subir

    def shoot(self):
        return super().shoot()
