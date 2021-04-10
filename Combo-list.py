import re
print(
"""   ______    By JOKER    __             
  / ____/___  ____ ___  / /_  ____      
 / /   / __ \/ __ `__ \/ __ \/ __ \     
/ /___/ /_/ / / / / / / /_/ / /_/ /     
\____/\____/_/ /_/ /_/_.___/\____/      
                                  LIST
 Mode:
  1- Email filtering
  2- Combo Maker  [ email:pass ]
  3- Combo Maker  [ user:pass  ]
  4- To get out
""")
joker = input('[+] Enter mode : ')
if joker == '1':
  print('   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
  print("""
    1- gmail   | 2- yahoo | 3- hotmail 
    4- outlook | 5- live  | 6- mail
  
  7- If the domain does not exist, type 7
    """)
  mml = input('[+] Enter the domain number : ')
  print(' ')
  if mml == '1':
    eml = input('Enter name file : ')
    print(' ')
    try:
      lst = open(eml, 'r')
      while True:
        lste = lst.readline().split('\n')[0]
        if re.search("(@gmail)", lste) :
          gmail = lste
          print(gmail)
          with open('gmail.txt', 'a') as x:
            x.write(gmail + '\n')
    except FileNotFoundError:
      print('[!] Please enter a file name !')
  elif mml == '2':
    eml = input('Enter name file : ')
    print(' ')
    try:
      lst = open(eml, 'r')
      while True:
        lste = lst.readline().split('\n')[0]
        if re.search("(@yahoo)", lste) :
          yahoo = lste
          print(yahoo)
          with open('yahoo.txt', 'a') as x:
            x.write(yahoo + '\n')
    except FileNotFoundError:
      print('[!] Please enter a file name !')
  elif mml == '3':
    eml = input('Enter name file : ')
    print(' ')
    try:
      lst = open(eml, 'r')
      while True:
        lste = lst.readline().split('\n')[0]
        if re.search("(@hotmail)", lste) :
          hotmail = lste
          print(hotmail)
          with open('hotmail.txt', 'a') as x:
            x.write(hotmail + '\n')
    except FileNotFoundError:
      print('[!] Please enter a file name !')
  elif mml == '4':
    eml = input('Enter name file : ')
    print(' ')
    try:
      lst = open(eml, 'r')
      while True:
        lste = lst.readline().split('\n')[0]
        if re.search("(@outlook)", lste) :
          outlook = lste
          print(outlook)
          with open('outlook.txt', 'a') as x:
            x.write(outlook + '\n')
    except FileNotFoundError:
      print('[!] Please enter a file name !')
  elif mml == '5':
    eml = input('Enter name file : ')
    print(' ')
    try:
      lst = open(eml, 'r')
      while True:
        lste = lst.readline().split('\n')[0]
        if re.search("(@live)", lste) :
          live = lste
          print(live)
          with open('live.txt', 'a') as x:
            x.write(live + '\n')
    except FileNotFoundError:
      print('[!] Please enter a file name !')
  elif mml == '6':
    eml = input('Enter name file : ')
    print(' ')
    try:
      lst = open(eml, 'r')
      while True:
        lste = lst.readline().split('\n')[0]
        if re.search("(@mail)", lste) :
          mail = lste
          print(mail)
          with open('mail.txt', 'a') as x:
            x.write(mail + '\n')
    except FileNotFoundError:
      print('[!] Please enter a file name !')
  elif mml == '7':
    dome = input('Enter the domain : @ ')
    eml = input('Enter name file : ')
    print(' ')
    try:
      lst = open(eml, 'r')
      while True:
        lste = lst.readline().split('\n')[0]
        if re.search(f"(@{dome})", lste) :
          non = lste
          print(non)
          with open(f'{dome}.txt', 'a') as x:
            x.write(non + '\n')
    except FileNotFoundError:
      print('[!] Please enter a file name !')
  else:
    print('\n\t\t\tBy JOKER @vv1ck')

elif joker == '2':
  eml = input('[+] Enter the name of the e-mail file : ')
  pess = input('[+] Enter the name of the password file : ')
  try:
    lst = open( eml , 'r')
    pe = open( pess , 'r')
    print(' ')
    while True:
      mel = lst.readline().split('\n')[0]
      pes = pe.readline().split('\n')[0]
      if mel == '':
        print('\n[+] Successfully completed')
        print('[+] Saved to email-List.txt file')
        input('[+] Press Enter to exit')
        exit()
      if pes == '':
        print('\n[+] Successfully completed')
        print('[+] Saved to email-List.txt file')
        input('[+] Press Enter to exit')
        exit()
      print(mel+ ':' +pes)
      with open('Combo-List.txt', 'a') as x:
        x.write(mel+ ':' +pes+'\n')
  except FileNotFoundError:
    print('[!] Please enter a file name !')

elif joker == '3':
  eml = input('[+] Enter the username file : ')
  pess = input('[+] Enter the name of the password file : ')
  try:
    lst = open( eml , 'r')
    pe = open( pess , 'r')
    print(' ')
    while True:
      mel = lst.readline().split('\n')[0]
      pes = pe.readline().split('\n')[0]
      if mel == '':
        print('\n[+] Successfully completed')
        print('[+] Saved to user-List.txt file')
        input('[+] Press Enter to exit')
        exit()
      if pes == '':
        print('\n[+] Successfully completed')
        print('[+] Saved to user-List.txt file')
        input('[+] Press Enter to exit')
        exit()
      print(mel+ ':' +pes)
      with open('user-List.txt', 'a') as x:
        x.write(mel+ ':' +pes+'\n')
  except FileNotFoundError:
    print('[!] Please enter a file name !')
else:
    print('\n\t\t\tBy JOKER @vv1ck')
