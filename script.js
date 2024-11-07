/*
function CheckAge(){

        console.log('This is text is printed to the console.');
        let age = prompt("Enter your age:")
        if (age>=18)
        {
            alert("You are an adult!");
        }
        else
        {
            alert("You are not an adult!")
        }

        }



   // format of the JS array
const names = ['Frank', 'Scott', 'Jasmine', 'Don'];

   // console.log(names[3]);

for (let name of names) {
  console.log(`Name: ${name}`);
}

for (let name of names) {
  console.log(`${console.sort()}`);
}



const student = {
  firstName: 'Greg',
  lastName: 'Focker',
  studentId: '234359',
  phone: '040 5902123',
}
const greeting = `Hello, my name is ${student.firstName} ${student.lastName}`;
const studentInfo = `student number: ${student['studentId']}, phone number: ${student['phone']}`

console.log(greeting)
console.log(studentInfo)

const chosenProperty = "lastName";
console.log(student[chosenProperty]);

*/

/*
let student2 = {
      firstName: 'Ahmed',
      lastName: 'Hussein',
      credits :175,
      hasLeft: function() {return 240-this.credits}
    }

console.log("Student " + student2.firstName + " is missing " + student2.hasLeft() + " credits.");
*/

/*
let result
function quadraticSum(first, second) {
        const result = first * first + second * second;
        return result;
}

const num1 = prompt('Enter 1. number.');
const num2 = prompt('Enter 2. number.');
const quad = quadraticSum(num1, num2);
console.log('The quadratic sum of ' + luku1 + ' and ' + luku2 + ' is ' + ns);

 */

/*
function doLottery (numbers, num) {
  const row = [];
  let r;
  for (let i = 0; i < num; i ++) {
    let ok = false;

    while (!ok) {
      ok = true;
      r = Math.floor(Math.random() * numbers) + 1;
      for (let j = 0; j < i + 1; j ++) {
        if (row [j] === r) {
          ok = false;
        }
      }
    }
    row[i] = r;
  }
  return row;
}

const lottery = doLottery(40,7);
for (let i = 0; i < lottery.length; i++) {
    console.log(lottery[i]);
}

*/

function sum(a,b){
    return a+b;
}
function minus(a,b){
    return a-b;
}
function division(a,b){
    if (b===0){
        console.log('can not by 0')
    }
    return a/b;
}
function multiplication(a,b){
    return a*b;
}
console.log(`The sum is ${sum(2,3)}`)
console.log(`The minus is ${minus(2,3)}`)
console.log(`The division is ${division(2,3)}`)
console.log(`The multiplication is ${multiplication(2,3)}`)

