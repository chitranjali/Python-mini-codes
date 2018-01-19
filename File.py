import os
import random
from collections import OrderedDict

def make_A_file(answer_key,quiznum):
   os.makedirs('Answers_fol', exist_ok=True)
   count = 1
   with open('Answers_fol/key%d.txt' %(quiznum), 'w') as test:
      for corr_ans in answer_key:
         test.write('{}.{}\n'.format(count,corr_ans))
         count = count + 1
   test.close()

def get_questions(capitals,quiznum):
   quest = {} #Loop through all 50 states, making a question for each.
   for questionNum in range(50)
   answer_key = [] # KeyS for answers
   for key in capitals:
      choices = [random.choice(list(capitals.values())), random.choice(list(capitals.values())),
                 random.choice(list(capitals.values())), capitals[key]]
      choices = random.sample(choices, len(choices))
      answer_key.append('ABCD'[choices.index(capitals[key])])
      quest[('What is the capital of {}'.format(key))] = choices

   make_A_file(answer_key,quiznum)
   # Shuffle the dictionary items and then make it to ordered Dict.( As we can't shuffle dictionary keys directly)
   items = quest.items()
   return OrderedDict(random.sample(list(items), len(list(items))))

def make_Q_file(quests,quiznum):
    os.makedirs('Questions_fol', exist_ok=True)
    ques_count = 1
    with open('Questions_fol/QuizFile%d.txt' %(quiznum), 'w') as QuizFile:
       # Header for Question File
       QuizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
       QuizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiznum))
       QuizFile.write('\n\n')

       for question in quests:
          QuizFile.write( '\n%s %s\n' %(ques_count,question))
          for option in quests[question]:
             QuizFile.write('%s %s\n' %('ABCD'[quests[question].index(option)],option))
          ques_count = ques_count + 1
    QuizFile.close()


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New mexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(35):
   quests = get_questions(capitals,quiznum + 1)
   make_Q_file(quests,quiznum + 1)

print('Generated question and answer files')



