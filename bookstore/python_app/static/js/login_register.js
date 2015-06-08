function signIn() {
		$.post("http://localhost:8000/login/", {'name':$("#username").val(),
				'password':$("#password").val(),'check':document.getElementById("remember").checked,'csrfmiddlewaretoken':$('#csrfmiddlewaretoken').val()},
				function(data){
					if(data == 'Error login'){
						window.location.replace("errorLoginPage.html")
					}
					else if(data == 'ADMIN'){
						$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" ><ul class=\"nav navbar-nav navbar-right\">"+
						"<li><a role=\"button\" href=\"profile-settings.html\"><i class=\"glyphicon glyphicon-user\"></i> Add book</a>"+
						"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout </a></li> </ul></div>")
					}
					else{
						$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" ><ul class=\"nav navbar-nav navbar-right\">"+
						"<li><a role=\"button\" href=\"profile-settings.html\"><i class=\"glyphicon glyphicon-user\"></i> Profile</a>"+
					"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout</a></li> </ul></div>")
					}
				}
			);/*  END of POST request*/
		}/*END of signIn*/


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