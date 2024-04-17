//Dom manipulation, async coding, and es6 features
//Dom manipulation has 4 parts mainly
//selecting element,altering html content,altering css content, eventListeners
//elements can be selected by document.queryselector("element-name"),
//here element-name is either tag-name, #id , .class
//or we can use document.getElementbyId("id-name"), document.getElementbyClass("class-name")
//for changing html, variable storing the element, can by accessed by innerhtml() or textcontent()
var h1= document.querySelector('h1');
console.log(a);
h1.innerHTML="Now good";//writes html script within h1 tags
h1.textContent="byebye";// writes text content only
h1.style.color = 'yellow';
h1.addEventListener('click',function(){ //first argument is event that happens on h1 tag here click
h1.style.color = 'blue';
h1.style.backgroundColor= 'red';
});
window.addEventListener('load', function() {
    document.querySelector('h1').style.opacity = 1;});
var b= document.querySelectorAll('p'); //selects all elements with tag name p
console.log(b); //prints nodelist that is in {}, kind of similiar to arrays
b.forEach(function(e){e.style.color='red'}) //forEach used to iterate each single element and change its color
//now async coding- this coding means creating functions and put to side stack
//functions in side stack get executed when main stack functions are all done
//in side stack, functions when they are ready to be executed are put in main stack at end and executed
//there is no order in sidestacks, first work done first go to main stack policy, doesnt matter which order u came
//functions to put in side stack so they can keep processing while our main code keeps working as well are created by-
//------->fetch,axios,promises,setTimeout,setInterval are used
//now after function is processed, code waiting for its output starts running, that are done by-
//-------->then-catch,callbacks,async await
//promises are used as constructor using new keyword, takes function and that function takes res and rej as argument
//res is if function processing is done, rej is if function processing failed, res is resolve,rej is reject
//that function has two return value,i.e, res and rej, based on a conditonal statement
//now after function is processed whether failed or passed, that data, i.e, res and rev with/without any extra argument is passed to a variable
//that varibale is used with then and catch,to run the code that was waiting. then for res, catch for rej
var ans= new Promise(function(res,rej){ //ans stores result of operation in form of res and rej
    var x=Math.floor(Math.random()*10); //promise takes function that returns res and rev based on success & failure
    if(x<5) {return res();} //res and rev are both function that can take argument as well
    else {return rej();}    //if they want to return something along with pass/fail
} );
ans.then(function(){console.log("passed");}) //varible storing res, starts func inside then rej starts catch func, 
.catch(function(){ console.log("failed");}); //and here the argument in res/rej func is used in then/catch
//little realistic usecase of promise
function asyncTask() {
    return new Promise(function(resolve, reject) { //res/rej can be wrriten as resolve and reject
        setTimeout(function() {
        // Simulate an asynchronous operation
        var success = true; //we put it true always so resolve works
        if (success) {
            resolve('Operation completed successfully.'); //passing data from async operation to use in then
        } else { //as can see, dont need to use return keyword since not using res/rej
            reject(new Error('Operation failed.')); //passing error that can shown in catch
        }
        }, 2000);
    });
    }
    asyncTask() //asyncTask has return set for resolve/reject directly
    .then(function(result) { //now arguements of resolve goes into function argument that is result
        console.log('Success:', result);
    })
    .catch(function(error) { //while reject one goes in error variable
        console.error('Error:', error.message);
    });
//now if multiple async funcs, since there no order, then if we want to have order in which async functions to execute
//then we have to use promise chaining or can say promise nesting like this below
// First asynchronous function
function asyncTask1() {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
        resolve('First task completed');
        }, 1000);
    });
    }
    
    // Second asynchronous function
    function asyncTask2(data) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
        resolve(data + ', Second task completed');
        }, 1500);
    });
    }
    
    // Third asynchronous function
    function asyncTask3(data) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
        resolve(data + ', Third task completed');
        }, 500);
    });
    }
    // Chain promises
    //like switch, just each case works from top to bottom, elsewise catch works on error/fail
    asyncTask1()
    .then(function(result1) {
        console.log(result1);
        return asyncTask2(result1);
    })
    .then(function(result2) {
        console.log(result2);
        return asyncTask3(result2);
    })
    .then(function(result3) {
        console.log(result3);
    })
    .catch(function(error) {
        console.error('Error:', error);
    });
//Async Await - it's like promise but simpler
//await makes javascript wait until promise gets resolved before executing next line of code
//async is used on code(func) that is waiting, and await is used for code(func) that needs time to get output
//await is used inside async code, it makes the async func to wait for its output then run the rest func code
async function fetchData() { //making func async with async keyword
    try {
        let response = await fetch('https://jsonplaceholder.typicode.com/posts/1'); //applying await on code that take time
        let data = await response.json(); //again await since  json() returns a promise so we are using await here too
        console.log(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
    }
    fetchData();
//fetch is mainly used to fetch data from 3rd party APIs, so it takes time, hence async code, the data stored in varibale.needs to be used with .json() func to read data of fetch
//------>axios is library just like python request module, so learn it
//Es6 js veraion features
//let,const, arrow func, temperate literals, spread/rest, destructuring,class,modules,try-catch
//also functions can have default arguments
function fun(a=0,b=0) {console.log(a,b)} //b no parameter passed so default value 0 is taken
fun(a); 
//arrow func are created as ()=>{} and stored in variables
var a = ()=>{return "Hello"}
console.log(a());
var b = (x)=> x*2;
console.log(b(5));
var c= ()=>12;
console.log(c());
//temperate literals are used in string on numbers to perform small calculations
console.log( `The result is ${4+7}` );
//spread operator is used to take out elements, like in python
var arr=[1,2,3];
var brr=[4,5,6];
console.log([...arr, ...brr]);
//rest parameter is used to take remaining parameters into an array
function fun(a,b,...args){
    console.log(args);
}
fun(1,2,3,4,5);
//destructuring is putting values of array,object in variable but in kind of a reverse way to storing
var array=[1,2,34,5];
var [m,n]=array;
console.log(m,n);
var obj={name:"Ram",age:17};
var {age}=obj;
console.log(age);
//class-exactly like classes in python, just this is used instead of self, and constructor is used instead of __init__
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    greet() {
        return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
    }
    }
    
    // Create an instance of the Person class
    var john = new Person('John', 30);
    // Call the greet method
    console.log(john.greet()); // Output: Hello, my name is John and I am 30 years old.
//Promise - A+ spec compliant promises
var p= new Promise((res, rej)=>{
    setTimeout(() => {
        res("I am resolved");
        }, 2000);
});
p.then((val)=>{
    console.log(val);
}).catch((err)=>{
    console.log(err);
    })
//try is used to run code, if error comes, catch prints error stored in err variable and dont stop code execution
try{ console.log(a)}
catch(err) {
    console.log(err);
}