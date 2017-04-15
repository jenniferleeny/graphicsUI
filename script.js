/*window.onload = function() {

	var container = document.getElementById("img-container");
	$.getJSON("visual_data_UI.json", function(data) {getJSON is a string -> object
		var L = data["myimages"];
		for (var i = 0; i < L.length; i++) {
			var newElt = document.createElement("img");
			newElt.src = "./visual_files/" + L[i]["jpeg_file"];
			newElt.height = 200;
			newElt.width = 200;

			container.appendChild(newElt);
		}
	});
}
*/

window.onload = function() {
	var parentContainer = document.getElementById("parent");
	var intViewportWidth = window.innerWidth;
	var container = document.createElement("container");
	
	console.log("hello world!")
	var newImg = document.createElement("img");
	newImg.src = "./visual_files/frame0.jpg";
	var src = document.createElement("div");
	src.appendChild(newImg);
/*
	$.getJSON("visual_data_UI.json", function(data) {
		console.log(data); 
		var L = data["myimages"];
		console.log(L);
		for (var i = 0; i < L.length ; i++) {
			var itemContainer = document.createElement("item");
			//itemContainer.setAttribute("order", i);
			//set image object
			var newImg = document.createElement("img");
			newImg.src = "./visual_files/" + L[i]["jpeg_file"];
			newImg.height = 200;
			newImg.width = 200;
			//set svg object
			var newSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
			var box = document.createElementNS("http://www.w3.org/2000/svg", "rect");
			var w = L[i]['width'];
			var h = L[i]['height'];
			var y = L[i]['y'];
			var x = L[i]['x'];
			console.log(w, h, y, x)
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
			divSvg.style.left = 5+(imgWidth+margin)*(i%max) +'px';
			console.log(divImg.style.left);
			divImg.style.top =  150+205*Math.floor(i/max) +'px';
			divSvg.style.top =  150+205*Math.floor(i/max) +'px';
			divImg.appendChild(newImg);
			divSvg.appendChild(newSvg);
			itemContainer.appendChild(divImg);
			itemContainer.appendChild(divSvg);
			container.appendChild(itemContainer);
			
		}
		parentContainer.appendChild(container);
	});*/
}
