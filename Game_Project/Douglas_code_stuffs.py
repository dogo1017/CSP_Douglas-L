# Douglas code stuff

import time
import os

frames = [
    """
      ########
   ##############
 ##################
####################
####################
 ##################
   ##############
      ########

    """,  # Front-facing coin

    """
       ######
    ############
  ################
 ##################
 ##################
  ################
    ############
       ######

    """,  # Slight tilt

    """
       ######
      ########
    ############
   ##############
   ##############
    ############
      ########
       ######
    """,  # More tilted

    """
       ######
      ########
      ########
     ##########
     ##########
      ########
      ########
       ######

    """,  # Side view (fully rotated)

    """
        ####
       ######
       ######
       ######
       ######
       ######
       ######
        ####
    """,  # Tilting back

    """
         ##
        ####
        ####
        ####
        ####
        ####
        ####
         ##
    """,  # Almost back

    """
         ##
         ##
         ##
         ##
         ##
         ##
         ##
         ##
    """,  # Back to front

    """
         ??
        ????
        ????
        ????
        ????
        ????
        ????
         ??
    """,  # Almost back

    """
        ????
       ??????
       ??????
       ??????
       ??????
       ??????
       ??????
        ????
    """,  # Almost back
    """
       ??????
      ????????
      ????????
     ??????????
     ??????????
      ????????
      ????????
       ??????

    """,  # Side view (fully rotated)
    """
       ??????
      ????????
     ??????????
    ???????????? 
    ???????????? 
     ??????????
      ????????
       ??????
    """,  # More tilted
    """
       ?????? 
    ??????????? 
   ?????????????? 
  ???????????????? 
  ???????????????? 
   ?????????????? 
     ?????????? 
       ??????

    """,  # Slight tilt
        """
      ????????
   ??????????????
 ??????????????????
????????????????????
????????????????????
 ??????????????????
   ??????????????
      ????????

    """,  # Front-facing coin
        """
       ?????? 
    ??????????? 
   ?????????????? 
  ???????????????? 
  ???????????????? 
   ?????????????? 
     ?????????? 
       ??????

    """,  # Slight tilt
     """
       ??????
      ????????
     ??????????
    ???????????? 
    ???????????? 
     ??????????
      ????????
       ??????
    """,  # More tilted
       """
       ??????
      ????????
      ????????
     ??????????
     ??????????
      ????????
      ????????
       ??????

    """,  # Side view (fully rotated)
        """
        ????
       ??????
       ??????
       ??????
       ??????
       ??????
       ??????
        ????
    """,  # Almost back
        """
         ??
        ????
        ????
        ????
        ????
        ????
        ????
         ??
    """,  # Almost back
        """
         ??
         ??
         ??
         ??
         ??
         ??
         ??
         ??
    """,  # Back to front
        """
         ##
        ####
        ####
        ####
        ####
        ####
        ####
         ##
    """,  # Almost back
        """
        ####
       ######
       ######
       ######
       ######
       ######
       ######
        ####
    """,  # Tilting back
        """
       ######
      ########
      ########
     ##########
     ##########
      ########
      ########
       ######

    """,  # Side view (fully rotated)
        """
       ######
      ########
    ############
   ##############
   ##############
    ############
      ########
       ######
    """,  # More tilted

    """
       ######
    ############
  ################
 ##################
 ##################
  ################
    ############
       ######

    """,  # Slight tilt


    
]

while True:
    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")  # Clears screen for smooth animation
        print(frame)
        time.sleep(0.1)  # Adjust speed if needed
