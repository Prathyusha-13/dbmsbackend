from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import oracledb
import queries as q

app = Flask(__name__)
CORS(app)
cs = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=oracle.cise.ufl.edu)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SID=orcl)))"
connection = oracledb.connect(
user='batchalakuri.p',
password='7FUCj8ODtylibgRcDYlPYeuC',
dsn=cs)

cursor = connection.cursor()
print("Successfully connected to Oracle Database")

users = dict()
users["admin@admin.com"]={"name": "admin", "password": "admin"}

@app.route('/login', methods=['POST'])
def get_token():
    print("login user request received !")
    credentials = request.get_json()
    print(credentials)
    print(q.login.format(credentials["username"], credentials["password"]))
    res = cursor.execute(q.login.format(credentials["username"], credentials["password"]))
    if list(res)[0][0] == 1:
        print("user authenticated !")
        return jsonify(
            isError=False,
            message="Success",
            statusCode=200,
            data={"token": "12346"}),200
    else:
        return jsonify(
            isError=False,
            message="Unauthenticated",
            statusCode=200,
            data={"token": "unAuth"}),200

@app.route('/register', methods=['POST'])
def register():
    print("new registration received !")
    data = request.get_json()
    #users[data["username"]]={"name": data["name"], "password":data["password"]}
    
    res = cursor.execute(q.register.format(data["username"], data["password"]))
    cursor.execute('commit')
    
    return jsonify(
        isError=False,
        message="Success",
        statusCode=200),200

    
    
@app.route('/mockup_5', methods = ['POST'])
def get_data5():

    #mockup_1_2 doesnt have any parameters
    ##Send SQL query - TODO
    data = request.get_json()
    # ##Query
    res = cursor.execute(q.mockup_5.format(data["country"],  data["from"], data["to"]))
    
    data_db = dict()
    data_db['x']=[]
    data_db['y1']=[]
    for row in res:
        data_db['x'].append(row[0])
        data_db['y1'].append(row[1])

    ##Parse SQL query and Send JSON object back with x and y data for graph - TODO
    if not data_db['x'] or not data_db['y1']:
        data_db={}
    if not data_db['x'] or not data_db['y1']:
        data_db={}
    return jsonify(
        isError=False,
        message="Success",
        statusCode=200,
        data=data_db),200
    

    

    

    
if __name__ == '__main__':
    app.run(debug=True)  
    

    

    
    

    
    