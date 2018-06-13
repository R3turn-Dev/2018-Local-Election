from elections import *
from json import dumps

open("parsed/Sidojisa.json", "w", encoding="UTF-8").write(dumps(Sidojisa().parse()))
open("parsed/GusiGun.json", "w", encoding="UTF-8").write(dumps(GusiGun().parse()))
open("parsed/SidoYehwe.json", "w", encoding="UTF-8").write(dumps(SidoYehwe().parse()))
open("parsed/GusigunYehwe.json", "w", encoding="UTF-8").write(dumps(GusigunYehwe().parse()))