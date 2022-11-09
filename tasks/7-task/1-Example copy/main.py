import time
import pprint

hour = time.localtime().tm_hour
year = time.localtime().tm_year
day = time.localtime().tm_mday
mount = time.localtime().tm_mon


def hourFormat(hour: int):
    if hour > 12:
        return f' {hour - 12} pm'

    return f' {hour} pm'


hora = hourFormat(hour)

print('hoy es ', day, '/', mount, '/', year, ', hora ', hourFormat(hour))
print(f'y faltan {19-hour} horas para salir')
