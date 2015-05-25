function signIn() {
		$.post("http://localhost:8000/login/", {'name':$("#username").val(),
				'password':$("#password").val(),'check':document.getElementById("remember").checked,'csrfmiddlewaretoken':$('#csrfmiddlewaretoken').val()},
				function(data){
					if(data == 'Error login'){
						window.location.replace("errorLoginPage.html")
					}
					else{
						$('#navbar-collapse').empty().html("<div class = \"navbar-collapse collapse\" ><ul class=\"nav navbar-nav navbar-right\">"+
						"<li><a role=\"button\" href=\"profile-settings.html\"><i class=\"glyphicon glyphicon-user\"></i> Profile</a>"+
					"</li><li><a  onclick=\"logout()\"><i class=\"glyphicon glyphicon-lock\"></i> Logout</a></li> </ul></div>")
					}
				}
			);/*  END of POST request*/
		}/*END of SEND REQUEST*/

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
				;}/* END OF .html */
			);/*  END of POST request*/
		}/*END of SEND REQUEST*/