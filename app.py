from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CI/CD Demo</title>
<style>
body{font-family:'Inter',sans-serif;background:#1e1e2f;color:#f0f0f0;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}
.card{background:rgba(255,255,255,0.1);backdrop-filter:blur(8px);border-radius:12px;padding:2rem;max-width:400px;text-align:center;box-shadow:0 8px 32px rgba(0,0,0,0.2);}
button{background:#4e9af1;border:none;color:#fff;padding:0.75rem 1.5rem;border-radius:8px;cursor:pointer;transition:background .3s;}
button:hover{background:#3a7dc9;}
#msg{margin-top:1rem;font-weight:bold;}
</style>
</head>
<body>
<div class="card">
<h1>CI/CD Pipeline Demo</h1>
<p>Halo! Pipeline CI/CD Self-Hosted berhasil jalan!</p>
<button id="fetchBtn">Get Greeting</button>
<div id="msg"></div>
</div>
<script>
document.getElementById('fetchBtn').addEventListener('click', async () => {
  const resp = await fetch('/api/message');
  const data = await resp.json();
  document.getElementById('msg').textContent = data.message;
});
</script>
</body>
</html>"""
    return render_template_string(html)

@app.route('/api/message')
def api_message():
    # Simple JSON endpoint returning a greeting message
    return {"message": "Halo! Pipeline CI/CD Self-Hosted berhasil jalan!"}

if __name__ == '__main__':
    # In production, disable debug and use a proper WSGI server.
    app.run(host='0.0.0.0', port=5000)  # nosec B104
