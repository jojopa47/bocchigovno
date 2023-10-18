#Задание 1

function saleHotdogs(n){
  var money = 0;
  if (n < 5 ) {
    money = n * 100
  }
  else if ( n >= 5 && n < 10 ) {
    money = n * 95
  }
  else if ( n >= 10 )  {
   money = n * 90 
  }
  return money
}

#Задание 2

function sumStr(a,b) {
  return (+a+ +b)+''  
}

#Задание 3

function otherAngle(a, b) {
  return 180-(a+b);
}

#Задание 4

function hexToDec(hexString){
 return  parseInt(hexString, 16);
}

#Задание 5

function getChar(c) {
  return String.fromCharCode(c)
}

#Задание 6

function strCount(str, letter){  
  return str.split(letter).length-1
}

#Задание 7

function problem(x){
  return typeof x === "number" ? x * 50 + 6 : "Error";
}

#Задание 8

function mouthSize(animal) {
  return animal.toLowerCase() == 'alligator' ? 'small' : 'wide';
}

#Задание 9

function simpleMultiplication(n){
  return n % 2 == 0 ? n * 8 : n * 9
}


#Задание 10

const getRealFloor = n => {
  if(n >= 13) return n - 2
  if(n > 0) return n - 1
  return n
}
