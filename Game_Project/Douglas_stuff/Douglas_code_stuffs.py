# Douglas code stuff

import time
import os

frames = [
    """
    N   N  EEEEE  V   V  EEEEE  RRRR
    NN  N  E      V   V  E      R   R
    N  NN  EEEE   V   V  EEEE   RRRR
    N   N  E       V V   E      R  R
    N   N  EEEEE    V    EEEEE  R   R
    """,  # "Never"

    """
    GGGG  OOO   N   N  N   N  AAAAA
    G     O  O  NN  N  NN  N  A   A
    G  GG O  O  N N N  N N N  AAAAA
    G   G O  O  N  NN  N  NN  A   A
    GGGG  OOO   N   N  N   N  A   A
    """,  # "Gonna"

    """
    GGGG  III  V   V  EEEEE
    G     III  V   V  E    
    G  GG III  V   V  EEEE 
    G   G III   V V   E    
    GGGG  III    V    EEEEE
    """,  # "Give"

    """
    Y   Y  OOO  U   U
     Y Y  O   O U   U
      Y   O   O U   U
      Y   O   O U   U
      Y    OOO   UUU 
    """,  # "You"

    """
    U   U  PPPP
    U   U  P   P
    U   U  PPPP
    U   U  P
     UUU   P
    """,  # "Up"

    """
    N   N  EEEEE  V   V  EEEEE  RRRR
    NN  N  E      V   V  E      R   R
    N N N  EEEE   V   V  EEEE   RRRR
    N  NN  E       V V   E      R  R
    N   N  EEEEE    V    EEEEE  R   R
    """,  # "Never"

    """
    GGGG  OOO   N   N  N   N  AAAAA
    G     O  O  NN  N  NN  N  A   A
    G  GG O  O  N N N  N N N  AAAAA
    G   G O  O  N  NN  N  NN  A   A
    GGGG  OOO   N   N  N   N  A   A
    """,  # "Gonna"

    """
    L      EEEEE  TTTTT
    L      E        T
    L      EEEE     T
    L      E        T
    LLLLL  EEEEE    T
    """,  # "Let"

    """
    Y   Y  OOO  U   U
     Y Y  O   O U   U
      Y   O   O U   U
      Y   O   O U   U
      Y    OOO   UUU 
    """,  # "You"

    """
    DDDD   OOO  W   W  N   N
    D   D O   O W   W  NN  N
    D   D O   O W W W  N N N
    D   D O   O WW WW  N  NN
    DDDD   OOO  W   W  N   N
    """,  # "Down"

    """
    N   N  EEEEE  V   V  EEEEE  RRRR
    NN  N  E      V   V  E      R   R
    N N N  EEEE   V   V  EEEE   RRRR
    N  NN  E       V V   E      R  R
    N   N  EEEEE    V    EEEEE  R   R
    """,  # "Never"

    """
    GGGG  OOO   N   N  N   N  AAAAA
    G     O  O  NN  N  NN  N  A   A
    G  GG O  O  N N N  N N N  AAAAA
    G   G O  O  N  NN  N  NN  A   A
    GGGG  OOO   N   N  N   N  A   A
    """,  # "Gonna"

    """
    RRRR  U   U  N   N
    R   R U   U  NN  N
    RRRR  U   U  N N N
    R  R  U   U  N  NN
    R   R UUUUU  N   N
    """,  # "Run"

    """
    AAAAA  RRRR   OOO  U   U  N   N  DDDD
    A   A  R   R O   O U   U  NN  N  D   D
    AAAAA  RRRR  O   O U   U  N N N  D   D
    A   A  R  R  O   O U   U  N  NN  D   D
    A   A  R   R  OOO   UUU   N   N  DDDD
    """,  # "Around"

    """
    AAAAA  N   N  DDDD
    A   A  NN  N  D   D
    AAAAA  N N N  D   D
    A   A  N  NN  D   D
    A   A  N   N  DDDD
    """,  # "And"

    """
    DDDD  EEEEE  SSSSS  EEEEE  RRRR  TTTTT
    D   D E      S      E      R   R   T
    D   D EEEE   SSSSS  EEEE   RRRR    T
    D   D E          S  E      R  R    T
    DDDD  EEEEE  SSSSS  EEEEE  R   R   T
    """,  # "Desert"

    """
    Y   Y  OOO  U   U
     Y Y  O   O U   U
      Y   O   O U   U
      Y   O   O U   U
      Y    OOO   UUU 
    """,  # "You"

    """
    N    N  EEEEE  V   V  EEEEE  RRRR
    N N  N  E      V   V  E      R   R
    N  N N  EEEE   V   V  EEEE   RRRR
    N   NN  E       V V   E      R  R
    N    N  EEEEE    V    EEEEE  R   R
    """,  # "Never"

    """
    GGGG   OOO   N   N  N   N  AAAAA
    G     O   O  NN  N  NN  N  A   A
    G  GG O   O  N N N  N N N  AAAAA
    G   G O   O  N  NN  N  NN  A   A
    GGGG   OOO   N   N  N   N  A   A
    """,  # "Gonna"

    """
    M   M  AAAAA  K   K  EEEEE
    MM MM  A   A  K  K   E
    M M M  AAAAA  KKK    EEEE
    M   M  A   A  K  K   E
    M   M  A   A  K   K  EEEEE
    """,  # "Make"

    """
    Y   Y  OOO  U   U
     Y Y  O   O U   U
      Y   O   O U   U
      Y   O   O U   U
      Y    OOO   UUU 
    """,  # "You"

    """
    CCCCC  RRRR  YY YY
    C      R   R  YYY
    C      RRRR    Y
    C      R  R    Y
    CCCCC  R   R   Y
    """,  # "Cry"

    """
    N  N  EEEEE  V   V  EEEEE  RRRR
    N  N  E      V   V  E      R   R
    N  N  EEEE   V   V  EEEE   RRRR
    N  N  E       V V   E      R  R
    NN N  EEEEE    V    EEEEE  R   R
    """,  # "Never"

    """
    GGGG  OOO  N   N  N   N  AAAAA
    G     O  O  NN  N  NN  N  A   A
    G  GG O  O  N N N  N N N  AAAAA
    G   G O  O  N  NN  N  NN  A   A
    GGGG  OOO   N   N  N   N  A   A
    """,  # "Gonna"

    """
    SSSSS  AAAAA  Y   Y
    S      A   A   Y Y
    SSSSS  AAAAA    Y
        S  A   A    Y
    SSSSS  A   A    Y
    """,  # "Say"

    """
    GGGG   OOO   OOO  DDDD   BBBB  Y   Y
    G     O   O O   O D   D  B   B  Y Y
    G  GG O   O O   O D   D  BBBBB   Y
    G   G O   O O   O D   D  B   B   Y
    GGGG   OOO   OOO  DDDD   BBBB    Y
    """,  # "Goodbye"

    """
    N   N  EEEEE  V   V  EEEEE  RRRR
    NN  N  E      V   V  E      R   R
    N N N  EEEE   V   V  EEEE   RRRR
    N  NN  E       V V   E      R  R
    N   N  EEEEE    V    EEEEE  R   R
    """,  # "Never"

    """
    GGGG  OOO   N   N  N   N  AAAAA
    G     O  O  NN  N  NN  N  A   A
    G  GG O  O  N N N  N N N  AAAAA
    G   G O  O  N  NN  N  NN  A   A
    GGGG  OOO   N   N  N   N  A   A
    """,  # "Gonna"

    """
    TTTTT  EEEEE  L     L   
      T    E      L     L     
      T    EEEE   L     L    
      T    E      L     L    
      T    EEEEE  LLLLL LLLLL 
    """,  # "Tell"

    """
    AAAAA     L      I   EEEEE
    A   A     L      I   E    
    AAAAA     L      I   EEEE 
    A   A     L      I   E    
    A   A     LLLLL  I   EEEEE
    """,  # "Lie"

    """
    AAAAA  N   N  DDDD
    A   A  NN  N  D   D
    AAAAA  N N N  D   D
    A   A  N  NN  D   D
    A   A  N   N  DDDD
    """,  # "And"

    """
    H   H  U   U  RRRR  TTTTT  
    H   H  U   U  R   R   T    
    HHHHH  U   U  RRRR    T     
    H   H  U   U  R  R    T     
    H   H  UUUUU  R   R   T    
    """,  # "Hurt"

    """ 
    Y   Y  OOO  U   U
     Y Y  O   O U   U
      Y   O   O U   U
      Y   O   O U   U
      Y    OOO  UUUUU
    """,
]

while True:
    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")  # Clears screen for smooth animation
        print(frame)
        time.sleep(0.5)  # Adjust speed if needed

import time
import os

