from random import shuffle
from sys import exit


game_name = ["geometry dash","minecraft","battleblock theater","legend of zelda", "cookie clicker","doom","pizza tower","among us","moonbase alpha","stardew valley"]

game_moji = ["⏹️🏃‍🔼","⛏️👷‍♂️","💥⏹️🎥","🔼🔼🔼🧝⚔️", "🍪👆","🧟😈🔫","🇮🇹🍕🧱","ඞ","🧑‍🚀🏈","🐔🧑‍🌾🌠"]

game_hint = ["geometry was one of my favorite subjects, i'm glad they made a game out of it!","my brother plays the crap out of this game! i cant get a handle of it, but i dont mine at all.",\
             "i love the little cat things in this game, i have exactly 1283 of them in my steam inventory! though i never actually ever... beat this game...","this game has the best nonverbal charactor since 1986"\
                , "this was one of the top ten games played on unblocked websites! by who's mectrics? what are you, a cop?","local italan goes into poverty, 362 injured 2 dead","what a strange symbol, dont you think?\
 how could such a simple shape cause so much psycic damage?", "some guy on youtube said this game provides a realistic simulation of life on a natural satellite. that's a good source, right? aeiou",\
    "to be honest, i also never beat this game. not much of a people person."]

wrong_ans = [["the impossible game","bit. trip","diep.io"],["fortnite","terraria","deep rock galactic"],["godzilla vs king kong","The Lego Movie Videogame","ultrakill"],["helldivers", "totally awesome battle simulator","balders gate 3"],["papa's cookieria","cookies inc.","squid games"],\
["call of duty zombies", "plants vs zombies", "resident evil"],["papa's pizzaria","super mario bros.","infinite pizza"], ["no. why.", "fall guys","[####] you."],["universe sandbox","space station 13","kerbal space program"],["coral island", "farming simulator 22","animal crossing"]]

question_list=[]
hint_count = 3


print("Welcome to... GameMoji!")
print("guess the game name from borderline hierogliphics")
print("you get 3 hints. say 'hint' when answering to use.")

for game in range(len(game_name)):
   
   while True:
      print()
      print()
      print("Question "+str(game+1)+": ")
      print("what's the game's name?")
      print(game_moji[game])
      print()
      question_list = []
      question_list.append(game_name[game])
      question_list.extend(wrong_ans[game])
      shuffle(question_list)
      for i in range(len(question_list)):
         print(str(i+1)+". "+question_list[i])
      print()
      print("*you have "+str(hint_count)+" hints left")
      p_input=input("(enter your answer by typing 1-4 or use a hint by typing 'hint')>> ")
      print()
      
      if p_input == "hint":
         if hint_count >0:
            print(game_hint[game])
            hint_count-=1
         else:
            print("you're out of hints bud.")
   
      elif int(p_input)>0:
         try:
            if question_list[int(p_input)-1] == game_name[game]:
               print("Correct!")
               break
            else:
               print("Incorrect!")
               print("ok off the stage, no doovers, you had your fun, now GET")
               exit()
         except IndexError:
            print("i uh didnt quite get that. only numbers 1-4 and hint, got it?")
         1
      else:
         print("i uh didnt quite get that. only numbers 1-4 and hint, got it?")
print("oh uh that's the last one....")
print("dont... really have anything...")
print("...")
print("ok off the stage, no doovers, you had your fun, now GET")
