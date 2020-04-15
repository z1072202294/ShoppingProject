$(function(){

// Test 自动化
	var reg = null;
	var log = '{{login}}'||null;


// Pages loaded check register or login
	console.log(reg);
	console.log(login);

	$(document).ready(function () {
		judgRegisOrLogin()
	});




// Judg resig or login
	function judgRegisOrLogin(){
		if(reg){

			$("#idRegis").trigger('click')
			disposeRegis();

		} else {

			$("#idLogin").trigger('click')
			disposeLogin()

		}
	}


// Judg username
	function judgUser(){
		let name = $('#formRegis input[name=username]');
		let realLink = '{% url register%}';
		let testLink = '/user/register/';
		let response = reqRegis(name,testlink,"post");
		if (response==false){
			alert("请求失败,未知的错误")
		}else{
			// success => login
			let realLogLink = '{% url login %}';
			let testLoginLink = 'user/login/';
			window.location.href=testLoginLink
		}
	}

// Judg pwd
	function judgPwd(){
		let pwdObject = $('#formRegis input[type="password"]') ;
		let pwd1 = pwdObject[0].value;
		let pwd2 = pwdObject[1].value;
		if(pwd1==pwd2){
			return true
		}else{
			alert("密码不一致")
			return false
		}
	}

// Dispose register
	function disposeRegis(){
		if (judgPwd()==judgUser()){
			$('#Submit').click(function () {
				reqRegis()
			})
		}
	}

// Dispose login
	function disposeLogin(judg){
		if(judg=="register"){
			return
		}else{
			return
		}
	}

// Register req backend
	function reqRegis(data,url,judgReqMethod) {
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
		}

		if(judgReqMethod=="GET"|| judgReqMethod=="get"){
			// 3.建立连接
			xhr.open('get', url, true)

			// 4.发送数据
			xhr.send()

		}else{
			// post
			// 3.1建立连接
			xhr.open('post',url, true)

			// 3.2 post请求 要设置请求头
			xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded')

			// 4.发送   参数名称 是 服务器端规定好的
			xhr.send(JSON(data))
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
	  }
	xmlhttp.open("GET","gethint.asp?q="+str,true);
	xmlhttp.send();
	}


});