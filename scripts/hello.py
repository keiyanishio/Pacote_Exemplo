#!/usr/bin/env python3
from dev_aberto import hello
from datetime import date, datetime
import babel 
from babel.dates import format_date, format_datetime, format_time
from babel.numbers import format_number
import gettext

 

if __name__ == '__main__':
    gettext.install('cli', localedir='locale')
    
    date, name = hello()
    
    ano = int(date[:4])
    mes = int(date[5:7])
    dia = int(date[8:10])
    hora = int(date[11:13])
    minuto = int(date[14:16])
    segundos = int(date[17:19])
    
    date = datetime(ano, mes, dia, hora, minuto, segundos)
    
    date = format_datetime(date)
    print(_('Último commit feito em:'), _(date), _(' por'), name)
    
