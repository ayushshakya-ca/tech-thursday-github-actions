from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "v1")

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TravelX - Explore The World</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>
* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}}

body {{
    background:#f4f7fa;
    scroll-behavior:smooth;
}}

header {{
    position:fixed;
    width:100%;
    top:0;
    left:0;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:15px 70px;
    background:linear-gradient(135deg,#0d6efd,#6610f2);
    color:white;
    z-index:1000;
}}

.hero {{
    height:100vh;
    background:url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e') no-repeat center/cover;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    color:white;
    position:relative;
}}

@keyframes waterFlow {{
    from {{ transform: rotate(0deg); }}
    to   {{ transform: rotate(360deg); }}
}}

.version-badge {{
    position:fixed;
    bottom:20px;
    right:20px;
    background:#0d6efd;
    color:white;
    padding:10px 15px;
    border-radius:10px;
    font-weight:bold;
    box-shadow:0 5px 15px rgba(0,0,0,0.3);
}}
</style>
</head>

<body>

<header>
<div style="font-size:22px;font-weight:700;">✈️ TravelX</div>
</header>

<section class="hero">
<h1>Experience The Beauty of The Ocean 🌊</h1>
</section>

<div class="version-badge">
Running Version: {version}
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
