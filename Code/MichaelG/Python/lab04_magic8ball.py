#Version 1
import random
answer = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
          'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again',
          'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
          'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good,', 'Very doubtful']

print('Welcome')
cont = "yes"
#Version 2
while cont == 'yes':
    output = random.choice(answer)
    question = input('Ask a question. ')
    print(output)
    cont = input('Do you wish to ask another question? ')
    if cont == 'no':
        break

