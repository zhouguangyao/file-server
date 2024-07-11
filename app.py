from flask import Flask, request, jsonify, send_file, url_for
from io import BytesIO
from flask import Flask, send_file
import os
from urllib.parse import quote
from urllib.parse import unquote
from flask_cors import CORS
from werkzeug.utils import secure_filename




app = Flask(__name__)
# 设置文件上传的目标文件夹
UPLOAD_FOLDER = '/Users/zhouguangyao/uploads/'
# UPLOAD_FOLDER = '/mnt/file-server/uploads/'
# UPLOAD_FOLDER = '/portrait/dmp/ruishi/user/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 创建上传文件夹
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# 初始化 CORS 扩展
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def hello():
    return 'hello'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        # 使用原始文件名，而不是secure_filename，以保留中文
        filename = file.filename
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(f'upload filepath: {filepath}')
        file.save(filepath)
        return jsonify({'filepath': filepath}), 200

# @app.route('/stream/<file_path>', methods=['GET'])
# def stream_file(file_path):
#     # 对中文文件名进行解码
#     # filename = quote(filename).replace('%25', '%')
#     # 对中文文件名进行解码
#     # filename = unquote(filename).encode('utf-8').decode('utf-8')
#     # file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     # if os.path.exists(file_path):
#     #     return send_file(file_path, as_attachment=True)
#     # else:
#     #     return '文件不存在'

@app.route('/stream/<path:filepath>', methods=['GET'])
def stream_file(filepath):
    # 确保文件路径是有效的
    if not os.path.exists('/'+filepath):
        return jsonify({'error': 'File not found'}), 404

    # 发送文件
    print(f'stream filepath: {filepath}')
    return send_file('/'+filepath, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

