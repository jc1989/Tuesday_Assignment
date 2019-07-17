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

    let checkBox = document.createElement("input")
    checkBox.setAttribute("type", "checkbox")

   
    liElement.append(checkBox)
    liElement.append(spanElement)
    liElement.append(delButton)

    pendingTasksList.append(liElement)

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
            completedTasksList.removeChild(liElement)
        }
        else if(pendingTasksList.contains(liElement)){
            pendingTasksList.removeChild(liElement)
        }
    })
})