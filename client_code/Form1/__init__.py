from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import random
from random import shuffle
from time import sleep
import time
import anvil_extras
import anvil.image

global ansselected
ansselected = False

class Form1(Form1Template):

  #pre form settings
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.quiztextarea1.enabled = False
    self.quiztextarea2.enabled = False
    self.quiztextarea3.enabled = False
    self.advorgtxt.enabled = False

    self.quiztextarea1.foreground = 'black'
    self.quiztextarea2.foreground = 'black'
    self.quiztextarea3.foreground = 'black'
    self.advorgtxt.foreground = 'black'

    self.advorgtxt.background = 'white'

  def quizbutton1_click(self, **event_args):
    self.quizanswerbox1.visible = True
    self.quiztextarea1.visible = True
    self.quizconfirm1.visible = True
    self.quizbutton1.visible = False
    global count
    global ansselected
    global questionNumList
    global points
    ansselected = False
    count = 0
    points = 0
    questionNumList = [-1,-1,-1,-1] #saves question number to prevent repeats
    def quiz1(q1,a01,a02,a03,a04,e1,q2,a11,a12,a13,a14,e2,q3,a21,a22,a23,a24,e3,q4,a31,a32,a33,a34,e4,counts):
      global count
      global ansselected
      global ans
      global points
      ansOrderList = [0,1,2,3] #changes order of answers and keeps track of correct answer
      questionList = [q1,q2,q3,q4]
      answerList = [a01,a02,a03,a04,a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34] #answers are always D
      explanationList = [e1,e2,e3,e4]
      #checks if question has been asked recently
      tcheck = True
      while tcheck is True:
        questionNum = random.randint(0,counts-1)
        if questionNum == questionNumList[-1] or questionNum == questionNumList[-2] or questionNum == questionNumList[-3] or questionNum == questionNumList[-4]:
          pass
        else:
          tcheck = False
          questionNumList.append(questionNum)
      #shuffles/prints answers
      shuffle(ansOrderList)
      print('\n'+questionList[questionNum]+'\n\n'+
            f'A: {answerList[questionNum*4+ansOrderList[0]]}\n'+
            f'B: {answerList[questionNum*4+ansOrderList[1]]}\n'+
            f'C: {answerList[questionNum*4+ansOrderList[2]]}\n'+
            f'D: {answerList[questionNum*4+ansOrderList[3]]}\n')
  

      self.quiz1indicator.visible = True
      
      while self.quiz1indicator.visible:
        time.sleep(0)

      self.quiz1indicator.visible = True

      ans = self.quizanswerbox1.selected_value
      
      try:
        if ansOrderList.index(3)+1 == ord(ans.lower())-96:
          print('\nCorrect!\n\nPress confirm to continue')
          points += 1
        else:
          print(f'\nIncorrect.\n{explanationList[questionNum]}\n\nPress confirm to continue')
      #in input is bad (eg. too long)
      except():
        print(f'\nBad Input.\n{explanationList[questionNum]}\n\nPress confirm to continue')
      
      count += 1

      while self.quiz1indicator.visible:
        time.sleep(0)

      self.quiz1indicator.visible = True
      
      if count == counts:
        print(f'\nYou got {points} out of {counts} correct\n\nPress confirm to complete quiz')

        while self.quiz1indicator.visible:
          time.sleep(0)

        self.quiz1indicator.visible = True
  
        self.quizbutton1.visible = True
        self.quizanswerbox1.visible = False
        self.quiztextarea1.visible = False
        self.quizconfirm1.visible = False
      else:
        quiz1(q1,a01,a02,a03,a04,e1,q2,a11,a12,a13,a14,e2,q3,a21,a22,a23,a24,e3,q4,a31,a32,a33,a34,e4,counts)
    
    def print(texts):
      self.quiztextarea1.text = texts
    
    quiz1('A neural network has', #question 1
        'An input layer, processing layers, and an output layer', #wrong answer
        'An input layer, recognition layers, and an output layer', #wrong answer
        'An input layer, equation layers, and an output layer', #wrong answer
        'An input layer, hidden layers, and an output layer', #right answer
        'A neural network has an input layer, where data in taken in, hidden layers, which are the network\'s neurons, and an output layer, where the final value is outputted', #explanation
    
        'Neural networks can be used for', #question 2
        'Security programs', #wrong answer
        'Facial recongnition systems', #wrong answer
        'Self driving systems', #wrong answer
        'All options apply', #right answer
        'Artificial intelligence is extremely versatile, and can fulfill all of the functions mentioned in the question', #explanation
    
        'Neural Network\'s outputs are based off of the confidence, which appears in the form of:', #question 3
        'A negative number', #wrong answer
        'A positive number', #wrong answer
        'A graph', #wrong answer
        'A percentage', #right answer
        'The confidence is the how sure the AI is of it\'s answer being correct, and is displayed through a percentage value', #explanation
    
        '', #question 4
        '', #wrong answer
        '', #wrong answer
        '', #wrong answer
        '', #right answer
        '', #explanation
    
        3 #number of questions
        )

  def quizconfirm1_click(self, **event_args):
    self.quiz1indicator.visible = False

  #quiz number two
  def quizbutton2_click(self, **event_args):
    global count
    global ansselected
    global questionNumList
    global points
    ansselected = False
    self.quizanswerbox2.visible = True
    self.quiztextarea2.visible = True
    self.quizconfirm2.visible = True
    self.quizbutton2.visible = False
    self.quiz1indicator.visible = True
    count = 0
    points = 0
    questionNumList = [-1,-1,-1,-1] #saves question number to prevent repeats

    def quiz(q1,a01,a02,a03,a04,e1,q2,a11,a12,a13,a14,e2,q3,a21,a22,a23,a24,e3,q4,a31,a32,a33,a34,e4,counts):
      global count
      global ansselected
      global points
      ansOrderList = [0,1,2,3] #changes order of answers and keeps track of correct answer
      questionList = [q1,q2,q3,q4]
      answerList = [a01,a02,a03,a04,a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34] #answers are always D
      explanationList = [e1,e2,e3,e4]
      #checks if question has been asked recently
      tcheck = True
      while tcheck is True:
        questionNum = random.randint(0,counts-1)
        if questionNum == questionNumList[-1] or questionNum == questionNumList[-2] or questionNum == questionNumList[-3] or questionNum == questionNumList[-4]:
          pass
          print('t')
        else:
          tcheck = False
          questionNumList.append(questionNum)
          print('f')
      #shuffles/prints answers
      shuffle(ansOrderList)
      print('\n'+questionList[questionNum]+'\n\n'+
            f'A: {answerList[questionNum*4+ansOrderList[0]]}\n'+
            f'B: {answerList[questionNum*4+ansOrderList[1]]}\n'+
            f'C: {answerList[questionNum*4+ansOrderList[2]]}\n'+
            f'D: {answerList[questionNum*4+ansOrderList[3]]}\n')
      
      #answer input/checking (enter brk to close the code)
      self.quiz2indicator.visible = True
      
      while self.quiz2indicator.visible:
        time.sleep(0)

      self.quiz2indicator.visible = True
      
      ans = self.quizanswerbox2.selected_value
      
      try:
        if ansOrderList.index(3)+1 == ord(ans.lower())-96:
          print('\nCorrect!\n\nPress confirm to continue')
          points += 1
        else:
          print(f'\nIncorrect.\n{explanationList[questionNum]}\n\nPress confirm to continue')
      #in input is bad (eg. too long)
      except():
        print(f'\nIncorrect.\n{explanationList[questionNum]}\n\nPress confirm to continue')
      
      count += 1
      self.quiz2indicator.visible = True
      
      while self.quiz2indicator.visible:
        time.sleep(0)

      self.quiz2indicator.visible = True
      
      if count == counts:
        print(f'\n\nYou got {points} out of {counts} correct\n\nPress confirm to complete quiz')

        self.quiz2indicator.visible = True
        
        while self.quiz2indicator.visible:
          time.sleep(0)
  
        self.quiz2indicator.visible = True

        self.quizbutton2.visible = True
        self.quizanswerbox2.visible = False
        self.quiztextarea2.visible = False
        self.quizconfirm2.visible = False
      else:
        quiz(q1,a01,a02,a03,a04,e1,q2,a11,a12,a13,a14,e2,q3,a21,a22,a23,a24,e3,q4,a31,a32,a33,a34,e4,counts)
    
    def print(texts):
      self.quiztextarea2.text = texts
    
    quiz(
     'To carry out adversarial attacks, it is necessary to...', #question 1
     'Have access to the model', #wrong answer
     'Plant a virus in one of the creator\'s computers', #wrong answer
     'Fool the model by generating an image', #wrong answer
     'Manipulate an input to create a false output', #right answer
     'When creating an adversarial attack, access to the model and viruses are not necessary. Since these adversarial attacks can also apply to inputs such as audio, specifying images only does not cover all cases.', #explanation

     'What is NOT an adversarial attack', #question 2
     'Putting stickers on a sign so an AI could misclassify it', #wrong answer
     'Bending a stop sign so the AI would recognize it wrong', #wrong answer
     'Painting a stop sign green to prevent the AI from recognizing it correctly', #wrong answer
     'Replacing a stop sign with a short one so the AI cannot find it', #right answer
     'Adversarial attacks involve manipulating the input to give a false output, not removing objects from its vision and causing no output', #explanation

     'What is an equation used to generate adversarial attacks', #question 3
     'FSGM', #wrong answer
     'PFGD', #wrong answer
     'PGSE', #wrong answer
     'FGSM', #right answer
     'FGSM, or the fast gradient sign method, is one of the equations used to generate adversarial attacks', #explanation

     'What is one usage of adversarial attacks', #question 4
     'Making cars crash by covering up signs with your scarves', #wrong answer
     'Fooling other people by wearing a very good disguise', #wrong answer
     'Breaking into houses by making cameras think you\'re not there', #wrong answer
     'Fooling a voice detector into thinking you\'re someone else', #right answer
     'The answer is fooling a voice detector, as the input (voice) is manipulated to provide a false output (that someone else is speaking)', #explanation

     4 #number of questions
     )

  #quiz number three
  def quizbutton3_click(self, **event_args):
    global count
    global ansselected
    global questionNumList
    global points
    ansselected = False
    self.quizanswerbox3.visible = True
    self.quiztextarea3.visible = True
    self.quizconfirm3.visible = True
    self.quizbutton3.visible = False
    count = 0
    points = 0
    questionNumList = [-1,-1,-1,-1] #saves question number to prevent repeats

    def quiz(q1,a01,a02,a03,a04,e1,q2,a11,a12,a13,a14,e2,q3,a21,a22,a23,a24,e3,q4,a31,a32,a33,a34,e4,counts):
      global count
      global ansselected
      global points
      ansOrderList = [0,1,2,3] #changes order of answers and keeps track of correct answer
      questionList = [q1,q2,q3,q4]
      answerList = [a01,a02,a03,a04,a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34] #answers are always D
      explanationList = [e1,e2,e3,e4]
      #checks if question has been asked recently
      tcheck = True
      while tcheck is True:
        questionNum = random.randint(0,counts-1)
        if questionNum == questionNumList[-1] or questionNum == questionNumList[-2] or questionNum == questionNumList[-3] or questionNum == questionNumList[-4]:
          pass
        else:
          tcheck = False
          questionNumList.append(questionNum)
      #shuffles/prints answers
      shuffle(ansOrderList)
      print('\n'+questionList[questionNum]+'\n\n'+
            f'A: {answerList[questionNum*4+ansOrderList[0]]}\n'+
            f'B: {answerList[questionNum*4+ansOrderList[1]]}\n'+
            f'C: {answerList[questionNum*4+ansOrderList[2]]}\n'+
            f'D: {answerList[questionNum*4+ansOrderList[3]]}\n')
      
      #answer input/checking (enter brk to close the code)
      self.quiz3indicator.visible = True
      
      while self.quiz3indicator.visible:
        time.sleep(0)

      self.quiz3indicator.visible = True
      
      ans = self.quizanswerbox3.selected_value
      
      try:
        if ansOrderList.index(3)+1 == ord(ans.lower())-96:
          print('\nCorrect!\n\nPress confirm to continue')
          points += 1
        else:
          print(f'\nIncorrect.\n{explanationList[questionNum]}\n\nPress confirm to continue')
      #in input is bad (eg. too long)
      except():
        print(f'\nIncorrect.\n{explanationList[questionNum]}\n\nPress confirm to continue')
      
      count += 1
      self.quiz3indicator.visible = True
      
      while self.quiz3indicator.visible:
        time.sleep(0)

      self.quiz3indicator.visible = True
      
      if count == counts:
        print(f'\n\nYou got {points} out of {counts} correct\n\nPress confirm to complete quiz')

        self.quiz3indicator.visible = True
        
        while self.quiz3indicator.visible:
          time.sleep(0)
  
        self.quiz3indicator.visible = True

        self.quizbutton3.visible = True
        self.quizanswerbox3.visible = False
        self.quiztextarea3.visible = False
        self.quizconfirm3.visible = False
      else:
        quiz(q1,a01,a02,a03,a04,e1,q2,a11,a12,a13,a14,e2,q3,a21,a22,a23,a24,e3,q4,a31,a32,a33,a34,e4,counts)
    
    def print(texts):
      self.quiztextarea3.text = texts
    
    quiz('What is a backdoor', #question 1
     'A piece of code hidden in a neural network allowing for hackers to remotely access it', #wrong answer
     'Malicious software hidden in a neural network that can compromise your device', #wrong answer
     'Code that warps the input of a neural network to always create false outputs', #wrong answer
     'Changing aspects of the training model to manipulate the output of one trained using it', #right answer
     'A backdoor works through manipulating a training model in various ways so any model trained using that model will have an ouput different than originally intended. This can be used in malicious ways.', #explanation

     'What phase of training are backdoors implemented into the neural network', #question 2
     'Testing the model', #wrong answer
     'Deploying the model',
     'Overviewing the model',
     'Training the model',
     'Backdoors are implented during the training process',

     'How much data has to be poisoned in order to create a backdoor', #question 3
     '80%', #wrong answer
     '50%', #wrong answer
     '20%', #wrong answer
     '>1%', #right answer
     'Depending on the sample size and trigger, even less than one percent of the data being poisoned can create a pronounced effect.', #explanation

     'What is one way backdoors are implemented', #question 4
     'Through using a poisoned data set to train your model', #wrong answer
     'Through a virus remotely placed into the neural network', #wrong answer
     'Through a hacker corrupting the data in the model remotely', #wrong answer
     'All of the above', #right answer
     'Backdoors can be implemented in a large number of ways, with the only requirement being the corruption of the model. This can be carried out through hacking, viruses, etc.', #explanation

     4 #number of questions
     )

  def quizconfirm3_click(self, **event_args):
    self.quiz3indicator.visible = False

  #link to form
  def outlined_button_1_click(self, **event_args):
    self.adgameimg1.visible = True

  #adversarial attack or original image activity
  def activityadvorg1_click(self, **event_args):
    global adoconf
    global correct
    global list
    correct = 0
    self.grid_panel_1.visible = True
    self.activityadvorg1.visible = False
    adoconf = False
    list = [1,2,3,4,5]
    shuffle(list)
    def startadvorg1game():
      def print(texts):
        self.advorgtxt.text = texts
      print('Select which one you think is the original image')
      global adoconf
      global correct
      global list
      self.switch_1.visible = True
      self.switch_2.visible = True
      try:
        if list[0] == 1:
          self.ddimg1.visible = True
          self.ddimg2.visible = True
          self.ddimg1.source = "_/theme/ddtruckadvimg.png"
          self.ddimg2.source = "_/theme/ddtruckorgimg.png"     
          while adoconf is False:
            pass
          adoconf = False
          self.ddimg1.visible = False
          self.ddimg2.visible = False        
          if self.switch_1.checked is True:
            correct += 1
            print('Correct! Press confirm to continue')
          else:
            print('Incorrect. Press confirm to continue')
          self.image_4.source = "_/theme/truckadvcomp.png"
          self.image_4.visible = True
          while adoconf is False:
            pass
          self.image_4.visible = False
          adoconf = False
          self.switch_1.checked = False
          self.switch_2.checked = False
          list.pop(0)
          startadvorg1game()
  
        if list[0] == 2:
          self.ddimg1.visible = True
          self.ddimg2.visible = True
          self.ddimg1.source = "_/theme/dddeerorgimg1.png"
          self.ddimg2.source = "_/theme/dddeerorgimg1.png"     
          while adoconf is False:
            pass
          adoconf = False
          self.ddimg1.visible = False
          self.ddimg2.visible = False        
          if self.switch_2.checked is True:
            correct += 1
            print('Correct! Press confirm to continue')
          else:
            print('Incorrect. Press confirm to continue')
          self.image_4.source = "_/theme/deeradvcomp1.png"
          self.image_4.visible = True
          while adoconf is False:
            pass
          self.image_4.visible = False
          adoconf = False
          self.switch_1.checked = False
          self.switch_2.checked = False
          list.pop(0)
          startadvorg1game()
  
        if list[0] == 3:
          self.ddimg1.visible = True
          self.ddimg2.visible = True
          self.ddimg1.source = "_/theme/dddeeradvimg2.png"
          self.ddimg2.source = "_/theme/dddeerorgimg2.png"     
          while adoconf is False:
            pass
          adoconf = False
          self.ddimg1.visible = False
          self.ddimg2.visible = False         
          if self.switch_1.checked is True:
            correct += 1
            print('Correct! Press confirm to continue')
          else:
            print('Incorrect. Press confirm to continue')
          self.image_4.source = "_/theme/deeradvcomp2.png"
          self.image_4.visible = True
          while adoconf is False:
            pass
          self.image_4.visible = False
          adoconf = False
          self.switch_1.checked = False
          self.switch_2.checked = False
          list.pop(0)
          startadvorg1game()
  
        if list[0] == 4:
          self.ddimg1.visible = True
          self.ddimg2.visible = True
          self.ddimg1.source = "_/theme/ddshiporgimg2.png"
          self.ddimg2.source = "_/theme/ddshipadvimg2.png"     
          while adoconf is False:
            pass
          adoconf = False
          self.ddimg1.visible = False
          self.ddimg2.visible = False      
          if self.switch_2.checked is True:
            correct += 1
            print('Correct! Press confirm to continue')
          else:
            print('Incorrect. Press confirm to continue')
          self.image_4.source = "_/theme/shipadvcomp2.png"
          self.image_4.visible = True
          while adoconf is False:
            pass
          self.image_4.visible = False
          adoconf = False
          self.switch_1.checked = False
          self.switch_2.checked = False
          list.pop(0)
          startadvorg1game()

        if list[0] == 5:
          self.ddimg1.visible = True
          self.ddimg2.visible = True
          self.ddimg1.source = "_/theme/ddshipadvimg1.png"
          self.ddimg2.source = "_/theme/ddshiporgimg1.png"     
          while adoconf is False:
            pass
          adoconf = False       
          self.ddimg1.visible = False
          self.ddimg2.visible = False
          if self.switch_1.checked is True:
            correct += 1
            print('Correct! Press confirm to continue')
          else:
            print('Incorrect. Press confirm to continue')
          self.image_4.source = "_/theme/shipadvcomp1.png"
          self.image_4.visible = True
          while adoconf is False:
            pass
          self.image_4.visible = False
          adoconf = False
          self.switch_1.checked = False
          self.switch_2.checked = False
          list.pop(0)
          startadvorg1game()
      except:
        self.switch_1.visible = False
        self.switch_2.visible = False
        print(f'You got {correct} out of 5. Press confirm to continue')
        while adoconf is False:
          pass
        adoconf = False
        self.conado.visible = False
        self.grid_panel_1.visible = False
        self.activityadvorg1.visible = True
    startadvorg1game()

  def switch_1_change(self, **event_args):
    if self.switch_1.checked is True:
      self.switch_2.checked = False
    else:
      self.switch_2.checked = True

  def switch_2_change(self, **event_args):
    if self.switch_2.checked is True:
      self.switch_1.checked = False
    else:
      self.switch_1.checked = True

  def conado_click(self, **event_args):
    global adoconf
    adoconf = True

  #neural network activity

  def nnslider_change(self, handle, **event_args):
    if self.nnactsetd.selected_value == '1':
      if self.nnslider.value == 1:
        self.nntrainedtextdisp.text = "Trained with 500 images"
        self.nnimg.source = '_/theme/500imge1.png'
      elif self.nnslider.value == 2:
        self.nntrainedtextdisp.text = "Trained with 1000 images"
        self.nnimg.source = '_/theme/1000imge1.png'
      elif self.nnslider.value == 3:
        self.nntrainedtextdisp.text = "Trained with 3000 images"
        self.nnimg.source = '_/theme/3000imge1.png'
      elif self.nnslider.value == 4:
        self.nntrainedtextdisp.text = "Trained with 7000 images"
        self.nnimg.source = '_/theme/7000imge1.png'
      elif self.nnslider.value == 5:
        self.nntrainedtextdisp.text = "Trained with 12000 images"
        self.nnimg.source = '_/theme/12000imge1.png'
      elif self.nnslider.value == 7:
        self.nntrainedtextdisp.text = "Trained with 48000 images"
        self.nnimg.source = '_/theme/48000imge1.png'
      else:
        self.nntrainedtextdisp.text = "Trained with 24000 images"
        self.nnimg.source = '_/theme/24000imge1.png'
    if self.nnactsetd.selected_value == '2':
      if self.nnslider.value == 1:
        self.nntrainedtextdisp.text = "Trained with 500 images"
        self.nnimg.source = '_/theme/500imge2.png'
      elif self.nnslider.value == 2:
        self.nntrainedtextdisp.text = "Trained with 1000 images"
        self.nnimg.source = '_/theme/1000imge2.png'
      elif self.nnslider.value == 3:
        self.nntrainedtextdisp.text = "Trained with 3000 images"
        self.nnimg.source = '_/theme/3000imge2.png'
      elif self.nnslider.value == 4:
        self.nntrainedtextdisp.text = "Trained with 7000 images"
        self.nnimg.source = '_/theme/7000imge2.png'
      elif self.nnslider.value == 5:
        self.nntrainedtextdisp.text = "Trained with 12000 images"
        self.nnimg.source = '_/theme/12000imge2.png'
      elif self.nnslider.value == 7:
        self.nntrainedtextdisp.text = "Trained with 48000 images"
        self.nnimg.source = '_/theme/48000imge2.png'
      else:
        self.nntrainedtextdisp.text = "Trained with 24000 images"
        self.nnimg.source = '_/theme/24000imge2.png'
    if self.nnactsetd.selected_value == '3':
      if self.nnslider.value == 1:
        self.nntrainedtextdisp.text = "Trained with 500 images"
        self.nnimg.source = '_/theme/500imge3.png'
      elif self.nnslider.value == 2:
        self.nntrainedtextdisp.text = "Trained with 1000 images"
        self.nnimg.source = '_/theme/1000imge3.png'
      elif self.nnslider.value == 3:
        self.nntrainedtextdisp.text = "Trained with 3000 images"
        self.nnimg.source = '_/theme/3000imge3.png'
      elif self.nnslider.value == 4:
        self.nntrainedtextdisp.text = "Trained with 7000 images"
        self.nnimg.source = '_/theme/7000imge3.png'
      elif self.nnslider.value == 5:
        self.nntrainedtextdisp.text = "Trained with 12000 images"
        self.nnimg.source = '_/theme/12000imge3.png'
      elif self.nnslider.value == 7:
        self.nntrainedtextdisp.text = "Trained with 48000 images"
        self.nnimg.source = '_/theme/48000imge3.png'
      else:
        self.nntrainedtextdisp.text = "Trained with 24000 images"
        self.nnimg.source = '_/theme/24000imge3.png'

  def nnactsetd_change(self, **event_args):
    if self.nnactsetd.selected_value == '1':
      if self.nnslider.value == 1:
        self.nntrainedtextdisp.text = "Trained with 500 images"
        self.nnimg.source = '_/theme/500imge1.png'
      elif self.nnslider.value == 2:
        self.nntrainedtextdisp.text = "Trained with 1000 images"
        self.nnimg.source = '_/theme/1000imge1.png'
      elif self.nnslider.value == 3:
        self.nntrainedtextdisp.text = "Trained with 3000 images"
        self.nnimg.source = '_/theme/3000imge1.png'
      elif self.nnslider.value == 4:
        self.nntrainedtextdisp.text = "Trained with 7000 images"
        self.nnimg.source = '_/theme/7000imge1.png'
      elif self.nnslider.value == 5:
        self.nntrainedtextdisp.text = "Trained with 12000 images"
        self.nnimg.source = '_/theme/12000imge1.png'
      elif self.nnslider.value == 7:
        self.nntrainedtextdisp.text = "Trained with 48000 images"
        self.nnimg.source = '_/theme/48000imge1.png'
      else:
        self.nntrainedtextdisp.text = "Trained with 24000 images"
        self.nnimg.source = '_/theme/24000imge1.png'
    if self.nnactsetd.selected_value == '2':
      if self.nnslider.value == 1:
        self.nntrainedtextdisp.text = "Trained with 500 images"
        self.nnimg.source = '_/theme/500imge2.png'
      elif self.nnslider.value == 2:
        self.nntrainedtextdisp.text = "Trained with 1000 images"
        self.nnimg.source = '_/theme/1000imge2.png'
      elif self.nnslider.value == 3:
        self.nntrainedtextdisp.text = "Trained with 3000 images"
        self.nnimg.source = '_/theme/3000imge2.png'
      elif self.nnslider.value == 4:
        self.nntrainedtextdisp.text = "Trained with 7000 images"
        self.nnimg.source = '_/theme/7000imge2.png'
      elif self.nnslider.value == 5:
        self.nntrainedtextdisp.text = "Trained with 12000 images"
        self.nnimg.source = '_/theme/12000imge2.png'
      elif self.nnslider.value == 7:
        self.nntrainedtextdisp.text = "Trained with 48000 images"
        self.nnimg.source = '_/theme/48000imge2.png'
      else:
        self.nntrainedtextdisp.text = "Trained with 24000 images"
        self.nnimg.source = '_/theme/24000imge2.png'
    if self.nnactsetd.selected_value == '3':
      if self.nnslider.value == 1:
        self.nntrainedtextdisp.text = "Trained with 500 images"
        self.nnimg.source = '_/theme/500imge3.png'
      elif self.nnslider.value == 2:
        self.nntrainedtextdisp.text = "Trained with 1000 images"
        self.nnimg.source = '_/theme/1000imge3.png'
      elif self.nnslider.value == 3:
        self.nntrainedtextdisp.text = "Trained with 3000 images"
        self.nnimg.source = '_/theme/3000imge3.png'
      elif self.nnslider.value == 4:
        self.nntrainedtextdisp.text = "Trained with 7000 images"
        self.nnimg.source = '_/theme/7000imge3.png'
      elif self.nnslider.value == 5:
        self.nntrainedtextdisp.text = "Trained with 12000 images"
        self.nnimg.source = '_/theme/12000imge3.png'
      elif self.nnslider.value == 7:
        self.nntrainedtextdisp.text = "Trained with 48000 images"
        self.nnimg.source = '_/theme/48000imge3.png'
      else:
        self.nntrainedtextdisp.text = "Trained with 24000 images"
        self.nnimg.source = '_/theme/24000imge3.png'


  def nnactivityb_click(self, **event_args):
    self.grid_panel_3.visible = True
    self.nnactivityb.visible = False

  def nnactivitybcomp_click(self, **event_args):
    self.grid_panel_3.visible = False
    self.nnactivityb.visible = True

  def backdoorslider_change(self, handle, **event_args):
    if self.backdoordropdown.selected_value == '1x10':
      if self.backdoorslider.value == 1:
        self.imgdispbackdoor.source = '_/theme/backdoor1-1.png'
      elif self.backdoorslider.value == 2:
        self.imgdispbackdoor.source = '_/theme/backdoor1-2.png'
      elif self.backdoorslider.value == 3:
        self.imgdispbackdoor.source = '_/theme/backdoor1-3.png'
      elif self.backdoorslider.value == 4:
        self.imgdispbackdoor.source = '_/theme/backdoor1-4.png'
      elif self.backdoorslider.value == 5:
        self.imgdispbackdoor.source = '_/theme/backdoor1-5.png'
      elif self.backdoorslider.value == 6:
        self.imgdispbackdoor.source = '_/theme/backdoor1-6.png'
    if self.backdoordropdown.selected_value == '10x10':
      if self.backdoorslider.value == 1:
        self.imgdispbackdoor.source = '_/theme/backdoor2-1.png'
      elif self.backdoorslider.value == 2:
        self.imgdispbackdoor.source = '_/theme/backdoor2-2.png'
      elif self.backdoorslider.value == 3:
        self.imgdispbackdoor.source = '_/theme/backdoor2-3.png'
      elif self.backdoorslider.value == 4:
        self.imgdispbackdoor.source = '_/theme/backdoor2-4.png'
      elif self.backdoorslider.value == 5:
        self.imgdispbackdoor.source = '_/theme/backdoor2-5.png'
      elif self.backdoorslider.value == 6:
        self.imgdispbackdoor.source = '_/theme/backdoor2-6.png'
    if self.backdoordropdown.selected_value == '5x5':
      if self.backdoorslider.value == 1:
        self.imgdispbackdoor.source = '_/theme/backdoor3-1.png'
      elif self.backdoorslider.value == 2:
        self.imgdispbackdoor.source = '_/theme/backdoor3-2.png'
      elif self.backdoorslider.value == 3:
        self.imgdispbackdoor.source = '_/theme/backdoor3-3.png'
      elif self.backdoorslider.value == 4:
        self.imgdispbackdoor.source = '_/theme/backdoor3-4.png'
      elif self.backdoorslider.value == 5:
        self.imgdispbackdoor.source = '_/theme/backdoor3-5.png'
      elif self.backdoorslider.value == 6:
        self.imgdispbackdoor.source = '_/theme/backdoor3-6.png'

  def backdoordropdown_change(self, **event_args):
    if self.backdoordropdown.selected_value == '1x10':
      if self.backdoorslider.value == 1:
        self.imgdispbackdoor.source = '_/theme/backdoor1-1.png'
      elif self.backdoorslider.value == 2:
        self.imgdispbackdoor.source = '_/theme/backdoor1-2.png'
      elif self.backdoorslider.value == 3:
        self.imgdispbackdoor.source = '_/theme/backdoor1-3.png'
      elif self.backdoorslider.value == 4:
        self.imgdispbackdoor.source = '_/theme/backdoor1-4.png'
      elif self.backdoorslider.value == 5:
        self.imgdispbackdoor.source = '_/theme/backdoor1-5.png'
      elif self.backdoorslider.value == 6:
        self.imgdispbackdoor.source = '_/theme/backdoor1-6.png'
    if self.backdoordropdown.selected_value == '10x10':
      if self.backdoorslider.value == 1:
        self.imgdispbackdoor.source = '_/theme/backdoor2-1.png'
      elif self.backdoorslider.value == 2:
        self.imgdispbackdoor.source = '_/theme/backdoor2-2.png'
      elif self.backdoorslider.value == 3:
        self.imgdispbackdoor.source = '_/theme/backdoor2-3.png'
      elif self.backdoorslider.value == 4:
        self.imgdispbackdoor.source = '_/theme/backdoor2-4.png'
      elif self.backdoorslider.value == 5:
        self.imgdispbackdoor.source = '_/theme/backdoor2-5.png'
      elif self.backdoorslider.value == 6:
        self.imgdispbackdoor.source = '_/theme/backdoor2-6.png'
    if self.backdoordropdown.selected_value == '5x5':
      if self.backdoorslider.value == 1:
        self.imgdispbackdoor.source = '_/theme/backdoor3-1.png'
      elif self.backdoorslider.value == 2:
        self.imgdispbackdoor.source = '_/theme/backdoor3-2.png'
      elif self.backdoorslider.value == 3:
        self.imgdispbackdoor.source = '_/theme/backdoor3-3.png'
      elif self.backdoorslider.value == 4:
        self.imgdispbackdoor.source = '_/theme/backdoor3-4.png'
      elif self.backdoorslider.value == 5:
        self.imgdispbackdoor.source = '_/theme/backdoor3-5.png'
      elif self.backdoorslider.value == 6:
        self.imgdispbackdoor.source = '_/theme/backdoor3-6.png'

  def bdactivity_button_click(self, **event_args):
    self.grid_panel_5.visible = True
    self.bdactivity_button.visible = False

  def bdcompact_click(self, **event_args):
    self.grid_panel_5.visible = False
    self.bdactivity_button.visible = True

  def quizconfirm2_click(self, **event_args):
    self.quiz2indicator.visible = False

  def returnhome_click(self, **event_args):
    open_form('HomePage')
