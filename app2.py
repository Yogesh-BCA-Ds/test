from flask import *
import sqlite3

conn = sqlite3.connect("sample.db")

app = Flask(__name__)

@app.route("/students",methods=['POST'])
def add_students():
    data = request.get_json()
    name = data['name']
    course = data['course']
    email = data['email']
    conn = sqlite3.connect("sample.db")
    conn.execute("insert into students (name,course,email) values (?,?,?)",(name,course,email))
    conn.commit()
    conn.close()
    return jsonify({
               "success":True,
               "message":"data added successfully",
               }),201
@app.route("/students",methods=["GET"])
def get_students():
    conn = sqlite3.connect("sample.db")
    students = conn.execute("select * from students").fetchall()
    conn.close()
    r = []
    for i in students:
        r.append({"id":i[0],
        "name":i[1],
        "course":i[2],
        "email":i[3]})    
    return jsonify(r),200

@app.route("/students/<int:id>",methods=["PUT"])
def update(id):
    data = request.get_json()
    name = data['name']
    course = data['course']
    email = data['email']
    conn = sqlite3.connect("sample.db")
    conn.execute("update students set name=?,course=?,email=? where id=?",(name,course,email,id))
    conn.commit()
    conn.close()
    return jsonify({'message':"successfully updated"})

@app.route("/students/<int:id>",methods = ['DELETE'])
def delete(id):
    conn = sqlite3.connect("sample.db")
    conn.execute("delete from students where id = ?",(id,))
    conn.commit()
    conn.close()
    return jsonify({"message":"data deleted successfully"})
    
if __name__ == '__main__':
    app.run(debug=True)
