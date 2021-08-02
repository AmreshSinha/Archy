import os
import time

# https://github.com/AmreshSinha/Archy

print("""\033[1;96m############################################
##### Archy - Automated Arch Installer #####
############################################
For Any Errors open a Issue in Archy Repo
############################################\n\n""")

print("Press a to Start: ")
startKey = str(input())
if startKey != 'a':
    print("Whew. Nvm, We can start again later!")
    os.system(exit())


# Setting Keyboard Layout
keyboardLocales = {
    0: 'by',
    1: 'ca',
    2: 'cf',
    3: 'cz',
    4: 'de',
    5: 'dk',
    6: 'es',
    7: 'et',
    8: 'fa',
    9: 'fi',
    10: 'fr',
    11: 'gr',
    12: 'hu',
    13: 'il',
    14: 'it',
    15: 'lt',
    16: 'lv',
    17: 'mk',
    18: 'nl',
    19: 'no',
    20: 'pl',
    21: 'ro',
    22: 'ru',
    23: 'sg',
    24: 'ua',
    25: 'uk',
    26: 'us'
}
time.sleep(0.5)
print("Keyboard Layout Locales List:\n")
time.sleep(1)
for k,v in keyboardLocales.items():
    print(str(k) + ': ' + str(v)) 
