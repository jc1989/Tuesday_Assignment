/* Your task is to display news to the user.
The news.zip file (attached) already has a JSON formatted object which contains the news.
Create a page which displays the following information related to the news. */ 

let newsDisplay = document.getElementById("newsDisplay")
let newsArray = Object.values(news)[2]

function newsArticles() {
// .map function
    let newsDiv = newsArray.map(article => {

        // if article.author == 'null
        let newsDiv = `<div class="newsItem">
                            <span>Author: ${article.author ? article.author : "No author provided"}</span>
                            <span>Title: ${article.title ? article.title : "No title provided"}</span>
                            <span>Description: ${article.description ? article.description : "No description provided"}</span>
                            <span>URL: ${article.url ? article.url : "No URL provided"}</span>
                            <img src='${article.urlToImage ? article.urlToImage : "https://upload.wikimedia.org/wikipedia/commons/f/fc/No_picture_available.png"}'></img>
                            <span>Publisher: ${article.publishedAt ? article.publishedAt : "No publisher provided"}</span>
                        </div>`
        // return
        return newsDiv
    })

    newsDisplay.innerHTML = newsDiv.join('')

}

newsArticles()