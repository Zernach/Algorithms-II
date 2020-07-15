#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # If the receipe calls for more variety of ingredients than stock, 
  # then no batches can be made
  if len(recipe) > len(ingredients):
    return 0
  
  # Else, do some basic division, and round the lowest answer down
  # to return the number of batches that can be made with stock
  ingreds = list(ingredients.keys())
  batch_list = []
  for i in ingreds:
    batch_list.append(ingredients[i] / recipe[i])
  return math.floor(min(batch_list))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))