let dishesListing = document.getElementById("dishesListing")
let newDishes = dishes


let allDishes = newDishes.map(dish => {

    return `<div class = "innerMenuItems">
        <img id = "menuImage" src='${dish.imageURL}'/>
        <span id = "menuDescriptions">${dish.title + ":"}</span>
        <span id = "menuDescriptions">${"$" + dish.price}</span>
        <p>${dish.description}</p>
        </div>`

})

    dishesListing.innerHTML = allDishes.join('')

console.log(dishSelector)
dishSelector.addEventListener('change', () => {
    console.log(dishSelector.value)
    if(dishSelector.value == "Starters"){
        newDishes = dishes.filter(dish => dish.course == "Starters")}
    else if(dishSelector.value == "Entrees"){
        newDishes = dishes.filter(dish => dish.course == "Entrees")}
    else if(dishSelector.value == "Desserts"){
        newDishes = dishes.filter(dish => dish.course == "Desserts")}
    else if(dishSelector.value == "dishes"){
        newDishes = dishes
    }

    let ListingDiv = newDishes.map(dish => {

        let listDiv = `<div class = "innerMenuItems">
        <img id = "menuImage" src='${dish.imageURL}'/>
        <span id = "menuDescriptions">${dish.title + ":"}</span>
        <span id = "menuDescriptions">${"$" + dish.price}</span>
        <p>${dish.description}</p>
        </div>`
        return listDiv
    })

    dishesListing.innerHTML = ListingDiv.join('')

})