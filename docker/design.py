from flask import Flask, render_template, request, jsonify
import requests
import json
design = Flask(__name__)
lambda_function_endpoint = 'https://g5h3ff4t34.execute-api.ap-northeast-1.amazonaws.com/default/all-methods-function'

@design.route('/')
def home():
    return render_template('home.html')

@design.route('/add')
def index():
    return render_template('add.html')


@design.route('/get')
def get():
    return render_template('get.html')

@design.route('/delete')
def delete():
    return render_template('delete.html')


@design.route('/get_data', methods=['POST'] )
def submit_post():
    user_name = request.form.get('user_name')
    
    data = {
	"user_name":user_name
    }

    data1=json.dumps(data)


    headers = {
    "Content-Type": "application/json"
    }
    
    
    response = requests.get(lambda_function_endpoint, data=data1 ,headers=headers )

    if response.status_code == 200:
        prettified_data = json.dumps(response.text, indent=2)
        return render_template('get_response.html', result=json.loads(prettified_data))
    else:
        prettified_data = json.dumps(response.text, indent=2)
        return render_template('get_response.html', result=json.loads(prettified_data))



@design.route('/add_data', methods=['POST' , 'GET'])
def submit_add():
    
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    data = {
	"user_name":user_name,
	"email": email
    }

    data1=json.dumps(data)


    headers = {
    "Content-Type": "application/json"
    }
    
    response = requests.post(lambda_function_endpoint, data=data1 ,headers=headers )
    
    
    if response.status_code == 200:
        success_message = "User registered successfully!"
        return render_template('add.html', message=success_message, message_type='success')
    else:
        return jsonify({'status': 'error', 'message': 'Error occurred while registering the user.'})





@design.route('/delete_data', methods=['POST' , 'GET'])
def submit_delete():
    # Get data from the form
    user_name = request.form.get('user_name')
    email = request.form.get('email')

    data = {
	"user_name":user_name,
	"email": email
    }

    data1=json.dumps(data)

    headers = {
    "Content-Type": "application/json"
    }

    response = requests.delete(lambda_function_endpoint, data=data1 ,headers=headers )
    

    if response.status_code == 200:
        success_message = "User Deleted successfully!"
        return render_template('delete.html', message=success_message, message_type='success')
    else:
        return jsonify({'status': 'error', 'message': 'Error occurred while deleting the user.'})



if __name__ == '__main__':
    design.run(port=5000,host="0.0.0.0")
