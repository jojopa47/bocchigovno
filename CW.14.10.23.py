#Задание 1

function sayHello (name) {
  return 'Hello, ' +  name;
}

#Задание 2

const grow = x => {
  let res = 1;
  for (let i = 0; i < x.length; i++) {
    res *= x[i];
  }
  return res;
};

#Задание 3

function doubleInteger(i) {
  return i+i;
}

#Задание 4

function bmi(weight, height) {
  var result = weight/Math.pow(height,2) 
  
  if (result <= 18.5) {
    return "Underweight";
  } else if (result <= 25) {
    return "Normal";
  } else if (result <= 30) {
    return "Overweight";
  } else {
    return "Obese";
  }
  
}

#Задание 5

const quarterOf = (month) => {
  if (month <= 3) {
    return 1
  } else if (month <= 6) {
    return 2
  } else if (month <= 9) {
    return 3
  } else if (month <= 12) {
    return 4
  }
  
}

#Задание 6

function removeExclamationMarks(s) {
  return s.replace(/!/g, '');
}\

#Задание 7

var square = function(a){
  return a*a;
}

#Задание 8

function shortcut(s){
  return s.replace(/[aeiou]/g,"")
}

#Задание 9

function howMuchILoveYou(nbPetals) {
    switch ((nbPetals - 1) % 6) {
        case 1:
            return "a little";
        case 2:
            return "a lot";
        case 3:
            return "passionately";
        case 4:
            return "madly";
        case 5:
            return "not at all";
        default:
            return "I love you";
    }
}

#Задание 10

function testEven(n) {
  return n % 2 === 0 ? true : false;
}

