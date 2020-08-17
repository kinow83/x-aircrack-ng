from flask import Flask, request, render_template
app = Flask(__name__)

'''
def api_params(f):
    @wraps(f)
    def get_post_params(*args, **kwargs):
        if 
'''
def api_param(key):
    if request.method == 'POST':
        return request.form.get('key')
    elif request.method == 'GET':
        return request.args.get(key)
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/x-aireplay-ng')
def v_x_aireplay_ng():
    return render_template('x-aireplay-ng.html')

@app.route('/api/x-aireplay-ng', methods=['GET', 'POST'])
def a_x_aireplay_ng():
    frame_type = api_param('frame_type')
    bssid = api_param('bssid')
    srcmac = ap_param('srcmac')
    dstmac = ap_param('dstmac')
    
    return ""