num=int(input("how many genres would you like to generate?"))
again=("y")
prefixlist=["hyper","dark","bubblegum","lofi","indie","noise","electro","synth","new-age","drone","kawaii","emo","bro","future","psychedelic","industrial","techno","disco","acid","old-school","minimal","masochist","reassuring","social media","post-instrumental","fan service","post-apocalyptic","1920's","pre-death of whitney houston","cringe","trad","drunk","christian","soft","art","hard","neo-classical","surf","medieval","doomer","pyramid scheme","celtic","death","capitalist","pirate","viking","astronaut","space","goth","commie","machiavellian","lovecraftian","horror","chaos"]
suffixlist=["metal","ambient","dance","pop","folk","blues","swing","drill","dnb","punk","house","rock","step","hip-hop","soul","gaze", "trance","hardcore","trap","country","funk","jazz","grunge","garage","jungle","city pop","j-pop","bass","beat","ska","reggae","grind","chant","yodeling"]
import random
while again==("y"):
    while num > 0:
        print(random.choice(prefixlist), end = ' ')
        print(random.choice(suffixlist))
        num-=1
    again=input("again?(y/n)")
    if again==("n"):
        num=0
        print("sláinte!")
    elif again==("y"):
        num=int(input("how many genres would you like to generate?"))