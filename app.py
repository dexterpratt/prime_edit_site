from flask import Flask, render_template, request, send_file
import io
import csv
from funs import fun1, fun2, fun3  # placeholder module

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error_msg = None
    table_data = None
    if request.method == 'POST':
        s = request.form.get('text_field', '')
        try:
            i = int(request.form.get('int_field', 0))
            c = request.form.get('char_field', '')
            ok, msg = fun1(s, i, c)
            if not ok:
                error_msg = msg
            else:
                arr = fun2(s, i, c)    # shape (n,3)
                rows = fun3(arr)     # shape (n,4)
                # Combine and sort by score descending
                #rows = [row + [score] for row, score in zip(arr, scores)] old / MK
                rows.sort(key=lambda x: x[-1], reverse=True)
                table_data = rows
        except Exception:
            import traceback; error_msg = traceback.format_exc()
    return render_template('index.html', error_msg=error_msg, table_data=table_data)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()['data']
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow([f'col{i}' for i in range(1,6)] + ['score'])
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
