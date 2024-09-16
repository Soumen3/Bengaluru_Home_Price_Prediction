

function onPageLoad() {
	console.log("Document loaded");
	// var url = "http://127.0.0.1:5000/get_location_names";
	var url = '/get_location_names';
	$.get(url, function(data, status) {
		console.log("Got response for get_location_names request");
		
		if(data) {
			var locations = data.locations;
			var uiLocations = document.getElementById("uiLocations");
			$('#id_uiLocations').empty();
			for(var i in locations) {
				var opt = new Option(locations[i]);
				$('#id_uiLocations').append(opt);
			}
		}
	});



	// Submit the form 
	document.getElementById("uiForm").onsubmit = function(e) {
		e.preventDefault();
		console.log("Form submitted");

		var location = document.getElementById("id_uiLocations").value;
		console.log("Location: ", location);

		var bedrooms = getSelectedRadioValue("uiBHK");
		var bathrooms = getSelectedRadioValue("uiBathrooms");
		var sqft_living = document.getElementById("id_Squareft").value;

		console.log("Bedrooms: ", bedrooms);
		console.log("Bathrooms: ", bathrooms);
		console.log("Sqft: ", sqft_living);

		var url = "/";
		$.ajax({
			type: "POST",
			url: url,
			data: {
				location: location,
				bedrooms: bedrooms,
				bathrooms: bathrooms,
				sqft_living: sqft_living
			},
			headers: {
				'X-CSRFToken': csrftoken
			},
			success: function(data, status) {
				console.log("Got response for home request");
				console.log(data);
				document.getElementById("uiEstimatedPrice").innerHTML = "<p class='fs-4'>" + data.price.toString() + " Lakh</p>";
				console.log(status);
			}

		});

		
	}
	
}

window.onload = onPageLoad;


function getSelectedRadioValue(name) {
    var radios = document.getElementsByName(name);
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            return radios[i].value;
        }
    }
    return null; // No radio button is selected
}

// Function to get the CSRF token from the cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');