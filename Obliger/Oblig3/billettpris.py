'''ASSIGNMENT 3'''
#Variabels
ticketPrice = 0
priceList = {'child':30,'adult':50,'elder':35}
total = 0

#User class
class User:
    def __init__(self):
        name = input('\nMy name is ')
        age = input('My age is ')
        if age.isdigit():
            self.name = name
            self.age = age
        else:
            print(age," is not a valid integer.")

#Functions
def feedback (group):
    print(str(priceList[group]),'NOK for ',group)

#Game
ordering = True
while ordering:
    amount = input('\nHow many people are you? We are ')
    isDigit = amount.isdigit()
    if isDigit:
        users = [User() for x in range(0,int(amount))]
        for x in users:
            if 17 >= int(x.age) > 0:
                total += priceList['child']
                feedback('child')
            elif 17 < int(x.age) < 63:
                total += priceList['adult']
                feedback('adult')
            elif int(x.age) > 63:
                total +=priceList['elder']
                feedback('elder')
        print('You have to pay: ',total,'NOK')
    else:
        print('The following is not an integer : ',amount)

    '''Helt syk bra prosedyre!!!
    Alt som kan sies om dette mesterverket er at det suger.
    Til tross for en kjedelig while løkke, så antar jeg at det kunne vært verre.
    1. Orket ikke, og manglet kunnskap til å avbryte ordering løkken fra classen
    dersom brukeren skrev noe annet enn et tall...
    2. I tillegg lagres ikke disse verdiene for senere bruk...
    3. De kan ikke bli henntet ut...
    4. Jeg gadd heller ikke å lage en prisliste som brukeren ser først
    5. osv...

    Uff... grusomt, men det får duge for oppgavebestillingen...
    Her er en vits:


A wife send her husband an sms on a cold winter evening: "Windows frozen".
The husband send answer back: "Pour some warm water over them".
Some time later husband receives answer from his wife: "The computer is completely fucked now".


... en annen vits hvis den første ikke gjorde jobben.


A man flying in a hot air balloon suddenly realizes he’s lost.
He reduces height and spots a man down below.
He lowers the balloon further and shouts to get directions,
"Excuse me, can you tell me where I am?"
The man below says: "Yes. You're in a hot air balloon, hovering 30 feet above this field."
"You must work in Information Technology," says the balloonist.
"I do" replies the man. "How did you know?"
"Well," says the balloonist, "everything you have told me is technically correct,
but It's of no use to anyone."
The man below replies, "You must work in management."
"I do," replies the balloonist, "But how'd you know?"
"Well", says the man, "you don’t know where you are or where you’re going,
but you expect me to be able to help.
You’re in the same position you were before we met, but now it’s my fault."

... siste, jeg lover!

A young Programmer and his Project Manager board a train headed through the mountains on its way to Wichita.
They can find no place to sit except for two seats right across the aisle from a young woman and her grandmother.
After a while, it is obvious that the young woman and the young programmer are interested in each other,
because they are giving each other looks. Soon the train passes into a tunnel and it is pitch black.
There is a sound of a kiss followed by the sound of a slap.
When the train emerges from the tunnel, the four sit there without saying a word.
The grandmother is thinking to herself,
"It was very brash for that young man to kiss my granddaughter,
but I'm glad she slapped him."
The Project manager is sitting there thinking,
"I didn't know the young tech was brave enough to kiss the girl,
but I sure wish she hadn't missed him when she slapped me!"
The young woman was sitting and thinking, "I'm glad the guy kissed me,
but I wish my grandmother had not slapped him!"
The young programmer sat there with a satisfied smile on his face. He thought to himself,
"Life is good.
How often does a guy have the chance to kiss a beautiful girl
and slap his Project manager all at the same time!"
'''
