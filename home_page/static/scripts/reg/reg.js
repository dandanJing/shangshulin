$(document).ready(function(){
	$("#mobileReg").click(function(){
		$(this).siblings().removeAttr("class");
		$(this).toggleClass("active");
		$("#phoneWrap").css({"display":"block"});
		$("#emailWrap").css({"display":"none"});
	});
	$("#emailReg").click(function(){
		$(this).siblings().removeAttr("class");
		$(this).toggleClass("active");
		$("#phoneWrap").css({"display":"none"});
		$("#emailWrap").css({"display":"block"});
	});

	$("#btnNext").click(function(){
		$("#reg-form").submit();
		// alert('click');
	});
});