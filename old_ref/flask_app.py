# import dependencies
from flask import Flask, request, redirect, render_template

# initialize the Flask application
app = Flask(__name__)
# map the  main part of you app(/)
@app.route("/")
def sql_database():
    from functions.sqlquery import sql_query

    results = sql_query(""" SELECT * FROM data-table""")
    msg = " SELECT * FROM data-table"
    return render_template("sqldatabase.html", results=results, msg=msg)


# run app behind an if quard
if __name__ == "__main__":
    app.run(debut=True)

