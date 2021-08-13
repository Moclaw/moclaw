var a = document.getElementById("done");
var b = document.getElementById("myBtn");
var c = document.getElementById("myBtnYes");
c.addEventListener("click",myBton)
clicks =0;
function myFunction()
{
    var i = Math.floor(Math.random()*150)+20;
    var j = Math.floor(Math.random()*150)+20;
    b.style.left = i+"px";
    b.style.top = j+"px";
	if(i > 150 || j > 150 ){
	b.style.left = -i+ "px";
	b.style.top = -j+"px";
	};
	clicks +=1;
	if(clicks >=10){
	b.style.left = 0+"px";
	b.style.top = 0+"px";
	document.getElementById("myBtn").disabled = true;
	a.innerHTML = "Nhấn có đi không nhấn không được đâu lêu lêu"
	}
}
function myBton(){
a.innerHTML = "Vậy thì không nhắn tin đi";
}