from flask import Flask
from auth import app_auth
from train import app_train
from upload import app_upload
from friend import app_friend

app=Flask(__name__)


app.register_blueprint(app_auth,url_prefix='/auth')
app.register_blueprint(app_train,url_prefix='/train')
app.register_blueprint(app_upload,url_prefix='/upload')
app.register_blueprint(app_friend,url_prefix='/friend')

@app.route('/')
def index():
    return 'index page'



if __name__=='__main__':

    app.run(debug=True)



