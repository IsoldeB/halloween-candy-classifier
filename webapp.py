import halloween_candy
from flask import Flask, request 
from flask_ngrok import run_with_ngrok
model = halloween_candy.HalloweenCandy("model_halloween_candy.joblib")
model.load_model()
    
app = Flask(__name__)
run_with_ngrok(app)
@app.route('/', methods=('GET', 'POST'))
def html_form():
    return """
    <form action="" method="post">
        <label for="fruity"> fruity </label>
        <input type="checkbox" name="candy" value="fruity" fruity />
        <br />
        <label for="caramel"> caramel</label>
        <input type="checkbox" name="candy" value="caramel" caramel />
        <br />
        <label for="peanutyalmondy"> peanutyalmondy </label>
        <input type="checkbox" name="candy" value="peanutyalmondy" peanutyalmondy />
        <br />
        <label for="nougat"> nougat </label>
        <input type="checkbox" name="candy" value="nougat" nougat />
        <br />
        <label for="crispedricewafer"> crispedricewafer </label>
        <input type="checkbox" name="candy" value="crispedricewafer" crispedricewafer />
        <br />
        <label for="hard"> hard </label>
        <input type="checkbox" name="candy" value="hard" hard />
        <br />
        <label for="bar"> bar </label>
        <input type="checkbox" name="candy" value="bar" bar />
        <br />
        <label for="pluribus"> pluribus </label>
        <input type="checkbox" name="candy" value="pluribus" pluribus />
        <br />
        <label for="sugarpercent"> sugarpercent </label>
        <input type="text" name="sugarpercent" value="sugarpercent" />
        <br />
        <label for="winpercent" winpercent> </label>
        <input type="text" name="winpercent" value="winpercent" />
        <br />
        <label for="pricepercent" pricepercent> </label>
        <input type="text" name="pricepercent" value="pricepercent" />
        <label for="predict"> preddict </label>
        <input type="submit" name="predict" value="predict" /> 
    </form>
    """
def create_html():
    if request.method == 'GET':
        html = html_form()
    else:
        fruity = request.form['fruity']
        caramel = request.form['caramel']
        peanutyalmondy = request.form['peanutyalmondy']
        nougat = request.form['nougat']
        crispedricewafer = request.form['crispedricewafer']
        hard = request.form['hard']
        bar = request.form['bar']
        pluribus = request.form['pluribus']
        sugarpercent = request.form['sugarpercent']
        winpercent = request.form['winpercent']
        pricepercent = request.form['pricepercent']
        if model.is_chocolate(fruity, caramel, peanutyalmondy, nougat, crispedricewafer, hard, bar, pluribus, sugarpercent, winpercent, pricepercent) == true:
            print("Dit snoepje bevat waarschijnlijk chcolade")
        else:
            print("Dit snoepje bevat waarschijnlijk geen chcolade")
            
            
app.run()
create_html()        
        
         
        
        
        
        
                 
        
        
    

