from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TravelX - Explore The World</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}
body{
    background:#f4f7fa;
    scroll-behavior:smooth;
}

/* ================= NAVBAR ================= */
header{
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
    transition:0.3s;
}
header.scrolled{
    box-shadow:0 8px 20px rgba(0,0,0,0.2);
}
.logo{
    display:flex;
    align-items:center;
    gap:10px;
    font-size:22px;
    font-weight:700;
}
nav ul{
    list-style:none;
    display:flex;
    gap:30px;
}
nav ul li a{
    text-decoration:none;
    color:white;
    font-weight:500;
}
nav ul li a:hover{
    opacity:0.7;
}
.menu-toggle{
    display:none;
    font-size:26px;
    cursor:pointer;
}

/* ================= HERO ================= */
.hero{
    height:100vh;
    background:url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e') no-repeat center/cover;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    color:white;
    position:relative;
    overflow:hidden;
}
.hero::after{
    content:"";
    position:absolute;
    width:200%;
    height:200%;
    background:rgba(255,255,255,0.05);
    top:0;
    left:-50%;
    animation:waterFlow 25s linear infinite;
}
.hero h1{
    font-size:55px;
    z-index:2;
}

/* ================= SECTIONS ================= */
section{
    padding:120px 80px;
}

.section-title{
    text-align:center;
    margin-bottom:60px;
    font-size:38px;
    font-weight:700;
    background:linear-gradient(45deg,#0d6efd,#6610f2);
    -webkit-background-clip:text;
    color:transparent;
}

/* ================= TOP EXPERIENCES ================= */
.carousel{
    position:relative;
    overflow:hidden;
    border-radius:20px;
}
.carousel-container{
    display:flex;
    transition:0.8s ease;
}
.slide{
    min-width:100%;
    position:relative;
}
.slide img{
    width:100%;
    height:500px;
    object-fit:cover;
}
.slide-text{
    position:absolute;
    bottom:40px;
    left:40px;
    font-size:32px;
    color:white;
    background:rgba(0,0,0,0.5);
    padding:15px 30px;
    border-radius:10px;
}
.carousel-buttons{
    position:absolute;
    top:50%;
    width:100%;
    display:flex;
    justify-content:space-between;
    transform:translateY(-50%);
    padding:0 20px;
}
.carousel-buttons button{
    background:rgba(255,255,255,0.4);
    border:none;
    padding:10px 20px;
    border-radius:50%;
    cursor:pointer;
}

/* ================= DESTINATIONS ================= */
.destinations{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:30px;
}
.card{
    background:white;
    border-radius:15px;
    overflow:hidden;
    box-shadow:0 10px 25px rgba(0,0,0,0.1);
    transition:0.4s;
}
.card:hover{
    transform:translateY(-10px);
}
.card img{
    width:100%;
    height:250px;
    object-fit:cover;
}
.card-content{
    padding:20px;
}

/* ================= TESTIMONIALS ================= */
.testimonials{
    background:linear-gradient(135deg,#0d6efd,#6610f2);
    color:white;
}
.testimonials h2{
    color:white;
    background:none;
}
.testimonial-container{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:30px;
}
.testimonial-card{
    background:rgba(255,255,255,0.15);
    backdrop-filter:blur(15px);
    padding:30px;
    border-radius:20px;
}

/* ================= PACKAGES ================= */
.packages{
    text-align:center;
}
.package-container{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:30px;
}
.package-card{
    background:white;
    padding:40px 20px;
    border-radius:20px;
    box-shadow:0 10px 25px rgba(0,0,0,0.1);
    transition:0.4s;
}
.package-card:hover{
    transform:translateY(-10px);
}
.package-card h2{
    font-size:28px;
    color:#0d6efd;
    margin-bottom:15px;
}

/* ================= FOOTER ================= */
footer{
    background:#111;
    color:white;
    text-align:center;
    padding:20px;
}

/* ================= RESPONSIVE ================= */
@media(max-width:768px){
    nav ul{
        position:absolute;
        top:70px;
        right:0;
        background:#0d6efd;
        flex-direction:column;
        width:200px;
        display:none;
        padding:20px;
    }
    nav ul.active{
        display:flex;
    }
    .menu-toggle{
        display:block;
    }
}
</style>
</head>

<body>

<header>
<div class="logo">✈️ TravelX</div>

<nav>
<ul id="menu">
<li><a href="#home">Home</a></li>
<li><a href="#experiences">Experiences</a></li>
<li><a href="#destinations">Destinations</a></li>
<li><a href="#pricing">Packages</a></li>
<li><a href="#contact">Contact</a></li>
</ul>
<div class="menu-toggle" onclick="toggleMenu()">☰</div>
</nav>
</header>

<!-- HERO -->
<section class="hero" id="home">
<h1>Experience The Beauty of The Ocean 🌊</h1>
</section>

<!-- TOP EXPERIENCES -->
<section id="experiences">
<h2 class="section-title">Top Experiences</h2>
<div class="carousel">
<div class="carousel-container" id="carousel">

<div class="slide">
<img src="https://images.unsplash.com/photo-1593069567131-53a0614dde1d?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
<div class="slide-text">Forest & Nature Retreats</div>
</div>

<div class="slide">
<img src="https://images.unsplash.com/photo-1501785888041-af3ef285b470">
<div class="slide-text">Mountain Adventures</div>
</div>

<div class="slide">
<img src="https://images.unsplash.com/photo-1526772662000-3f88f10405ff">
<div class="slide-text">City Skylines</div>
</div>

</div>

<div class="carousel-buttons">
<button onclick="prevSlide()">❮</button>
<button onclick="nextSlide()">❯</button>
</div>
</div>
</section>

<!-- DESTINATIONS -->
<section id="destinations">
<h2 class="section-title">Popular Destinations</h2>
<div class="destinations">
<div class="card">
<img src="https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?q=80&w=1074&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
<div class="card-content"><h3>Goa</h3></div>
</div>
<div class="card">
<img src="https://images.unsplash.com/photo-1502602898657-3e91760cbb34">
<div class="card-content"><h3>Paris</h3></div>
</div>
<div class="card">
<img src="https://images.unsplash.com/photo-1512453979798-5ea266f8880c">
<div class="card-content"><h3>Dubai</h3></div>
</div>
</div>
</section>

<!-- TESTIMONIALS -->
<section class="testimonials">
<h2>What Our Travelers Say</h2>
<div class="testimonial-container">
<div class="testimonial-card">
<p>"Goa trip was absolutely stunning. TravelX handled everything perfectly!"</p>
<h4>- Priya Sharma</h4>
</div>
<div class="testimonial-card">
<p>"Luxury Dubai experience with zero hassle. Highly recommended."</p>
<h4>- Arjun Mehta</h4>
</div>
<div class="testimonial-card">
<p>"Best booking experience ever. Professional and smooth."</p>
<h4>- Sneha Reddy</h4>
</div>
</div>
</section>

<!-- TRAVEL PACKAGES -->
<section class="packages" id="pricing">
<h2 class="section-title">Travel Packages</h2>

<div class="package-container">

<div class="package-card">
<h2>₹19,999</h2>
<h3>Basic Package</h3>
<p>3 Days • Hotel • Breakfast Included</p>
</div>

<div class="package-card">
<h2>₹39,999</h2>
<h3>Standard Package</h3>
<p>5 Days • 4★ Hotel • Meals Included</p>
</div>

<div class="package-card">
<h2>₹69,999</h2>
<h3>Premium Package</h3>
<p>7 Days • 5★ Resort • All Activities</p>
</div>

<div class="package-card">
<h2>₹1,29,999</h2>
<h3>Luxury Elite</h3>
<p>10 Days • Private Villa • Personal Guide</p>
</div>

</div>
</section>

<footer id="contact">
© 2026 TravelX | Designed with @cloudambassadorsteam
</footer>

<script>
function toggleMenu(){
document.getElementById("menu").classList.toggle("active");
}

window.addEventListener("scroll", function(){
document.querySelector("header").classList.toggle("scrolled", window.scrollY > 50);
});

let currentIndex=0;
const carousel=document.getElementById("carousel");
const slides=document.querySelectorAll(".slide");

function showSlide(index){
if(index<0) currentIndex=slides.length-1;
else if(index>=slides.length) currentIndex=0;
else currentIndex=index;

carousel.style.transform=`translateX(-${currentIndex*100}%)`;
}
function nextSlide(){ showSlide(currentIndex+1); }
function prevSlide(){ showSlide(currentIndex-1); }
setInterval(()=>{ nextSlide(); },5000);
</script>

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
