/* Manage links in the documents here - also change text in template topbar.html when changes need to be made */

$(document).ready(function() {
	
	/* $("#mycontent").load("defhome.html"); */

	var listNav = {
			"item01" : "/voyage/index.html",
			"item01a" : "/voyage/guide.html",
			"item01b" : "/voyage/search.html",
			"item01c" : "/voyage/download.html",
			"item01d" : "/voyage/submission-login.html",
			
			"item02" : "/assessment/index.html",
			"item02a" : "/assessment/essays-intro.html",
			"item02b" : "/assessment/estimates.html",
			"item02c" : "/assessment/intro-maps.html",
			
			"item03" : "/resources/index.html",
			"item03a" : "/resources/images.html",
			"item03b" : "/resources/origins.html",
			
			"item04" : "/education/index.html",
			"item04a" : "/education/lessons-plans.html",
			"item04b" : "/education/others.html",
			
			"item05" : "/about/index.html",
			"item05a" : "/about/history.html",
			"item05b" : "/about/team.html",
			"item05c" : "/about/data.html",
			"item05d" : "/about/acknowledgements.html",
			"item05e" : "/about/origins.html",
			"item05f" : "/about/contacts.html",

		}
	/*
	$.each(listNav, function(key, value) {
		// load about page on click
		$("#" + key).click(function(){
			
			$("#mycontent").load(value);
			
		});
	}); 
	*/
	/*
	$.each(listNav, function(key, value) {
				// load about page on click
		$("#" + key).click(function(){
			
			$("#mycontent").load(value, function() {
				 $("#mycontent") .resize();
				}	
			);
			
		});
	}); 
	*/
	
	$.each(listNav, function(key, value) {
				// load about page on click
		$("#" + key).click(function(){
			window.location = value;
		});
	}); 
});


