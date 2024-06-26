document.addEventListener("DOMContentLoaded",function()
{
    setTimeout(function(){
    gsap.to(document.querySelector('.load'),{
        duration:0.5,
        opacity:0
    })},1000);
})
var home = document.querySelector(".home");
var menu = document.querySelector(".menu");
var stge = document.querySelector(".menu video")
var m1= document.querySelector(".m1");
var tl = gsap.timeline();
var c=0,d=0;
var f;
tl.from(stge, {
    y: '-100%',
    duration: 4,
    ease: "power2.out",
}).to(stge, { duration: 8, ease: "none", onStart: function() {
    stge.play();
    }}).to(m1, {
    delay: function(){if(f==1){return 8}},
    opacity: 1,
    duration: 3,
    ease: "power2.out"
},).pause();
home.addEventListener('click',function()
{
    console.log("hi");
    tl.play();
})
menu.addEventListener('mouseleave',function()
{
    stge.id="1";
    tl.reverse();
    var currentTime = stge.currentTime;
    var duration = stge.duration;
    var reverseTime = currentTime;
    stge.pause();
    intervalId = setInterval(function() {
    reverseTime -= 0.05; // Adjust speed by changing decrement value
    if (reverseTime < 0) {
        clearInterval(intervalId);
        stge.pause();
        stge.currentTime = 0;
    } else {
        stge.currentTime = reverseTime;
    }
    }, 50);
})
var web = document.querySelector(".guider");

var mouseTimer;
document.addEventListener('mousemove',function(e)
{
    var x=e.pageX;
    var y=e.pageY;
    var wx = web.getBoundingClientRect().x;
    var wy = web.getBoundingClientRect().y;
    var distance= Math.sqrt((wx-x)*(wx-x)+(wy-y)*(wy-y));
    var duration=distance/60;
    gsap.to(web,{
        duration: duration,
        y: y,
        x: x,
        ease: 'none',
        backgroundImage: "url(spidy.gif)"
    })
    clearTimeout(mouseTimer);
    mouseTimer = setTimeout(function() {
    console.log("Mouse still event detected");
    setTimeout(function(){
        console.log("An stop");
        web.style.backgroundImage="url(spidystill.png)";
    },duration*1000-500)
    }, 1000);
})
var swiper = new Swiper(".mySwiper", {
    direction: 'horizontal',
    loop:true,
    slidesPerView: 'auto',
    spaceBetween: 10,
    autoplay: {
        delay: 2500,
        disableOnInteraction: true,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    });
gsap.registerPlugin(ScrollTrigger);
var box=document.querySelector('.scroll');
var text=document.querySelectorAll('.text');
var img = document.querySelector('.img');
var tl2= gsap.timeline();

ScrollTrigger.create(
    {
        trigger: ".scroll",
        start:  "top bottom",
        end: "bottom top",
        markers: true,
        onEnter: function()
    {
        tl2.to(text,{
        duration:8,
        y:-130,
        opacity: 1,
        stagger:0.5,
        scrollTrigger:{
        trigger:text,
        start: "top bottom",
        end: 'bottom top',
        scrub: true,
        markers: true
            }
        })
    }
    }
);
gsap.to(".img img", {
    scrollTrigger: {
        trigger: '.scroll',
        start: "top bottom",
        end: "bottom top",
        scrub: true,
        markers:true,
    },
    y:'-140vh',
    ease: "power1.inOut"
    });
var text2 = document.querySelector('.text2');
var chars = text2.textContent.split('');
ScrollTrigger.create({
    trigger: '.text2',
    start: 'top bottom',
    end: 'bottom top',
    markers: true,
    toggleActions: 'play none none reverse',
    onEnter: ()=>{
        text2.textContent="";
chars.forEach((char, index) => {
    const span = document.createElement('span');
    span.textContent = char;
    span.style.opacity = 0;
    span.style.position='relative';
    span.style.display='inline-block';
    text2.appendChild(span);
    gsap.fromTo(span, 
    { opacity: 0, y: '-30',x: 50}, 
    { opacity: 1, y: 50, x:0,
        delay: index * 0.1, // Adjust delay for staggered animation
        duration: 0.5,
        ease: 'power2.out',
    }
    );
})}
})
var story=document.querySelector(`.story`);
var storytext = document.querySelector(`.story-text`);
var btnNext = document.querySelector(`.btn-next`);

    function createparticle(numSnowflakes) {
    for (let i = 0; i < numSnowflakes; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        story.appendChild(particle);
        gsap.set(particle, {
        left: Math.random() * window.innerWidth - 10,
        top: -1,
        scale: Math.random(),
        opacity: Math.random(),
        });
    animateSnowflake(particle);
    }
}

function animateSnowflake(particle) {
    const duration = Math.random() * 10 + 5;
    gsap.to(particle, {
        top: `93vh`,
        x: '-=200',
        rotate: '+=180',
        duration: duration,
        ease: 'power1.inOut',
        repeat: -1,
        delay: -Math.random() * duration,
        onComplete: function() {
        gsap.set(particle, {
            x: Math.random() * window.innerWidth -10,
            y: -1,
            opacity: Math.random(),
        });
    }
});
}
//var url[]={"","","",""}
var url =["url('https://static.vecteezy.com/system/resources/thumbnails/001/194/635/small_2x/snowflake.png')"
,"url('petal2.png')","url(https://w7.pngwing.com/pngs/845/229/png-transparent-drop-water-rain-drops-angle-cosmetics-drop-thumbnail.png)"
,"url(https://clipart-library.com/images/rTjGj5rkc.png)"];
var bimg = ["url(https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsX29mZmljZV81X3Nub3dfZm9yZXN0X3NreV9iYWNrZ3JvdW5kX3Nub3dfaXNfZmFsbGluZ19jbF85ZmYwMWRjZS1hZjY0LTQxYzEtOTg0Yi0zYTM5ODM0NmNjMDRfMS5qcGc.jpg)",
"url(https://preview.redd.it/cherry-blossoms-wallpaper-v0-whi25yjrdzqb1.png?width=1080&crop=smart&auto=webp&s=1e7ec3a03d3abf91a7a40fc27ae71ed1251e47d0)",
"url(https://w0.peakpx.com/wallpaper/216/818/HD-wallpaper-summer-thunderstorm-awesome-clouds-dark-grass-new-rain-storms-weather.jpg)",
"url(https://getwallpapers.com/wallpaper/full/f/6/4/1228318-download-autumn-backgrounds-1920x1200-for-iphone-5s.jpg)"];
var seasons=["winter","spring","monsoon","autumn"];
var click = -2;
btnNext.addEventListener('click',function(){
    click++;
    if(click==-1){
        createparticle(100);
        story.style.backgroundColor = 'transparent';
        btnNext.textContent="NEXT";
        click++;
    }
    var particle=document.querySelectorAll('.particle');
    gsap.set(particle,{
        backgroundImage: url[click%4],
    });
    story.style.backgroundImage= bimg[click%4];
    storytext.textContent=seasons[click%4];
})
function scrolltotop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}