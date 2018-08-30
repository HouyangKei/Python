//登录js
var fl=true;
$(document).ready(function(){
	 $("#login-btn").click(function(event){
		 if($("#username").val()==""){
			 alert("用户名不能为空哦!")
			 return false;
		 }
		 if($("#password").val()==""){
			 alert("密码不能为空哦!")
			 return false;
		 }
		 $.ajax({
	         type : 'POST',
	         url : "/blog.do",
	         dataType : 'json',
	         data:$("#login").serialize(),
	         cache : false,
	         async:false,
	         beforeSend: function () {
	        	// 禁用按钮防止重复提交
	        	$(".login-btn").attr("flag","false");
		     },
	         error : function(e) {
	          return false;
	         },
	         success : function(json){
	        	 if(json.code=="0000"){
	        		 alert("登录成功"+json.username)
	        		 location.href="/index";
	        	 }else{
	        		 alert("登录失败，用户名或者密码不对哦--"+json.username)
	        	 }
	        	
	         },
	         complete: function () {
		        $(".login-btn").attr("flag","true");
			 }
	      });
		 
	 })
	 
	 
});