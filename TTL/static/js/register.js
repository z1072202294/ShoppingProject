$(function(){	
	
// Test
	var reg = '{{ register }}'||null;
	var log = '{{ login }}'||null;


// Pages loaded check register or login
	console.log(reg);
	console.log(log);

	$(document).ready(function () {
		judgRegisOrLogin();

		$('#username').blur(function() {
		check_user_name();
		});

		$('#pwd1').blur(function() {
			check_pwd();
		});

		$('#pwd2').blur(function() {
			check_cpwd();
		});

		$('#email').blur(function() {
			check_email();
		});

		$('#tel').blur(function() {
			check_tel();
		});
	});





	function check_user_name(){

		var len = $('#username').val().length;

		if(len<6||len>15)
		{
			$('#username').next().html('输入6-15个字符的用户名');
			$('#username').next().show();
		}
		else
		{
			$('#username').next().hide();
			let url = window.location.href;

			  $.post(url,
				  {
					name:$('#username').value,
				  },
				  function(data,status){
					let dit = {
						result:data,
						Status: status
					};
					if (dit.result == 0) {
                    	$('#username').next().html('用户名已经存在').show();
                	}else{
                    	$('#username').next().hide();
                	}
				  });
        }
	}

	function check_pwd() {
		var len = $('#pwd1').val().length;
		if(len<6)
		{
			$('#pwd1').next().html('密码至少6位');
			$('#pwd1').next().show();
		}
		else
		{
			$('#pwd1').next().hide();
		}
	}

	function check_cpwd(){
		var pass = $('#pwd1').val();

		var cpass = $('#pwd2').val();

		if(cpass==pass)
		{
			$('#pwd2').next().hide();

		}
		else
		{
			$('#pwd2').next().html('两次输入的密码不一致');
			$('#pwd2').next().show();
		}

	}
	
	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确');
			$('#email').next().show();
		}

	}


	function check_tel(){
		var len = $('#tel').val().length;
		if (len==11)
		{
			$('#tel').next().hide();
		}
		else
		{
			$('#tel').next().html('');
			$('#tel').next().show();
		}
	}

	
// Judg resig or login
	function judgRegisOrLogin(){
		if(reg){
			$("#idRegis").trigger('click');
			disposeRegis();
			
		} else {
			
			$("#idLogin").trigger('click');
			disposeLogin()
			
		}	
	}

// Dispose register
	function disposeRegis(){
		$('#regisSubmit').click(function () {
			judgUser()

		});
	}

// Dispose login
	function disposeLogin(judg){
		$('#loginSubmit').click(function () {
			if(loginJudg()) {
				linkIndex()
			}
		});
	}


/*	====Regis judg==== */

 	// Judg username
	function judgUser(){

		let usname = $('#username').val();
		let pswd = $('#pwd1').val();
		let email = $('#email').val();
		let tel = $('#tel').val();
		let data = {
			nickname:usname,
			pwd:pswd,
			email:email,
			tel:tel
		};
		alert(usname);
		alert(pswd);
		let realRegisLink = window.location.href;

		///                $.ajaxSetup({
		//                    data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
		//               });
		$.post(realRegisLink,
		data,
  		function(data,status){
    		alert("Data: " + data + "\nStatus: " + status);
    		if(data)
    		{
				let realLogLink = "/user/login/";

				window.location.href=realLogLink
			}else{
    			alert("注册失败未知的错误")
			}
		});

		// let response = reqBackend(data,realRegisLink,"post");
		// if(response==false)
		// {
		// 	alert("请求失败,未知的错误")
		// }
		// else
		// {
		// 	let realLogLink = '{% url login %}';
		// 	// let testLoginLink = 'user/login/';
		// 	window.location.href=realLogLink
		// }
	}
	
	// Judg pwd
	function judgPwd(){
		let pwdObject = $('#formRegis input[type="password"]') ;
		let pwd1 = pwdObject[0].value;
		let pwd2 = pwdObject[1].value;
		if(pwd1==pwd2){
			return true
		}else{
			alert("密码不一致");
			return false
		}
	}


/*	====Login judg==== */

	// Go to the backend judg
	function loginJudg() {
		let data = {
			"nickname":$('#formLogin input[type="text"]').value,
			"password":$('#formLogin input[type="password"]').value
		};
		if(reqBackend(data,window.location.href,"post")==false){
			alert()
		}
	}

	// Login successed link index
	function linkIndex() {

	}

/* 	Ajax req backend	*/
	function reqBackend(data,url,judgReqMethod) {
		var xmlhttp;
		if (window.XMLHttpRequest){
			// code for IE7+, Firefox, Chrome, Opera, Safari
		  xmlhttp = new XMLHttpRequest();
		  return chooseMethod(xmlhttp,data,url,judgReqMethod)
		  
	  }else{
			  // code for IE6, IE5
		  xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
		  return chooseMethod(xmlhttp,data,url,judgReqMethod)
			
	  }
	}


// Choose req method
	function chooseMethod(xhr,data,url,judgReqMethod){
			// 2.连接成功后的处理函数(回调函数)
		xhr.onreadystatechange = function(){
			if (xhr.readyState==4 && xhr.status==200) {
				return xhr
			}else{
				return false
			}
		};
		
		if(judgReqMethod=="get"){
			// 3.建立连接
			xhr.open('get', url, true);

			// 4.发送数据
			xhr.send()
			
		}else{
			// post
			// 3.1建立连接
			xhr.open('post',url, true);

			// 3.2 post请求 要设置请求头
			xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded');

			// 4.发送   参数名称 是 服务器端规定好的
			xhr.send(data)
		}
	}








// 搜索 <ajax>
	function showHint(str)
	{
	var xmlhttp;
	if (str.length==0)
	  {
	  document.getElementById("txtHint").innerHTML="";
	  return;
	  }
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
	  if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
		document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
		}
	  };
	xmlhttp.open("GET","gethint.asp?q="+str,true);
	xmlhttp.send();
	}
	

});