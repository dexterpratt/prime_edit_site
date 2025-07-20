from flask import Flask, render_template, request, send_file
import io
import csv
from funs import validate_inputs, generate_triples, score_triples

app = Flask(__name__)

DEFAULTS = {
    'text_field': 'AGCTAGCTAGCTAGCTAGCT',
    'int_field': 5,
    'char_field': 'A'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    error_msg = None
    table_data = None
    form_data = DEFAULTS.copy()
    if request.method == 'POST':
        form_data['text_field'] = request.form.get('text_field', DEFAULTS['text_field'])
        try:
            form_data['int_field'] = int(request.form.get('int_field', DEFAULTS['int_field']))
        except Exception:
            form_data['int_field'] = DEFAULTS['int_field']
        form_data['char_field'] = request.form.get('char_field', DEFAULTS['char_field'])
        ok, msg = validate_inputs(form_data['text_field'], form_data['int_field'], form_data['char_field'])
        if not ok:
            error_msg = msg
        else:
            triples = generate_triples(form_data['text_field'], form_data['int_field'], form_data['char_field'])
            rows = score_triples(triples)
            rows.sort(key=lambda x: x[-1], reverse=True)
            table_data = rows
    return render_template('index.html', error_msg=error_msg, table_data=table_data, **form_data)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()['data']
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['Spacer', 'PBS', 'RTT', 'Score'])
    cw.writerows(data)
    mem = io.BytesIO()
    mem.write(si.getvalue().encode('utf-8'))
    mem.seek(0)
    return send_file(mem,
                     mimetype='text/csv',
                     as_attachment=True,
                     download_name='results.csv')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
