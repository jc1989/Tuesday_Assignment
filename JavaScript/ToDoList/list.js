let saveButton = document.getElementById("saveButton")
let taskTextBox = document.getElementById('taskTextBox')
let pendingTasksList = document.getElementById("pendingTasksList")
let completedTasksList = document.getElementById("completedTasksList")

function clearTaskBar(){
    taskTextBox.value = ""
}

//This is a function to handle save button click
saveButton.addEventListener('click', function() {
    console.log("button click fired...")

    //Appending the task list with the value saved in task text box
    // let task = taskTextBox.value

    let spanElement = document.createElement("span")
    spanElement.innerHTML = taskTextBox.value
    clearTaskBar()

    let liElement = document.createElement("li")
    liElement.className = "taskItem"

    let delButton = document.createElement("button")
    delButton.innerHTML = "Remove"
    delButton.className = "removeButton"


    let checkBox = document.createElement("input")//checkbox
    checkBox.setAttribute("type", "checkbox")
    //checkbox.type = "checkbox"

    //let taskTitle = document.createelement("h3") instead of creating a title in html and then using css 
   
    liElement.append(checkBox)
    liElement.append(spanElement)
    liElement.append(delButton)

    pendingTasksList.append(liElement)

    // () => arrow function that takes the place of writing function(). It is an anonymous function 
    checkBox.addEventListener('click', function() {
        if(this.checked){
            completedTasksList.append(liElement)
        }
        else{
            pendingTasksList.append(liElement)
        }
    })
    delButton.addEventListener('click', function() {
        if(completedTasksList.contains(liElement)){
            //can say this.parentElement.parentElement to accomplish the same thing
            completedTasksList.removeChild(liElement)
        }
        else if(pendingTasksList.contains(liElement)){
            pendingTasksList.removeChild(liElement)
            //instead of liElement I can use this.parentElement
        }
    })
})