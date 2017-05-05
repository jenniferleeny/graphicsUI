/*
newImg.addEventListener("click", function(e) {
	console.log("addEventListener fired on " +e.target);
	if (e.target.className == "") {
		selectedFrames.add(i);
		e.target.className = "selected";
	} else {
		selectedFrames.delete(i);
		e.target.className = "";
	}
	
});
*/

function incorrect_frames(){
	//find all selected images using jquery => store into something
	console.log("HELLO WORLD");
	var selectedFrames = $('#frame-container').find('.selected').toArray();
	console.log("selectedFrames:", selectedFrames);
	var getId = selectedFrames.map( function(x) {
		return parseInt( (x.id).substring(1) );
	});
	console.log("getId: ", getId);
	var jsonArray = JSON.stringify( {"selectedFrames": getId} );
	console.log("jsonArray: ", jsonArray);
	$.ajax({
        url: '/face_does_not_exist',
        data: jsonArray,
        datatype: "json",
        type: 'POST',
        success: function(response) {
            console.log("Success: ", response);
        },
        error: function(error) {
            console.log("Failure: ", error);
        }
    });
}

function validate_frames(){
	//find all selected images using jquery => store into something
	console.log("HELLO WORLD");
	var selectedFrames = $('#frame-container').find('.selected').toArray();
	console.log("selectedFrames:", selectedFrames);
	var getId = selectedFrames.map( function(x) {
		return parseInt( (x.id).substring(1) );
	});
	console.log("getId: ", getId);
	var jsonArray = JSON.stringify( {"selectedFrames": getId} );
	console.log("jsonArray: ", jsonArray);
	$.ajax({
        url: '/face_exists',
        data: jsonArray,
        datatype: "json",
        type: 'POST',
        success: function(response) {
            console.log("Success: ", response);
        },
        error: function(error) {
            console.log("Failure: ", error);
        }
    });
}
