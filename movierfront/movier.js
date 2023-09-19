let MovieObject = {
    getMovie: function () {

        $.ajax({
            type: "GET",
            url: 'http://localhost:8000/all',
            //data: JSON.stringify(user),
            //contentType: "application/json; charset=utf-8"
        }).done(function (response) {

            // console.log(response)
            movielist = response.result
            alldivs = document.getElementById("alldiv")

            movielist.forEach(movie => {
                mdiv = document.createElement("div")
                mdiv.style = "width:100%"
                mdiv.className = "card"
                mdiv.class = "card"
                mtotal = document.createElement("div")
                mtotal.className = "card-total"
                mtotal.style = "text-align:center;"
                mimg = document.createElement("img")
                mimg.className = "card-img-top"
                mbody = document.createElement("div")
                mbody.className = "card-body"
                mtitle = document.createElement("h6")
                mtitle.className = "card-title"
                mtitle.innerText = movie.title
                mtitle.style = "text-align:left; font-weight: bold;"
                mgenre = document.createElement("p")
                mgenre.className = "card-text"
                mgenre.innerText = movie.genres
                mgenre.style = "text-align:left;"
                mbody.appendChild(mtitle)
                mbody.appendChild(mgenre)
                
                mimg.src = movie.poster_path
                mtotal.appendChild(mimg)
                mtotal.appendChild(mbody)
                mdiv.appendChild(mtotal)
                // mdiv.appendChild(mbody)
                alldivs.appendChild(mdiv)
                // console.log(movie.poster_path)
            });


        }).fail(function (error) {
            alert("movier.js에서 에러발생: " + error.statusText);
        });
    },

		getgenresMovie: function () {
			
			sgen =  document.getElementById("genres")
			selgenre = sgen.value
			urlmade = 'http://localhost:8000/genres/' + selgenre.toLowerCase()
			$.ajax({
				type: "GET",
				url: urlmade,
				contentType: "application/json; charset=utf-8"
			}).done(function (response) {

				// console.log(response)
				movielist = response.result
				console.log(movielist)
				gdivs = document.getElementById("gdiv")
				gdivs.innerHTML = '';
	
				movielist.forEach(movie => {
					mdiv = document.createElement("div")
					mdiv.style = "width:100%"
					mdiv.className = "card"
					mdiv.class = "card"
					mtotal = document.createElement("div")
					mtotal.className = "card-total"
					mtotal.style = "text-align:center;"
					mimg = document.createElement("img")
					mimg.className = "card-img-top"
					mbody = document.createElement("div")
					mbody.className = "card-body"
					mtitle = document.createElement("h6")
					mtitle.className = "card-title"
					mtitle.innerText = movie.title
					mtitle.style = "text-align:left; font-weight: bold;"
					mgenre = document.createElement("p")
					mgenre.className = "card-text"
					mgenre.innerText = movie.genres
					mgenre.style = "text-align:left;"
					mbody.appendChild(mtitle)
					mbody.appendChild(mgenre)
					
					mimg.src = movie.poster_path
					mtotal.appendChild(mimg)
					mtotal.appendChild(mbody)
					mdiv.appendChild(mtotal)
					gdivs.appendChild(mdiv)
					// console.log(movie.poster_path)
				});
	
	
			}).fail(function (error) {
				alert("movier.js에서 에러발생: " + error.statusText);
			});
		},
}

MovieObject.getMovie()
