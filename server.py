from flask import Flask , render_template, request, redirect, session
import random
import datetime
now = datetime.datetime.now()

print
print "Current date and time using str method of datetime object:"
print str(now)

app=Flask(__name__)
app.secret_key='lkjhfdfsdfs'

@app.route('/')
def index():

    if 'gold' not in session:
        session['gold']=0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route("/process_money", methods=["POST"])
def process():
    if 'gold' not in session:
        session['gold']=0
    if request.form['building'] == 'farm':
        gold = random.randrange(10,21)
        session['gold'] += gold
        session['activities'].append("Earned {} gold from the farm {})".format(int(gold),str(now)))
    elif request.form['building'] == 'cave':
        gold = random.randrange(5,11)
        session['gold'] += gold
        session['activities'].append("Earned {} gold from the cave {})".format(int(gold),str(now)))
    elif request.form['building'] == 'house':
        gold = random.randrange(2,6)  
        session['gold'] += gold
        session['activities'].append("Earned {} gold from the house {})".format(int(gold),str(now)))
    elif request.form['building'] == 'casino':
        gold = random.randrange(-51,51)
        session['gold'] += gold
        session['activities'].append("Earned {} gold from the casino {})".format(int(gold),str(now)))
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
app.run(debug=True)