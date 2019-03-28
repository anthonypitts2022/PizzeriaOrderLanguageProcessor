# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:03:48 2019

@author: antho
"""

#place order; choose pizza, salad, or done
def select_meal(): 
    order = 'You ordered ' #full order string
    choiceOfMeal = '' #user input to pizza vs salad
    firstObject = True #allows for grammatical and in between orders
    while(choiceOfMeal.lower() != "done"):
        choiceOfMeal = input("Hello would you like pizza or salad? ")
        #gets pizza order string through function calls
        if(choiceOfMeal.lower()=="pizza"):
            if(firstObject==True):
                order = order + pizza()
                print (order + ". Place another order or say 'done'")  
                firstObject = False
            else:
                order = order+ ' and '+ pizza()
                print (order + ". Place another order or say 'done'") 
        #gets salad order String through function calls
        elif(choiceOfMeal.lower()=="salad"):
            if(firstObject==True):
                order = order + salad()
                print (order + ". Place another order or say 'done'")  
                firstObject = False
            else:
                order = order+ ' and '+ salad()
                print (order + ". Place another order or say 'done'") 
        #if the user said 'done'
        else:
            print('Your order has been placed. Goodbye')
            return

#chooses pizza size
def pizza():
    sizeOfPizza = input("small, medium, or large: ")
    return 'A ' + sizeOfPizza + ' pizza with'+ toppings()

#choosing toppings type
def toppings():
    toppingString = ''
    toppingChoice = ''
    toppingNumber = 0
    while (toppingChoice.lower()!='done'):
      toppingChoice = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done': ")  
      if(toppingChoice.lower()!='done'):
          if(toppingNumber!=0):
              toppingString = toppingString + ' and ' + toppingChoice
              toppingNumber=toppingNumber+1
          else:
              toppingString = toppingString+ ' ' + toppingChoice
              toppingNumber=toppingNumber+1
    return toppingString

#chooses salad type
def salad(): 
    typeOfSalad = input("Would you like a garden salad or greek salad? ")
    return 'A ' + typeOfSalad + ' salad with ' + dressing()

#chooses dressing type
def dressing():
    dressingChoice = input("Please choose a dressing: vinaigrette, ranch, blue, cheese, lemon. ")  
    return dressingChoice
      
select_meal()