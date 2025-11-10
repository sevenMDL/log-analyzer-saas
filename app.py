from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def detect_log_type(lines):
    """Detect the likely log type based on common patterns."""
    joined = "\n".join(lines[:20]).lower()  # only check first 20 lines

    if re.search(r'eth\d|vlan|ppp\d|br0|ifconfig', joined):
        return "router/network interface log"
    elif re.search(r'\b(get|post|put|delete)\b\s+\/', joined):
        return "web server access log"
    elif re.search(r'\b(error|exception|traceback)\b', joined):
        return "application/error log"
    elif re.search(r'\bkernel\b|\bsystemd\b|\bjournal\b', joined):
        return "system log"
    elif re.search(r'^\d{4}-\d{2}-\d{2}', joined, re.MULTILINE):
        return "timestamped log (generic)"
    else:
        return "unknown or custom format"

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    lines = file.read().decode(errors='ignore').splitlines()

    log_type = detect_log_type(lines)

    result = {
        "total_lines": len(lines),
        "detected_log_type": log_type,
        "sample_preview": lines[:5]
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
