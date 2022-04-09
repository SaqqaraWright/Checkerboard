from flask import Flask, render_template, redirect, request
app = Flask(__name__)





@app.route('/')                           
def checkerboard():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')



@app.route('/<int:x>')                           
def checkerX(x):

    return render_template('x_index.html', x=4)






@app.route('/<int:x>/<int:y>')                           
def checkerXY(x,y):

    return render_template('xy_index.html', x=10, y=10)









if __name__=="__main__":
    app.run(debug=True)