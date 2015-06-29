STATIC_URL = '/static/'

function signIn() {
		$.post("http://localhost:8000/login/", {'name':$("#username").val(),
				'password':$("#password").val(),'check':document.getElementById("remember").checked,'csrfmiddlewaretoken':$('#csrfmiddlewaretoken').val()},
				function(data){
					if(data == 'Error login'){
						window.location.load("errorLoginPage.html")
					}
					else if(data == 'ADMIN'){
						$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" id=\"login\"><ul class=\"nav navbar-nav navbar-right\">"+
						"<li><a role=\"button\" href=\"newBook.html\"><i class=\"glyphicon glyphicon-user\"></i> Add book</a>"+
						"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout </a></li> </ul></div>")
					}
					else if(data == 'false'){
						window.location.load("index.html")
					}
					else{
						$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" ><ul class=\"nav navbar-nav navbar-right\">"+
						"<li><a role=\"button\" href=\"profile-settings.html\"><i class=\"glyphicon glyphicon-user\"></i> Profile</a>"+
					"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout</a></li> </ul></div>")
					}
				}
			);/*  END of POST request*/
		}/*END of signIn*/

function index(){
	$.post("http://localhost:8000/index/", {},
		function(data){
			if(data == 'ADMIN'){
				$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" id=\"login\"><ul class=\"nav navbar-nav navbar-right\">"+
						"<li><a role=\"button\" href=\"newBook.html\"><i class=\"glyphicon glyphicon-user\"></i> Add book</a>"+
						"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout </a></li> </ul></div>")
			}
			else if (data ='None'){
				window.location.load('index.html')
			}
			else{
				$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" ><ul class=\"nav navbar-nav navbar-right\">"+
						"<li><a role=\"button\" href=\"profile-settings.html\"><i class=\"glyphicon glyphicon-user\"></i> Profile</a>"+
					"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout</a></li> </ul></div>")
			}
		}
	)/*end of POST*/
}/*end of index()*/

function register() {
		$.post("http://localhost:8000/register/", {'username':$("#username-reg").val(),
				'password':$("#password-reg").val(),'address':$("#address-reg").val(),'phone':$("#phone-reg").val(),
				'email':$("#email-reg").val(),'csrfmiddlewaretoken':$('#csrfmiddlewaretoken-reg').val()},
				function(data){
					alert(data)
					if(data == 'Wrong password'){
						alert(data)
						document.getElementById("registerForm").reset();
					}
					if(data == 'User exists'){
						alert(data)
						window.location.reload()
					}
					else{
						window.location.reload()
					}
				}
			);/*  END of POST request*/
		}/*END of register*/

function logout(){
	$.post("http://localhost:8000/logout/", {},
				function(data){
					alert(data)
					window.location.replace("index.html")
				}
			);/*  END of POST request*/
		}/*END of logout*/

function profile() {
		$.post("http://localhost:8000/profile/", {},
				function(data){
					if (data=='You\'re not logged in'){
						alert(data)
						window.location.replace("index.html")
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
					if (data=='You\'re not logged in'){
						alert(data)
						window.location.replace("index.html")
					}
					else{
						var values = data.split(',')
						$("#Liked").append("<p align=\"center\">"+values[0]+"</p>");
						$('#Bought').append("<p align=\"center\">"+values[1]+"</p>");
						}
				}
			);/*  END of POST request*/
}

function go_to_home_page(){
	window.location.href = "index.html";
}

function categories(){
	$.post("http://localhost:8000/categories/", {},
				function(data){			

					// Remove the parentheses and whitespace
					values = data.replace(/[() ]/g,'')

					var splited_values =values.split(',')

					function splitvar(element,index,array){
						array.pop();
						array[index]=array[index].replace(/'/g, '');
						$("#CategoriesMenu").append("<br><div><a style=\"font-size: 15px;\" onclick=\"cat("+ element+ ")\">"+array[index]+ "</a></div>");
					}
					splited_values.forEach(splitvar);
				}
			);/*  END of POST request*/
}

function cat(index){
	alert(index)	
}

function All(){
	categories();
	showBook()
}
function showBook(){
	$.post("http://localhost:8000/show_book/", {},
		function(data){	

			if(data == '' || data == null){
				return;
			}
			var values = data.split('),')

			$("#tbody").append("<tr>");
			for(var index=0;index<values.length-1;index++){
				if(index==4){
					$("#tbody").append("<tr>");
				}
				
				var varu = values[index]
				varus = varu.split(',')
				img = varus[varus.length-1]
				img = img.substring(2, img.length - 1);

				$("#tbody").append("<td valign=\"top\" align=\"center\" width=\"20%\" class=\"product-td\"><div align=\"center\">"+
                   "<h2 align=\"center\">"+varus[0].substring(2,varus[0].length-1)+"</h2>"+
                "<img src=\"static/img/"+img+"\" width=\"140\" height=\"140\" alt=\"\" style=\"display:block;\"/>"+
                "<p align=\"center\"><h4 align=\"center\">Price: "+ varus[1]+ " BGN<h4> <button onclick=\"showProduct("+varus[0].substring(1,varus[0].length)+")\"> View </button></p>"+"</div></td>");
			}
			$("#tbody").append("</tr>");
	}//end of function
)//end of post
}//show_book

function addCategories(){
	$.post("http://localhost:8000/categories/", {},
				function(data){			

					// Remove the parentheses and whitespace
					values = data.replace(/[() ]/g,'')

					var splited_values =values.split(',')

					function splitvar(element,index,array){
						array.pop();
						array[index]=array[index].replace(/'/g, '');
						$("#prod-categories-reg").append("<a style=\"font-size:20px;\" onclick=\"setCategories("+element+")\">"+array[index]+"</a><br>");
					}
					splited_values.forEach(splitvar);
				}
			);/*  END of POST request*/
}
function setCategories(index){
	$("#prod-categories-reg").append("<input type=\"text\" name=\"category-input\" value=\""+index+ "\" />	")
}

function showProduct(name){
	$.post("http://localhost:8000/showProduct/", {'name':name},
				function(data){		
					alert(data)	
				
				}
			);/*  END of POST request*/
}