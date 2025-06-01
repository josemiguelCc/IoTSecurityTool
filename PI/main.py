from flask import Flask, render_template, request
import nmap, json, subprocess

app = Flask(__name__)
scanner = nmap.PortScanner()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escaneo', methods=['POST'])
def escaneo():
    objetivo = request.form['target']
    try:
        resultado = scanner.scan(hosts=objetivo, arguments='-p- --open -sV --script vulners --min-rate 5000 -n -Pn')
    except Exception as e:
        return render_template('escaneo.html',
                               dispositivos=[],
                               objetivo=objetivo,
                               error=f"Error al ejecutar Nmap: {e}")

    scan_data = resultado.get('scan', {})
    dispositivos = []

    for ip, datos in scan_data.items():
        # Extraer puertos abiertos
        puertos = list(datos.get('tcp', {}).keys()) or []

        #CVE por puerto
        cve_puertos = {}
        for port, info in datos.get('tcp', {}).items():
            # Cada 'info' puede tener un script 'vulners' con líneas que contengan "CVE-XXXX"
            for ln in info.get('script', {}).get('vulners', '').splitlines():
                for token in ln.split():
                    if token.startswith("CVE-"):
                        cve_puertos.setdefault(port, []).append(token)

        # Exploit del cve de ese puerto
        port_vulns = {}
        for port, lista_cves in cve_puertos.items():
            port_vulns[port] = []
            for cve in set(lista_cves):
                try:
                    sp = subprocess.run(
                        ['searchsploit', '--cve', cve],
                        capture_output=True, text=True
                    ).stdout.strip().splitlines()
                    exploits = sp if sp else []
                except Exception:
                    exploits = []

                port_vulns[port].append({
                    'cve': cve,
                    'exploits': exploits
                })

        dispositivos.append({
            'ip': ip,
            'puertos': puertos if puertos else ["Ninguno"],
            'port_vulns': port_vulns,
            'raw_json': json.dumps(datos, indent=2)
        })

    return render_template('escaneo.html',
                           dispositivos=dispositivos,
                           objetivo=objetivo,
                           error=None)

if __name__ == '__main__':
    app.run(debug=True)
