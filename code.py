import random 

album = input('Which album would you like to listen to?\n Enter 1 for Blunderbuss or 2 for Lazaretto.\n')

Blunderbuss = ["Missing Pieces","Sixteen Saltines","Freedom at 21","Love Interruption","Blunderbuss", "Hypocritical Kiss","Weep Themselves to Sleep","I'm Shakin'","Trash Tongue Talker","Hip (Eponymous) Poor Boy","I Guess I Should Go to Sleep","On and On and On","Take Me with You When You Go"]             

Lazaretto = ["Three Women","Lazaretto","Temporary Ground","Would You Fight for My Love?","High Ball Stepper","Just One Drink","Alone in My Home","Entitlement","That Black Bat Licorice","I Think I Found the Culprit","Want and Able"]
              
def choose_song():
    if album == "1":
              print(random.choice(Blunderbuss))
    if album == "2":
              print(random.choice(Lazaretto))
    else: print("Please select from the two albums by typing in "1" or "2". I will add more ASAP. Love, Jack.")
            
choose_song()

        
## Need to add the rest of the albums for this to be a complete program. However, these two albums are definitely the best. 
## Although... this program doesn't include my all time favorite Jack White song, a White Stripes ditty called "I Think I Smell A Rat." 

