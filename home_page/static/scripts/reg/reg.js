$(document).ready(function(){
	$("#mobileReg").click(function(){
		$(this).siblings().removeAttr("class");
		$(this).toggleClass("active");
		$("#phoneWrap").css({"display":"block"});
		$("#email").val("");
		$("#emailWrap").css({"display":"none"});
	});
	$("#emailReg").click(function(){
		$(this).siblings().removeAttr("class");
		$(this).toggleClass("active");
		$("#phoneWrap").css({"display":"none"});
		$("#phone").val("");
		$("#emailWrap").css({"display":"block"});
	});

	<!--用户名验证 -->
	$("#username").focus(function(){
		$("#username_Tip").removeAttr("class");
		$("#username_Tip").toggleClass("action");
		$("#username_Tip").children().html("4-20位,注册成功后用户名不能修改");
	});

	$("#username").blur(function(){
		vfname();
	});

	<!--手机号验证 -->
	$("#phone").focus(function(){
		$("#phone_Tip").removeAttr("class");
		$("#phone_Tip").toggleClass("action");
		$("#phone_Tip").children().html("请输入您的手机号码");
	});

	$("#phone").blur(function(){
		vfphone();
	});

	<!--邮箱验证 -->
	$("#email").focus(function(){
		$("#email_Tip").removeAttr("class");
		$("#email_Tip").toggleClass("action");
		$("#email_Tip").children().html("请输入您的邮箱");
	});

	$("#email").blur(function(){
		vfemail();
	});

	<!--密码验证 -->
	$("#password").focus(function(){
		$("#password_Tip").removeAttr("class");
		$("#password_Tip").toggleClass("action");
		$("#password_Tip").children().html("密码长度6-16位");
	});

	$("#password").blur(function(){
		vfpassword();
	});

	$("#cpassword").focus(function(){
		$("#cpassword_Tip").removeAttr("class");
		$("#cpassword_Tip").toggleClass("action");
		$("#cpassword_Tip").children().html("请再次输入您的密码");
	});

	$("#cpassword").blur(function(){
		vfcpassword();
	});

	// var validator = new FormValidator('register-form',[{
	// 	name:'username',
	// 	display:'required',
	// 	rules:'required|max_length[20]|min_length[1]',
	// },{
	// 	name:'phone',
	// 	rules:'exact_length[11]|integer',
	// },{
	// 	name:'email',
	// 	rules:'valid_email',
	// },{
	// 	name:'password',
	// 	display:'required',
	// 	rules:'min_length[6]|max_length[30]',
	// },{
	// 	name:'cpassword',
	// 	display:'required',
	// 	rules:'matches[password]',
	// }],function(errors,event){
	// 	if(errors.length > 0){
	// 		vfname();
	// 		vfemail();
	// 		vfphone();
	// 		vfpassword();
	// 		vfcpassword();
	// 	}
	// });
	$("#btnNext").click(function(){
		// alert('submit');
		$("#reg-form").submit();
	});
});

function vfname(){
	var text = $("#username").val();
	var result = false;
	if(text.length>=4 && text.length<=20){
		result = true;
	} else{
		result = false;
	}
	if(result){
		$("#username_Tip").removeAttr("class");
		$("#username_Tip").toggleClass("success");
		$("#username_Tip").children().html("");
	}else{
		$("#username_Tip").removeAttr("class");
		$("#username_Tip").toggleClass("wrong");
		$("#username_Tip").children().html("您输入的用户名无效");
	}
}

function vfphone(){
	var text = $("#phone").val();
	var result = false;
	
	if(text.length!=11){
		result = false;
	} else if(text.search(/^[0-9]+$/)==-1){
		result = false;
	} else{
		result = true;
	}
	if(result){
		$("#phone_Tip").removeAttr("class");
		$("#phone_Tip").toggleClass("success");
		$("#phone_Tip").children().html("");
	} else {
		$("#phone_Tip").removeAttr("class");
		$("#phone_Tip").toggleClass("wrong");
		$("#phone_Tip").children().html("请输入正确的手机号码");
	}
}

function vfemail(){
	var text = $("#email").val();
	var result = false;
	if (text.search(/^[_/.a-z0-9]+@[a-z0-9]+[/.][a-z0-9]{2,}$/i)==-1) {
		result = false;
	} else {
		result = true;
	}
	if(result){
		$("#email_Tip").removeAttr("class");
		$("#email_Tip").toggleClass("success");
		$("#email_Tip").children().html("");
	} else {
		$("#email_Tip").removeAttr("class");
		$("#email_Tip").toggleClass("wrong");
		$("#email_Tip").children().html("您输入的邮箱有误");
	}
}

function vfpassword(){
	var text = $("#password").val();
	var result = false;
	if(text.length>=6 && text.length<=16)
		result=true;
	else
		result=false;
	if (result) {
		$("#password_Tip").removeAttr("class");
		$("#password_Tip").toggleClass("success");
		$("#password_Tip").children().html("");
	}else{
		$("#password_Tip").removeAttr("class");
		$("#password_Tip").toggleClass("wrong");
		$("#password_Tip").children().html("您输入的密码有误");
	};
	return result;
}

function vfcpassword(){
	var text = $("#cpassword").val();
	var passtext = $("#password").val();
	var result = false;
	if(text==passtext)
		result=true;
	else
		result=false;
	if (result) {
		$("#cpassword_Tip").removeAttr("class");
		$("#cpassword_Tip").toggleClass("success");
		$("#cpassword_Tip").children().html("");
	}else{
		$("#cpassword_Tip").removeAttr("class");
		$("#cpassword_Tip").toggleClass("wrong");
		$("#cpassword_Tip").children().html("两次输入的密码不一致");
	};
}