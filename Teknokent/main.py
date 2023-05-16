import os
from flask import Flask, render_template, render_template_string, jsonify
import teknokent_scraper as tns

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
    ret = """<ul>
        <li><a href='/bilisim_vadisi'>4 - Bilişim Vadisi</a> &#10003;(offline, firma ünvanı var, tam adı yok, selenium docker sorunu)</li>
        <li><a href='/kapadokya'>13 - Kapadokya</a> (firma isimleri resim)</li>
        <li><a href='/adu'>24 - ADÜ Teknokent</a> (DHTML yükleme sorunu, selenium docker sorunu)</li>
        <li><a href='/bogazici'>31 - Boğaziçi Teknokent</a> &#10003;(tutarsız çalışma, tekrar çağırmak gerekebiliyor)</li>
        <li><a href='/cumhuriyet'>35 - Cumhuriyet Teknokent</a> &#10003;</li>
        <li><a href='/duzce'>40 - Düzce Teknopark</a> &#10003;</li>
        <li><a href='/ege'>41 - Ege Teknopark</a></li>
        <li><a href='/gazi'>45 - Gazi Teknopark</a></li>
        <li><a href='/gaziantep'>46 - Gaziantep Teknopark</a></li>
        <li><a href='/nigde'>61 - Niğde Teknopark</a></li>
        <li><a href='/trabzon'>71 - Trabzon Teknokent</a></li>
        <li><a href='/yildiz'>76 - Yıldız Teknopark</a></li>
        <li><a href='/zonguldak'>78 - Zonguldak Teknopark</a></li>
        </ul>
    """
    return render_template_string(ret)

@app.route('/bilisim_vadisi')
@app.route('/4')
def bilisim_vadisi():
    tk = tns.BilisimVadisi()
    #ret = tk.run()
    ret = tk.test()
    return jsonify(ret)

@app.route('/kapadokya')
@app.route('/13')
def kapadokya():
    tk = tns.Kapadokya()
    ret = tk.run()
    #ret = bv.test()
    return jsonify(ret)

@app.route('/bogazici')
@app.route('/13')
def bogazici():
    tk = tns.Bogazici()
    ret = tk.run()
    #ret = bv.test()
    return jsonify(ret)

@app.route('/cumhuriyet')
@app.route('/35')
def cumhuriyet():
    tk = tns.Cumhuriyet()
    ret = tk.run()
    return jsonify(ret)

@app.route('/duzce')
@app.route('/40')
def duzce():
    tk = tns.Duzce()
    ret = tk.run()
    return jsonify(ret)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))