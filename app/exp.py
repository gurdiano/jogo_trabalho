# figuras geo 

pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50))
pygame.draw.circle(tela, (0, 0, 200), (300, 260), 40)
pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)


if event.type == KEYDOWN:
            if event.key  == K_a:
                x -= 20
            if event.key  == K_d:
                x += 20
            if event.key  == K_w:
                y -= 20
            if event.key  == K_s:
                y += 20

if event.type == KEYDOWN:
            if event.key  == K_a:
                x = x - 20
            if event.key  == K_d:
                x = x + 20
            if event.key  == K_w:
                y = y - 20
            if event.key  == K_s:
                y = y + 20