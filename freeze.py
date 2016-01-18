from flask.ext.frozen import Freezer
from resume import app


freezer = Freezer(
    app=app,
    with_static_files=True
    )

if __name__ == '__main__':
    freezer.freeze()
