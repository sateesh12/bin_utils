#Author : Sateesh Kalidas
#Date   : 17/June/2022
#Purpose: Based on an input Date and Month of birth, find the Zodiac sign
def zodiac_sign(day,month):
    print('Entered zodiac_sign method code')
    if month == 'december':
        astro_sign = 'Saggitarius' if (day <22) else 'capricon'
    elif month == 'january':
        astro_sign = 'Capricon' if (day < 20) else 'aquarius'
    elif month == 'february':
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 'march':
        astro_sign = 'Pisces' if (day < 20) else 'tarus'
    elif month == 'april':
        astro_sign = 'Aries' if (day < 20) else 'gemini'
    elif month == 'may':
        astro_sign = 'Tarus' if (day < 20) else 'gemini'
    elif month == 'june':
        astro_sign = 'Gemini' if (day < 20) else 'cancer'
    elif month == 'july':
        astro_sign = 'Cancer' if (day < 20) else 'leo'
    elif month == 'august':
        astro_sign = 'Leo' if (day < 20) else 'virgo'
    elif month == 'september':
        astro_sign = 'Virgo' if (day < 20) else 'libra'
    elif month == 'october':
        astro_sign = 'Libra' if (day < 20) else 'scorpio'
    elif month == 'november':
        astro_sign = 'Scorpio' if (day < 20) else 'saggittarius'
    print(astro_sign)


if __name__ == '__main__':
    d = int(input('Enter Day ::>'))
    m = input('Enter Month ::>')
    zodiac_sign(d,m)
