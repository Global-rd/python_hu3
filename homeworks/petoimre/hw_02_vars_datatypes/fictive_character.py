'''
Exercise one
Fictive character
'''
# Task-1 
character_name = (input("Type in your name: ")).title().strip()                # Bekért név, egyből nagybetűssé tesz és szóközöket kivesz
character_age = int(input("Give me how old are you: "))                        # Bekért kor egyből int-be, mert számolunk vele
character_experience = input("How much experience do you have in Python? ")    # Bekért exp. Marad str, mert nem számolunk vele
character_age_in_day = character_age*365                                       # Évekből napok száma
character_profil = f"My character is lives {character_age_in_day} days ago. His/her name is {character_name} and he/she has {character_experience} years experience in Python."      # Az egészet összefűz
print(character_profil)                                                        # print

# Extra task
character_want_prof = input("Do you want to became professional Python developer? Please answer yes or no: ") # Kérdés
character_want_prof = "" if character_want_prof == "yes" else "doesn't"                                       # yes-> semmi, else-> doesn't
character_want_prof = f"{character_profil} He/she {character_want_prof} wants to be Python developer."        # Összefűz
print(character_want_prof)                                                                                    # Print
# end


