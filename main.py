def on_overlap_tile(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile2, on_overlap_tile)

def on_overlap_tile2(sprite, location):
    startNextLevel()
scene.on_overlap_tile(SpriteKind.player, myTiles.tile4, on_overlap_tile2)

def on_a_pressed():
    newPlayer.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def startNextLevel():
    global newEnemy, currentLevel
    for value in sprites.all_of_kind(SpriteKind.enemy):
        value.destroy(effects.hearts, 200)
    if currentLevel == 0:
        tiles.set_tilemap(tilemap("""
            level_0
        """))
    elif currentLevel == 1:
        tiles.set_tilemap(tilemap("""
            level_1
        """))
    elif currentLevel == 2:
        tiles.set_tilemap(tilemap("""
            level_2
        """))
    else:
        game.over(True)
    tiles.place_on_random_tile(newPlayer, myTiles.tile3)
    for value2 in tiles.get_tiles_by_type(myTiles.tile5):
        newEnemy = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . c c . c c . . . . . . . . 
                            . . f 3 c c 3 c c c . . . . . . 
                            . f c 3 b c 3 b c c c . . . . . 
                            f c b b b b b b b b f f . . . . 
                            c c 1 b b b 1 b b b f f . . . . 
                            c b b b b b b b b c f f f . . . 
                            c b 1 f f 1 c b b f f f f . . . 
                            f f 1 f f 1 f b c c b b b . . . 
                            f f f f f f f b f c c c c . . . 
                            f f 2 2 2 2 f b f b b c c c . . 
                            . f 2 2 2 2 2 b c c b b c . . . 
                            . . f 2 2 2 b f f c c b b c . . 
                            . . . f f f f f f f c c c c c . 
                            . . . . . . . . . . . . c c c c
            """),
            SpriteKind.enemy)
        tiles.place_on_tile(newEnemy, value2)
        newEnemy.follow(newPlayer, 20)
    currentLevel += 1

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    if sprite.bottom < otherSprite.y:
        sprite.vy = -100
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

newEnemy: Sprite = None
currentLevel = 0
newPlayer: Sprite = None
newPlayer = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f . . . . . 
            . . . f f e e e e f 2 f . . . . 
            . . f f e e e e f 2 2 2 f . . . 
            . . f e e e f f e e e e f . . . 
            . . f f f f e e 2 2 2 2 e f . . 
            . . f e 2 2 2 f f f f e 2 f . . 
            . f f f f f f f e e e f f f . . 
            . f f e 4 4 e b f 4 4 e e f . . 
            . f e e 4 d 4 1 f d d e f . . . 
            . . f e e e e e d d d f . . . . 
            . . . . f 4 d d e 4 e f . . . . 
            . . . . f e d d e 2 2 f . . . . 
            . . . f f f e e f 5 5 f f . . . 
            . . . f f f f f f f f f f . . . 
            . . . . f f . . . f f f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(newPlayer, 150, 0)
newPlayer.ay = 500
scene.camera_follow_sprite(newPlayer)
info.set_life(3)
startNextLevel()