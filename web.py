from flask import Flask, render_template
import yaml

app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('bugging1.yaml', 'r') as file:
        data = yaml.safe_load(file)['bugging']

    docker_data = add_serial_numbers(data, 'docker')
    helm_data = add_serial_numbers(data, 'helm')
    checkov_data = add_serial_numbers(data, 'checkov')

    return render_template('dashboard.html', docker_data=docker_data, helm_data=helm_data, checkov_data=checkov_data)

def add_serial_numbers(data, policy_type):
    filtered_data = [entry for entry in data if policy_type in entry['namespace']]
    for i, entry in enumerate(filtered_data, start=1):
        entry['serial'] = i
    return filtered_data

if __name__ == '__main__':
    app.run(debug=True)
