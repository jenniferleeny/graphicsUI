
window.onload = function() {
	var selectedFrames = new Set();
	//output all the frames
	var parentContainer = document.getElementById("parent");
	var intViewportWidth = window.innerWidth;
	var container = document.createElement("container");
	$.getJSON("./static/visual_data_UI.json", function(data) {
		console.log("About to request JSON");
		console.log(data); 
		var L = data["myimages"];
		console.log(L);
		for (var i = 0; i < L.length ; i++) {
			var itemContainer = document.createElement("item");
			//set image object
			var newImg = document.createElement("img");
			newImg.src = "./static/visual_files/" + L[i]["jpeg_file"];
			newImg.id = "a" + (L[i]["id"]).toString();
    		console.log("ID: #" + newImg.id);
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
			var yfactor = 200/newImg.naturalHeight;
			var xfactor = 300/newImg.naturalWidth;
			//console.log(xfactor, yfactor);
			newImg.height = 200; 
			newImg.width = 300;
			//set svg object
			var newSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
			var box = document.createElementNS("http://www.w3.org/2000/svg", "rect");
			var w = Math.round(xfactor * L[i]["bbox0"][3]);
			var h = Math.round(yfactor * L[i]["bbox0"][2]);
			var y = Math.round(yfactor * L[i]["bbox0"][1]);
			var x = Math.round(xfactor * L[i]["bbox0"][0]);
			console.log(w, h, y, x);
			newSvg.setAttribute('width', newImg.width);
			newSvg.setAttribute('height', newImg.height);

			box.setAttribute('fill', 'none');
			box.setAttribute('stroke', 'red');
			box.setAttribute('stroke-width', "3");
			//what happens if box coord does not exist?
			box.setAttribute("width", w);
			box.setAttribute("height", h);
			box.setAttribute("y", y);
			box.setAttribute("x", x);
			//console.log(box.width, box.height, box.y, box.x);
			newSvg.appendChild(box);
			//set div objects
			var divImg = document.createElement("div"); divImg.className = "floatTL"; 
			var divSvg = document.createElement("div"); divSvg.className = "floatTL";
			//positions of images (Mathy part!)
			var imgWidth = newImg.width;
			var imgHeight = newImg.height;
			var margin = 5;
			var max = Math.floor(intViewportWidth/(margin+imgWidth));
			divImg.style.left = 5+(imgWidth+margin)*(i%max) +'px'; 
			divSvg.style.left = 5+(imgWidth+margin)*(i%max) +'px'
			divImg.style.top =  150+(imgHeight+margin)*Math.floor(i/max) +'px';
			divSvg.style.top =  150+(imgHeight+margin)*Math.floor(i/max) +'px';
			//console.log(divImg.style.left, divSvg.style.left);
			//console.log(divImg.style.top, divSvg.style.top);
			divImg.appendChild(newImg);
			divSvg.appendChild(newSvg);
			itemContainer.appendChild(divImg);
			itemContainer.appendChild(divSvg);
			

			console.log(itemContainer);
			container.appendChild(itemContainer);
			
		}
		parentContainer.appendChild(container);
	});
}

function incorrect_frames(){
	//find all selected images using jquery => store into something
	console.log("HELLO WORLD");
	var selectedFrames = $('#parent').find('.selected').toArray();
	console.log("selectedFrames:", selectedFrames);
	var getId = selectedFrames.map( function(x) {
		return parseInt( (x.id).substring(1) );
	});
	console.log("getId: ", getId);
	var jsonArray = JSON.stringify( {"selectedFrames": getId} );
	console.log("jsonArray: ", jsonArray);
	$.ajax({
        url: '/wrong_bbox',
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
	var selectedFrames = $('#parent').find('.selected').toArray();
	console.log("selectedFrames:", selectedFrames);
	var getId = selectedFrames.map( function(x) {
		return parseInt( (x.id).substring(1) );
	});
	console.log("getId: ", getId);
	var jsonArray = JSON.stringify( {"selectedFrames": getId} );
	console.log("jsonArray: ", jsonArray);
	$.ajax({
        url: '/correct_bbox',
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
