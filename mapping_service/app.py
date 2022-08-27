from flask import Flask

import config
from api.views.IncidentsOfficers import main_api


app = Flask(__name__)
app.register_blueprint(main_api)

if __name__=="__main__":
    app.run(host=config.HOST, port=int(config.PORT), debug=True)
