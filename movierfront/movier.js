let MovieObject = {
	getMovie: function() {
	
		$.ajax({
			type: "GET",
			url: 'http://localhost:8000/all',
			//data: JSON.stringify(user),
			//contentType: "application/json; charset=utf-8"
		}).done(function(response) {

            console.log(response)

		}).fail(function(error) {
			alert("!/js/user.js에서 에러발생: " + error.statusText);
		});
	},
 }

 MovieObject.getMovie()