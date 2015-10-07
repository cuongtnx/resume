from flask.ext.frozen import Freezer
from resume import app


freezer = Freezer(app)
if __name__ == '__main__':
    freezer.freeze()
    # freezer.run(debug=True)
