import sys
from time import sleep

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po


# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)

mc.postToChat('オリジナルネザーゲート ')


z = -5
y = param.Y_SEA + 1
for _n in range(15):
    x = 5
    for _i in range(15):
        mc.setBlock(x, y, z,  param.SEA_LANTERN_BLOCK)
        sleep(0.1)
        x -= 1
    z -= 1

z = -10
y = param.Y_SEA + 2
for _n in range(20):
    x = 5
    for _i in range(15):
        mc.setBlock(x, y, z,  param.ODSIDIAN)
        sleep(0.1)
        x -= 1
    y += 1

z = -10
y = param.Y_SEA + 3
for _n in range(18):
    x = 4
    for _i in range(13):
        mc.setBlock(x, y, z,  param.AIR)
        sleep(0.1)
        x -= 1
    y += 1

z = -11
y = param.Y_SEA + 2
for _n in range(20):
    x = 5
    for _i in range(15):
        mc.setBlock(x, y, z,  param.GOLD_BLOCK)
        sleep(0.1)
        x -= 1
    y += 1
