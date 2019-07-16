// - Create a Palindrome app in Javascript which will print whether a string is a palindrome or not

let word = "hannah"
let reversedWord = ""

for(let index = word.length - 1; index >= 0;index-- ) {
  reversedWord += word[index]
}

if(reversedWord == word){
console.log("This is a palindrome")
}
else {
console.log("This is not a palindrome")
}


// - Create an app which removes duplicates from an array 

let names = ["Alex","Mary","John","Mary", "Alex", "Jerry"]

let duplicateFreeArray = [] 

function doesNameExists(name) {
    
  let alreadyExists = false 
  
  for(let index =0; index < duplicateFreeArray.length; index++) {
    if(name == duplicateFreeArray[index]) {
      alreadyExists = true 
      break
    }
  }
  
  return alreadyExists
  
}

for(let index = 0; index < names.length; index++) {
  
    let name = names[index]
    // if the name does not exists in duplicateFreeArray
    if(!doesNameExists(name)) {
       duplicateFreeArray.push(name)
    }
  
}

console.log(duplicateFreeArray)


//- Create an app whichs returns true/false depending on if the item is in the array 

function hasItem(item, names){
    inArray = false
    for(i = 0; i < names.length; i++){
        inArray = true
        break
    }
    return inArray
}

console.log(hasItem("Mary",names))
//- Create an app which finds the largest number in an array 

numbers = [23,4,6,8,3,9,23,534,6,7467,858567]

function largest(numbers){
    var max = numbers[0]
    for (i =1; i < numbers.length; i++){
        if(numbers[i] > max){
            max = numbers[i]
        }
    }
    return max
}
console.log(largest(numbers))

// - Create an app which finds the smallest number in an array 

function smallest(numbers){
    let min = numbers[0]
    for (i = 1; i < numbers.length; i++){
        if(numbers[i] < min){
            min = numbers[i]
        }
    }
    return min
}
console.log(smallest(numbers))

// - Create FizzBuzz app

fizzInput = prompt("Enter a number: ")

if(fizzInput % 3 == 0 && fizzInput % 5 == 0){
    console.log("FIZZBUZZ")
}
else if(fizzInput % 3 == 0){
    console.log("FIZZ")
}
else if(fizzInput % 5 == 0){
    console.log("BUZZ")
}

// - Create an app which determines whether the number is even or odd. 

userInput = prompt("Please enter a number: ")

if(userInput % 2 == 0){
    console.log("This is an even number")
}
else{
    console.log("This is an odd number")
}

// - Take the array [3,4,56,7,8,1] and sort them in ascending and descending order. 

orderArray = [3,4,56,7,8,1]

function sorting(orderArray){
    for(var i = 1; i < orderArray.length; i++){
        var pos = orderArray[i];
        for(var j = i -1; j >= 0 && (orderArray[j] < pos); j--){
            orderArray[j + 1] = orderArray[j];
        }
        orderArray[j + 1] = pos;
    }
    return orderArray;
}

console.log(sorting(orderArray))
// console.log(sorting(orderArray).reverse())

function reverseSorting(orderArray){
    for(var i = 1; i < orderArray.length; i++){
        var pos = orderArray[i];
        for(var j = i -1; j >= 0 && (orderArray[j] > pos); j--){
            orderArray[j + 1] = orderArray[j];
        }
        orderArray[j + 1] = pos;
    }
    return orderArray;
}
console.log(reverseSorting(orderArray))


/* -------------------------------------------------------
In this assignment you are going to test your knowledge of class composition. 
Your task is to create a class which represent a "Bank Account". 
The Bank Account will have the following properties. 

Bank Account: 

- First Name

- Last Name

- Middle Name

- Account Type 

- Balance 

- Status (Opened/Closed/Freeze) 

 

Here are the features that needs to be implement: 

- A user should be able to open a bank account provided they have the initial balance of $100

- User should be able to transfer money from one bank account to another  

- A user should be able to withdraw money from the bank account 

- The app should charge $-35 fees if the bank account is below $0

---------------------------------------------------------*/
class bankAccount{
    constructor(firstName, lastName, middleName = '') {
        this.firstName = firstName
        this.lastName = lastName
        this.middleName = middleName
        this.accountType = ""
        this.balance = 0
        this.status = "closed"
    }

    openAccount(initialBalance, accountType) { 
        if(initialBalance >= 100){
            this.accountType = accountType
            this.status = "open"
            this.balance = initialBalance
            console.log("Your account has been successfully created!")
        }
        else(console.log("Please add $100.00 to the account balance"))
    }

    transferMoney(){
        if (this.balance >= 0){
            let transfer = prompt("Would you like to transfer money to another account? Please type 'Yes' or 'No' ")
            if (transfer == 'Yes'){
                let amount = prompt("How much would you like to transfer?")
                this.balance -= amount
                console.log("Youre account balance is: " + this.balance)
            }
        }
    }

    withdraw(){
        let withdraw = prompt("Would you like to Withdraw funds? Please type 'Yes' or 'No' ")
        if (withdraw == 'Yes'){
            let amount = prompt("How much would you like to withdraw?")
            this.balance -= amount
            console.log("Youre account balance is: " + this.balance)
        }
}
    overdraft(){
        let fee = 35
        if (this.balance < 0){
            this.balance -= fee
            console.log("Youre account balance is: " + this.balance)
        }
    }
}


// let firstName = prompt("Please enter your first name: ")
// let firstName = prompt("Please enter your first name: ")


// bankAccount.lastName = prompt("Please enter your last name: ")
// bankAccount.middleName = prompt("Please enter your middle name: ")
// bankAccount.accountType = prompt("Please enter your account type: ")
// bankAccount.balance = prompt("Please enter your starting balance: ")


// sample = new bankAccount("eric", "snover")
// sample.openAccount(150,"checking")


joshAccount = new bankAccount("j","c","d")
joshAccount.openAccount(4000,"checking")
joshAccount.transferMoney()
joshAccount.withdraw()
joshAccount.overdraft()