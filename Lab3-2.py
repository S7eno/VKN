import sys
sys.stdout.write('задайте координату х першої точки ')
bar = sys.stdin.readline()
sys.stdout.write('задайте координату у другої точки ')
foo = sys.stdin.readline()
Bar = str((((0 - int(bar)) ** 2) + ((0 - int(foo)) ** 2)) ** 0.5)
Bar1 = str(((((0 - int(bar)) - int(bar)) ** 2) + ((0 - 0) ** 2)) ** 0.5)
sys.stdout.write('довжина AB = ' + Bar)
sys.stdout.write(' довжина BC = ' + Bar1)
