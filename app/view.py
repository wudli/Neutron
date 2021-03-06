from app import app
from flask import request, jsonify, send_from_directory
from .baidu_api import recognize, synthesize
from .turing_api import turing_robot


@app.route('/')
def index():
    return 'Test Page'


@app.route('/upload_voice', methods=['POST', 'GET'])
def upload_voice():
    # f = open('app/hello.wav', 'rb')
    f = request.files['voice']
    recognize_result = recognize(f)
    print("Recognize result: {}".format(recognize_result))
    resp_message = turing_robot(recognize_result)
    print("Respond message: {}".format(resp_message))
    is_succeed, save_file_name = synthesize(resp_message)
    return jsonify(
        {
            'code': 0,
            'message': 'ok',
            'recognize_result': recognize_result,
            'save_file_name': save_file_name
        }
    )


@app.route('/voice/<filename>')
def get_voice(filename):
    return send_from_directory(
        directory='return_voice',
        filename=filename
    )
