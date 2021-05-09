from flask import Flask, render_template  
app = Flask(__name__)                     
    
@app.route('/play')                           
def hello_world():
    return render_template('index.html')  

@app.route('/play/<boxes>')
def numBoxes(boxes):
    howMany = int(boxes)
    return render_template('indexBoxes.html', howMany = howMany)
    
@app.route('/play/<boxes>/<color>')
def numAndColor(boxes, color):
    howMany = int(boxes)
    return render_template('indexColor.html', howMany = howMany, color = color)


if __name__=="__main__":
    app.run(debug=True)                   