var c=document.querySelector(".h0")
var p=document.querySelector(".h1")
var p2=document.querySelector(".h2")
var p3=document.querySelector(".h3")
var p4=document.querySelector(".h4")
var p5=document.querySelector(".h5")
c.style.backgroundColor="black";
[c,p,p2,p3,p4,p5].forEach(function(cur,index){
    cur.style.transform=`scale(${1-index/10})`;
    cur.style.opacity= 0.9- index/10;
})
document.addEventListener("mousemove", function(dets) {
    var delay = 100; // Set the delay in milliseconds
    [c, p, p2, p3, p4, p5].forEach(function(cursor, index) {
    setTimeout(function() {
        cursor.style.top = dets.y + "px";
        cursor.style.left = dets.x + "px";
        }, index * delay);
    });
});
var cpic=document.querySelector(".cen")
var pic1=document.querySelector(".grid1");
var pic2=document.querySelector(".grid2");
var pic3=document.querySelector(".grid4");
var pic4=document.querySelector(".grid3");
var ar1=document.querySelector(".gif1");
var ar2=document.querySelector(".gif2");
var ar3=document.querySelector(".gif3");
var ar4=document.querySelector(".gif4");
cpic.style.opacity=1;
cpic.addEventListener('mouseenter',function()
{
    if(cpic.style.opacity==1)
    {
    pic1.style.opacity=1;
    console.log("Hi");}
});
pic1.addEventListener('mouseenter',function()
{
    if(pic1.style.opacity==1)
    {
    ar1.style.width='100%';
    ar1.style.opacity=1;
    pic2.style.opacity=1;
    cpic.style.opacity=0;}
});
pic1.addEventListener('mouseleave',function()
{
    ar1.style.opacity=0;
    ar1.style.width='10%';
});
pic2.addEventListener('mouseenter',function()
{
    if(pic2.style.opacity==1)
    {
    pic1.style.opacity=0;
    pic3.style.opacity=1;
    ar2.style.height='100%';
    ar2.style.opacity=1;}
});
pic2.addEventListener('mouseleave',function()
{
    ar2.style.opacity=0;
    ar2.style.height='10%';
});
pic3.addEventListener('mouseenter',function()
{
    if(pic3.style.opacity==1)
    {
    pic2.style.opacity=0;
    pic4.style.opacity=1;
    ar3.style.width='100%';
    ar3.style.opacity=1;
    }
});
pic3.addEventListener('mouseleave',function()
{
    ar3.style.opacity=0;
    ar3.style.width='10%';
});
pic4.addEventListener('mouseenter',function()
{
    if(pic4.style.opacity==1){
    pic3.style.opacity=0;
    cpic.style.opacity=1;
    ar4.style.height='100%';
    ar4.style.opacity=0;}
});
pic4.addEventListener('mouseleave',function()
{
    pic4.style.opacity=0;
    ar4.style.opacity=0;
    ar4.style.height='10%';
});
var btig=document.querySelector('.villian');
var btn1=document.querySelector('.btn1');
var btn2=document.querySelector('.btn2');
var btn3=document.querySelector('.btn3');
var btn4=document.querySelector('.btn4');
var btn5=document.querySelector('.btn5');
var url =["url(https://mfiles.alphacoders.com/100/thumb-350-1009778.webp)"
,"url(https://i.pinimg.com/564x/e7/5f/ec/e75fec35b549527c11191f3c19e67ec0.jpg)","url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFEtGevaVswGmJw8Cp9LPTnAMAB0BMVc1ryP_5OEWwzA&s)"
,"url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU-0rMxqZpSbUqT7izlwAJSAcrHDpPfvPhG-98VM75Pg&s)","url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW59tgjx63x6KxmnEhzFz7pQ35DSl3wWgWsxAGJyLdAw&s)"];

btn1.addEventListener('click',function(){
    btig.style.backgroundImage=url[0];
});
btn2.addEventListener('click',function(){
    btig.style.backgroundImage=url[1];
});
btn3.addEventListener('click',function(){
    console.log('hi');
    btig.style.backgroundImage=url[2];
});
btn4.addEventListener('click',function(){
    btig.style.backgroundImage=url[3];
});
btn5.addEventListener('click',function(){
    btig.style.backgroundImage=url[4];
});
var c=document.querySelector(".h0")
var reveal=document.querySelectorAll('.reveal h1');
reveal.forEach(function(reveal){
reveal.addEventListener("mouseover", function(dets) {
        c.style.backgroundColor='transparent';
        c.style.backgroundImage="url(https://png.pngtree.com/png-clipart/20221117/ourmid/pngtree-goldfish-clipart-cartoon-vector-image-png-image_6461602.png\)";
        c.style.backgroundSize='cover';
        c.style.transform='scale(7)';
        c.style.opacity=1;
        c.style.top = dets.y + "px";
        c.style.left = dets.x + "px";
        reveal.style.webkitTextStroke='1px black';
        [p,p2,p3,p4,p5].forEach(function(cur){
            cur.style.opacity= 0;
        })
        setTimeout(function(){reveal.style.webkitTextStroke='1px transparent'},2000);
});})
var reveal1=document.querySelector('.reveal');
reveal1.addEventListener("mouseleave", function(dets) {
    var delay = 100; // Set the delay in milliseconds
    c.style.transform='scale(1)';
    c.style.backgroundColor="black";
    c.style.backgroundImage='none';
    [c, p, p2, p3, p4, p5].forEach(function(cursor, index) {
    setTimeout(function() {
        cursor.style.top = dets.y + "px";
        cursor.style.left = dets.x + "px";
        }, index * delay);
        cursor.style.opacity= 0.7- index/10;
    });
});
var img=["url(https://images.pexels.com/photos/164041/pexels-photo-164041.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)",
"url(https://images.pexels.com/photos/1051838/pexels-photo-1051838.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)","url(https://i.pinimg.com/564x/15/f3/da/15f3da57daeea2a55b66f8f4ae7cdc01.jpg)",
"url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJWLWgSjaI3elDHCnApS9WVgHXweOopY_wSRyLMOdPZw&s)"];
var click=0;
const chngimg = document.querySelector('.best');
var im = document.querySelector('.img');
        chngimg.addEventListener("mousemove", function(dets) {
            console.log(dets.x,dets.y);
            console.log(im.src);
            im.style.display='block';
            c.style.opacity=0;
            im.style.top= dets.y-70+"px";
            im.style.left= dets.x-70+"px";
            im.style.borderRadius='50%';
            im.style.backgroundSize='500px 300px'
            im.style.backgroundPositionX = `${-dets.x+140+"px"}`;
            im.style.backgroundPositionY= `${-dets.y -73.5+"px"}`;
        });
    chngimg.addEventListener('click', () => {
            chngimg.style.backgroundImage=img[click%4];
            chngimg.style.visibility='visible';
            click++;
            setTimeout(function(){
                im.style.backgroundImage=img[click%4];},3000);
});
chngimg.addEventListener('mouseleave', function(){
    im.style.display='none';
    console.log('hi');
});
var cont='<p style=" background-color: aqua;"></p>';
var out = document.querySelector('.out');
var inp = document.querySelector('.num');
var data="";
inp.addEventListener('input',function(){
    while(out.firstChild)
    {
        out.removeChild(out.firstChild);
    }
    var n= this.value;
    var i=0;
    for(i=0;i<n;i++)
    {
        data = data +cont;
    }
    out.innerHTML=data;
    data="";
})
var l1 = document.querySelector('.demon');
l1.addEventListener('click',function()
{
    window.location.href = 'index2.html';
})
