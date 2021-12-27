#!/usr/bin/env python2

from flask import Flask, Response, request, render_template, request
from random import choice, randint
from string import lowercase
from functools import wraps


app = Flask(__name__)

def calc(recipe):
	global garage
	garage = {}
    # garage has access to all global variables, recipe does not
    # because garage is equal to {}
	try: exec(recipe, garage)
	except: pass

def GCR(func): # Great Calculator of the observable universe and it's infinite timelines
	@wraps(func)
	def federation(*args, **kwargs):
        # initialize ingredient / recipe to default values
        # concatenate 10 random lowercase characters
		ingredient = ''.join(choice(lowercase) for _ in range(10))
		GET_recipe = '%s = %s' % (ingredient, ''.join(map(str, [randint(1, 69), choice(['+', '-', '*']), randint(1,69)])))

        # get ingredient / measurements from POST request
        # meaning to put how much (measurement) for a specific ingredient in a recipe
		if request.method == 'POST':
			ingredient = request.form.get('ingredient', '')
			POST_recipe = '%s = %s' % (ingredient, request.form.get('measurements', ''))
			calc(POST_recipe)
            # print all globals vars via garage to the client
			return render_template('index.html', calculations=garage)

        # exploit is executed here
		calc(GET_recipe)

		# if garage.get(ingredient, ''):
		# 	return render_template('index.html', calculations=garage[ingredient])

		return func(*args, **kwargs)
	return federation

@app.route('/', methods=['GET', 'POST'])
@GCR
def index():
	return render_template('index.html')

@app.route('/debug')
def debug():
	return Response(open(__file__).read(), mimetype='text/plain')

if __name__ == '__main__':
	app.run('0.0.0.0', port=1337)