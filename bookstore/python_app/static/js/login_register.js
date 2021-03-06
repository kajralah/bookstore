STATIC_URL = '/static/'

function go_to_home_page(){
	window.location.href = "\index.html";
}
function go_to_error_page(){
		window.location.href = "\errorLoginPage.html";
}

function sign_in() {
	$.post("http://localhost:8000/login/", {'name':$("#username").val(),
		   'password':$("#password").val(),'check':document.getElementById("remember").checked,'csrfmiddlewaretoken':$('#csrfmiddlewaretoken').val()},
		function(data){
			if(data == 'Error login'){
				go_to_error_page()
			}
			else if(data == 'ADMIN'){
				$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" id=\"login\"><ul class=\"nav navbar-nav navbar-right\">"+
				"<li><a role=\"button\" href=\"newBook.html\"><i class=\"glyphicon glyphicon-user\"></i> Add book</a>"+
				"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout </a></li> </ul></div>");
			}
			else if(data == 'false'){
				go_to_home_page();
			}
			else{
				$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" ><ul class=\"nav navbar-nav navbar-right\">"+
				"<li><a role=\"button\" href=\"profile-settings.html\"><i class=\"glyphicon glyphicon-user\"></i> Profile</a>"+
				"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout</a></li> </ul></div>");
			}	
		}
	);/*  END of POST request*/
}/*END of signIn*/

function register() {
	$.post("http://localhost:8000/register/", {'username':$("#username-reg").val(),
			'password':$("#password-reg").val(),'address':$("#address-reg").val(),'phone':$("#phone-reg").val(),
			'email':$("#email-reg").val(),'csrfmiddlewaretoken':$('#csrfmiddlewaretoken-reg').val()},
		function(data){
			alert(data);
			if(data == 'Wrong password'){
				alert(data);
				document.getElementById("registerForm").reset();
			}
			if(data == 'User exists'){
				alert(data);
				window.location.reload();
			}
			else{
				window.location.reload();
			}
		}
	);/*  END of POST request*/
}/*END of register*/

function logout(){
	$.post("http://localhost:8000/logout/", {},
		function(data){
			alert(data);
			go_to_home_page();
		}
	);/*  END of POST request*/
}/*END of logout*/

function check_if_user_is_active() {
	$.post("http://localhost:8000/isLoggedUser/", {},
		function(data){
			if (data=== 'False'){
				return;
			}
			else{
				$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" ><ul class=\"nav navbar-nav navbar-right\">"+
				"<li><a role=\"button\" href=\"profile-settings.html\"><i class=\"glyphicon glyphicon-user\"></i> Profile</a>"+
				"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout</a></li> </ul></div>"
				);
			}
		}
	);/*  END of POST request*/
}/*END of register*/

function profile() {
	$.post("http://localhost:8000/profile/", {},
		function(data){
			if (data==='You\'re not logged in'){
				alert(data);
				go_to_home_page();
			}
			else{
				var values=data.split(',');	
				$("#home").replaceWith("<div align=\"right\"><h2 align=\"center\">User info</h2><div align=\"center\"><br><br> Email: <p>"+values[0]+"</p>Address : <p>"+values[1]+"</p>Phone: <p>"+values[2]+"</p></div></div>");
			}
		}
	);/*  END of POST request*/
}/*END of register*/

function liked_products(){
	$.post("http://localhost:8000/liked/", {},
		function(data){
			if (data==='You\'re not logged in'){
				go_to_home_page();
			}
			else{
				var values = data.split(',')
				$("#Liked").append("<p align=\"center\">"+values[0]+"</p>");
				$('#Bought').append("<p align=\"center\">"+values[1]+"</p>");
			}
		}
	);/*  END of POST request*/
}

function categories(){
	$.post("http://localhost:8000/categories/", {},
		function(data){	
			// Remove the parentheses and whitespace
			values = data.replace(/[() ]/g,'');
			var splited_values =values.split(',');
			for (value in splited_values){
				elementWithoutStr=splited_values[value].replace(/'/g, '');
				$("#CategoriesMenu").append("<br><div><a style=\"font-size: 15px;\" onclick=\"category("+ splited_values[value]+ ")\">"+elementWithoutStr+ "</a></div>");
			}
		}
	);/*  END of POST request*/
}

function all(){
	check_if_user_is_active();
	categories();
	show_book();
}

function showing_books(data){
	if(data === '' || data === null){
		return;
	}
	var values = data.split('),');
	$("#tbody").append("<tr>");
	for(var index=0;index<values.length-1;index++){
		if(index%4==0){
			$("#tbody").append("<tr>");
		}	
		var varu = values[index]
		varus = varu.split(',');
		img = varus[varus.length-1];
		img = img.substring(2, img.length - 1);

		$("#tbody").append("<td valign=\"top\" align=\"center\" width=\"30%\" class=\"product-td\"><div align=\"center\">"+
        "<h2 align=\"center\">"+varus[0].substring(2,varus[0].length-1)+"</h2>"+
        "<img src=\"static/img/"+img+"\" width=\"140\" height=\"140\" alt=\"\" style=\"display:block;\"/>"+
        "<p align=\"center\"><h4 align=\"center\">Price: "+ varus[1]+ " BGN<h4> <button onclick=\"showProduct("+varus[0].substring(1,varus[0].length)+")\"> View </button></p>"+"</div></td>");
	}
	$("#tbody").append("</tr>");
}


function category(category){
	$.post("http://localhost:8000/category/", {category:category},
		function(data){
			$("#tbody").empty();
			showing_books(data);
		}
	);
}

function show_book(){
	$.post("http://localhost:8000/show_book/", {},
		function(data){	
			showing_books(data);
		}//end of function
	);//end of post
}//show_book

function load_profile(){
	$.post("http://localhost:8000/isLoggedUser/", {},
		function(data){
			if(data === 'False'){
				go_to_home_page();
			}
			else{
				profile();
			}
		}
	);
}

function add_categories(){
	$.post("http://localhost:8000/categories/", {},
		function(data){			
			// Remove the parentheses and whitespace
			values = data.replace(/[() ]/g,'');

			var splited_values =values.split(',');

			for (value in splited_values){
				elementWithoutStr=splited_values[value].replace(/'/g, '');
				$("#prod-categories-reg").append("<a style=\"font-size:20px;\" onclick=\"setCategories("+splited_values[value]+")\">"+elementWithoutStr+"</a><br>");
			}
		}
	);/*  END of POST request*/
}

function add_new_book(){
	$.post("http://localhost:8000/is_supervisor/", {},
		function(data){
			if(data === 'False'){
				go_to_home_page();
			}
			else{
				add_categories();
			}
		}
	);/*END OF POST */
}/*END OF addNewBook() */


function set_categories(index){
	$("#prod-categories-reg").append("<input type=\"text\" name=\"category-input\" value=\""+index+ "\" />	")
}

function show_product(title){
	window.open("http://localhost:8000/books?title="+title);
}


function bought_books(){
	$.post("http://localhost:8000/boughtBooks/", {},
		function(data){
			if(data == '' || data == null){
				return;
			}
			var values = data.split('),');
			$('#tbody').append("<th style=\"text-align: center\">Title</th>");
			$('#tbody').append("<th style=\"text-align: center\">Price</th>");
			$('#tbody').append("<th style=\"text-align: center\">Buy date:</th>");
			$('#tbody').append("<th style=\"text-align: center\">Info:</th>");
			for(var index=0;index<values.length-1;index++){
				$("#tbody").append("<tr>");
				var varu = values[index];
				varus = varu.split(',');

				$("#tbody").append("<td class=\"td\"> <h4 align=\"center\">"+varus[1].substring(2,varus[1].length-1)+"</h2></td>"+
                "<td class=\"td\"><h4 align=\"center\">"+ varus[2]+ " BGN<h4></td>");
              	$("#tbody").append("<td class=\"td\">"+varus[9].substring(2,varus[9].length-1)+"</td>");
                $("#tbody").append("<td class=\"td\"><button onclick=\"showProduct("+varus[1].substring(1,varus[1].length)+")\"> View </button></td>");
				$("#tbody").append("</tr>");
			}

		}
	);/*END of post */
}/*END of boughtBooks */

function load_page(){
	$.post("http://localhost:8000/isLoggedUser/", {},
		function(data){
			if(data === 'False'){
				go_to_home_page();
			}
		}
	);
}

function search_category(){
	var search = document.getElementById('search').value;
	event.preventDefault();
	$.post("http://localhost:8000/searchCategory/", {'whatToSearchFor':search},
		function(data){
			$("#tbody").empty();
			showing_books(data);
		}
	);
}
