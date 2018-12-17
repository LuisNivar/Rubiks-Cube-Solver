from colorama import Fore, Style


class Cube:
    def __init__(self):
        self.white = ['%dW' % w for w in range(9)]
        self.yellow = [f'{Fore.LIGHTYELLOW_EX}%d%s{Style.RESET_ALL}' % (y, 'Y') for y in range(9)]
        self.red = [f'{Fore.RED}%d%s{Style.RESET_ALL}' % (r, 'R') for r in range(9)]
        self.orange = [f'{Fore.YELLOW}%d%s{Style.RESET_ALL}' % (o, 'O') for o in range(9)]
        self.green = [f'{Fore.GREEN}%d%s{Style.RESET_ALL}' % (g, 'G') for g in range(9)]
        self.blue = [f'{Fore.BLUE}%d%s{Style.RESET_ALL}' % (b, 'B') for b in range(9)]

    def get_nivel(self, nivel=0):
        """Retorna un string que contiene una linea(nivel) con las piezas naranjas, blancas, rojas, amarillas
        respectivamente. primer nivel = 0, segundo nivel = 3, tercer nivel = 6 en un cubo 3x3"""
        linea = ""
        final = nivel + 3
        for o in range(nivel, final):
            linea += self.orange[o] + '  '
        for g in range(nivel, final):
            linea += self.green[g] + '  '
        for r in range(nivel, final):
            linea += self.red[r] + '  '
        for b in range(nivel, final):
            linea += self.blue[b] + '  '
        return linea

    def show(self):
        """ Muestra el estado actual de cada una de las caras en 2D, esta funcion es temporal para comprobar
        el funcionamiento de los algoritmos y sera eliminada una vez implementemos una GUI"""

        # Contador para indicar cuando ir a la siguiente linea
        row_size = 3
        # Mostrando las azules
        for w in self.white:
            # si la linea finalizo
            if row_size == 0:
                #  Reiniciar contador y continuar en la siguiente linea
                row_size = 3
                print('')
            #  Posicionar la capa
            if row_size == 3:
                blk = ' ' * row_size * 4  # El 4 es = Index+Caracter + (dos espacios vacios que dejas)
                print(blk, end='')
            print(w, ' ', end='')
            row_size -= 1
        print('')
        # Mostrando las naranjas, blancas, rojas y amarillas
        for nivel in range(0, 9, 3):
            print(self.get_nivel(nivel))

        row_size = 3  # Reinicio el contador para evitar problemas al imprimir las verdes
        # Mostrando las verdes
        for y in self.yellow:
            # si la linea finalizo
            if row_size == 0:
                #  Reiniciar contador y continuar en la siguiente linea
                row_size = 3
                print('')
            if row_size == 3:
                blk = ' ' * row_size * 4  # El 4 es = Index+Caracter + (dos espacios vacios que dejas)
                print(blk, end='')
            print(y, ' ', end='')
            row_size -= 1
        print('')

    def mov(self, letra):
        if letra == 'R':
            col = self.green[2::3]  # var temporal para almacenar el valor de la verde
            self.green[2::3] = self.yellow[2::3]
            self.yellow[2::3] = reversed(self.blue[::3])
            self.blue[::3] = reversed(self.white[2::3])
            self.white[2::3] = col
            self.red = rot(self.red)
        elif letra == 'L':
            col = reversed(self.yellow[::3])
            self.yellow[::3] = self.green[::3]
            self.green[::3] = self.white[::3]
            self.white[::3] = reversed(self.blue[2::3])
            self.blue[2::3] = col
            self.orange = rot(self.orange, 90)

        elif letra == 'U':
            row = self.green[:3]
            self.green[:3] = self.red[:3]
            self.red[:3] = self.blue[:3]
            self.blue[:3] = self.orange[:3]
            self.orange[:3] = row
            self.white = rot(self.white)
        elif letra == 'D':
            row = self.orange[6:]
            self.orange[6:] = self.blue[6:]
            self.blue[6:] = self.red[6:]
            self.red[6:] = self.green[6:]
            self.green[6:] = row
            self.yellow = rot(self.yellow)
        elif letra == "R'":
            col = self.white[2::3]
            self.white[2::3] = reversed(self.blue[::3])
            self.blue[::3] = reversed(self.yellow[2::3])
            self.yellow[2::3] = self.green[2::3]
            self.green[2::3] = col
            self.red = rot(self.red, -90)
        elif letra == "L'":
            col = self.green[0::3]
            self.green[::3] = self.yellow[::3]
            self.yellow[::3] = reversed(self.blue[2::3])
            self.blue[2::3] = reversed(self.white[::3])
            self.white[::3] = col
            self.orange = rot(self.orange, -90)
        elif letra == "U'":
            row = self.green[:3]
            self.green[:3] = self.orange[0:3]
            self.orange[:3] = self.blue[0:3]
            self.blue[:3] = self.red[0:3]
            self.red[:3] = row
            self.white = rot(self.white, -90)
        elif letra == "D'":
            row = self.green[6:]
            self.green[6:] = self.red[6:]
            self.red[6:] = self.blue[6:]
            self.blue[6:] = self.orange[6:]
            self.orange[6:] = row
            self.yellow = rot(self.yellow,-90)
        elif letra == 'F':
            aux = self.white[6:]
            self.white[6:] = reversed(self.orange[2::3])
            self.orange[2::3] = self.yellow[:3]
            self.yellow[:3] = reversed(self.red[::3])
            self.red[::3] = aux
            self.green = rot(self.green)
        elif letra == 'B':
            aux = reversed(self.white[:3])
            self.white[:3] = self.red[2::3]
            self.red[2::3] = reversed(self.yellow[6:])
            self.yellow[6:] = self.orange[::3]
            self.orange[::3] = aux
            self.blue = rot(self.blue)
        elif letra == "F'":
            aux = reversed(self.white[6:])
            self.white[6:] = self.red[::3]
            self.red[::3] = reversed(self.yellow[:3])
            self.yellow[:3] = self.orange[2::3]
            self.orange[2::3] = aux
            self.green = rot(self.green, -90)
        elif letra == "B'":
            aux = self.white[:3]
            self.white[:3] = reversed(self.orange[::3])
            self.orange[::3] = self.yellow[6:]
            self.yellow[6:] = reversed(self.red[2::3])
            self.red[2::3] = aux
            self.blue = rot(self.blue, -90)
        elif letra == "U2":
            self.green[:3], self.blue[:3] = self.blue[:3], self.green[:3]
            self.red[:3], self.orange[:3] = self.orange[:3], self.red[:3]
            self.white = rot(self.white, 180)
        elif letra == "R2":
            self.white[2::3], self.yellow[2::3] = self.yellow[2::3], self.white[2::3]
            self.green[2::3], self.blue[0::3] = reversed(self.blue[0::3]), reversed(self.green[2::3])
            self.red = rot(self.red, 180)
        elif letra == "L2":
            self.white[::3], self.yellow[::3] = self.yellow[::3], self.white[::3]
            self.red[::3], self.orange[::3] = reversed(self.orange[::3]), reversed(self.red[::3])
            self.orange = rot(self.orange, 180)
        elif letra == "D2":
            self.green[6:], self.blue[6:] = self.blue[6:], self.green[6:]
            self.red[6:], self.orange[6:] = self.orange[6:], self.red[6:]
            self.yellow = rot(self.yellow, 180)
        elif letra == "F2":
            self.white[6:], self.yellow[:3] = reversed(self.yellow[:3]), reversed(self.white[6:])
            self.red[::3], self.orange[2::3] = reversed(self.orange[::3]), reversed(self.red[::3])
            self.green = rot(self.green,180)
        elif letra == "B2":
            self.white[:3], self.yellow[6:] = reversed(self.yellow[6:]), reversed(self.white[:3])
            self.red[2::3], self.orange[::3] = reversed(self.orange[::3]), reversed(self.red[2::3])
            self.blue = rot(self.blue, 180)
        else:
            print("ERROR")

    def mov_sq(self, sequence):
        pasos = sequence.split()
        for p in pasos:
            self.mov(p)


def rot(face, deg=90):
    """Esta funcion rota las caras en 90, 180, -90"""
    face_aux = []
    if deg == 90:
        for i in range(3):
            # Transpone las las columnas, "volteadas" por las filas
            face_aux.extend(reversed(face[i::3]))
    elif deg == -90:
        for i in range(3):
            ''' Aquí coloco el 2-i par aque se intercambien las columnas en orden inverso al de las filas
            esto es porque la rotacion en scmr '''
            face_aux.extend(face[2 - i::3])
    elif deg == 180:
        # Rotacion de 180
        face_aux.extend(reversed(face))
    else:
        # Hmm ... por si acaso
        face_aux = face
    return face_aux


cubo = Cube()
cubo.mov_sq("F2")
cubo.show()

print()