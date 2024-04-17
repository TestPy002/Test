//js has hoisting means declarations are pushed to top of code just before execution
//object like dictinoary in python having key: value pairs, as well have functions as value called methods for keys like classes
const person = { //const is used so this entity cant make another object copying itself
  name: 'John',
  age: 30,
  city: 'New York'
};
//accessing values
console.log(person.name); // John
console.log(person.age); // 30
console.log(person.city); // New York
//altering values
person.name = 'Jane';
console.log(person.name); // Jane
person.country = 'USA'; //adding new property
console.log(person.country); // USA
//delete obj.key is used to delete and to accesss, obj.key and obj[key] in forin loop
delete person.age;
//in object, key names created with '_' as prefix, like _name is private variable, can be accessed with get and set functions
//Note: get and set, and getter and setter are same thing, getter,setter used in func, while get set used in obj
const person2 = {
  _name: '', //private variable
  get name() { //creates func to access private variable
    return this._name;
  },
  set name(value) {
    this._name = value;
  }
};
person2.name = 'Johnny'; //autocalls set
console.log(person2.name); // autocalls get, prints John
person2.name = 'Janu';
console.log(person2.name); // Jane
//variables are created by keyword var,let,const
//var- function scoped- not limited to braces,its "window object" ,old js version
//js can use browser context apis
//variables/data stored in heap, function stored in stack
//let,const- bracket scoped
//if-else,for,while,do-while,functions same as C
//functions has execution context, basically fox box which contains its variables, child functions and lexical environment
//pure funcs are those that returns same value for same input everytime while impure ones can have different return values for same input
//as well pure func dont change/alter global variables
//data stored in [](array),{}.() are refernces (can say like variables are pointer/address to data), so 
//b=[1,6,89,56];
//if we use a=b, then a doesnt take b values, it takes b refernce, so any change in a, will change b as well
//for making copy get passed, a= [...b], then a gets copied values of b
//array has 4 functions, push,pop,shift,unshift
//push,pop same as C, shift push new value at bottom of stack or can say start of array, while unshift removes from bottom/first
//any condition has true or false, things that mean false are 0,false,undefined,null,NaN,document.all , rest anything give true
//js has switch case
//forEach loop is used for interating array, performing operations but not changing the actual array values
function add(val) {console.log(val);}
var numbers = [1, 2, 3, 4, 5];
numbers.forEach(add); //using created func
//syntax of for each
//array.forEach(function(currentValue, index, array) {
  // code block to be executed on each element});
  var numbers = [1, 2, 3, 4, 5];
  numbers.forEach(function(number) { //using anonymous func
    console.log(number);
  });
//there is another way to short it by using => operator
var numbers = [1, 2, 3, 4, 5];
numbers.forEach(number => {
  console.log(number);
});
//forin loop is used for iterating object, same as forEach
var guy = {
  name: 'John',
  age: 30,
  gender: 'male'
};
for (var key in guy) { //iterates over all properties included inherited ones as well,
  console.log(key + ': ' + guy[key]); //obj[key] is used to access value
  if (person.hasOwnProperty(key)) { console.log(key + ': ' + person[key]);} //used to not iterate inherited properties
}
//there are callback functions that doesnt stop execution of code
//some functions takes time to execute, so the code doesnt frezee, it keeps running, when the func is executed/ready, callback func is called to transfer the control to that func
//callback in simple words, tells code that func is ready now, its part of asynchorus js coding
//setTimeout(func,time)
setTimeout(function(){console.log("2 seconds");},2000); //syntax of how call back a function after required time passes
//proper utilization of callback
function print(){console.log("Hello boy after 0 seconds");}
setTimeout(print,0);
//as can see above this hello still prints at end just before 2 seconds even time is 0 seconds, because its async coding, and that is executed at end of sync code 
//functions can be stored in variables, as well given as parameter/arguement to another func, just like python
function greet(){console.log("Hello")}
var a = greet;
a();
//js has anonymous func that are created and used together instantly, just like created in heat of moment
//high order func that takes argument as function or return function or both, basically used as closures
//constructor func are like as in python, they use 'this' keyword instead of self
//cons func are called with new keyword as prefix, new keyword creates func as objects to be stored in variables(objects)
//const func use this to create key-value pairs, like this.name="Ram", then new keyword used in calling, creating object having name:"Ram"
//const func are basically used to create lot of objects with similiar properties
function mydata(name)
{
  this.name=name;
  this.species="human";
  this.lifespan=100;
}
var boy=new mydata("Ramu"); //adding my own property rest same properties
//iife is immediately invoked function expression, basically a special function whose inside data is private, cant be accessed normslly
//iife is made by putting func within() then again parenthesis() since now its become a new func then data(like variables,func,obj) can only be accessed using return
//return should have getter func that access the private var, while there's setter func that can change private var
var val = (function(){ //function is iife func, storing its return in val
  var privateval = 12;
  return{
    getter: function(){console.log(privateval);},
    setter: function(val){privateval=val;}
  }
})();
//anonymous func are those which dont have name, like function(){}
//objects created all have a prtotyoe propery having prototype methods that can used, can check console
//there's one method which is used to inherit properties of one object
par={thing:"human", age:"adult"}
child={name:"Ram",age:13}
child.__proto__=par; //__proto__ makes child inherit property of par
//now if both have same key value like age here, value of age in child has more priority so its not changed by par
//this is basically self in python, just in python self points to object of a class but
// this points to window if its in global or func scope and points to object if in object scope
//one more difference, self is in parameter of func, while this is not, it can be directly written in func body
console.log(this);
function win()
{
  console.log(this);
} win();
obj={ age:15, object: function ()
  {
    console.log(this.age); //object scope of obj so can access its properties so prints 15
  }}
  obj.object()
//this can take value as object and can acess that object properties only when object is passed in function using call/apply/bind
//or when using event listners
function cal(){ console.log(this.age);}
cal.call(child) //passing object, stored in this
function cals(a,b,c)
{
  console.log(a,b,c,this.name)
}
cals.call(child,1,2,3) //we can pass arguements as well after passing object
cals.apply(child,[1,2,3]) //apply same as call just arguments are given in array, since apply only takes 2 arguments, object and argumengts
//using bind, we can create a new func that works same as call/apply, can be used anywhere anytime with new func name
var newfun = cals.bind(child,1,2,3) 
newfun(); //new function, call it anytime