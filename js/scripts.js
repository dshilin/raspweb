/* activate scrollspy menu */
$('body').scrollspy({
  target: '#navbar-collapsible',
  offset: 180
});

/* smooth scrolling sections */
$('a[href*=\\#]:not([href=\\#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top - 50
        }, 800);
        
        if (this.hash=="#section1") {
            $('.scroll-up').hide();
        }
        else {
            $('.scroll-up').show();
        }
        
        
        // activte animations in this section
        target.find('.animate').delay(1000).addClass("animated");
        setTimeout(function(){
            target.find('.animated').removeClass("animated");
        },2000);
        return false;
      }
    }
});

function getCurTemp() {
	nocache = "&nocache=" + Math.random() * 1000000;
	var request = new XMLHttpRequest();
	request.onreadystatechange = function() {
		if (request.readyState === 4) {
			if (request.status === 200) {
				document.getElementById('temp').innerHTML = request.responseText;
			} else {
				alert("Что то пошло не так, попробуйте перезагрузить страницу.");
			}
		}
	};
	request.open('POST', '/select_current_temp.py', true);
	request.send(null);
	setTimeout('getCurTemp()', 4000);
	return false;  // Prevent the default button action
};

function getCurHum() {
	nocache = "&nocache=" + Math.random() * 1000000;
	var request = new XMLHttpRequest();
	request.onreadystatechange = function() {
		if (request.readyState === 4) {
			if (request.status === 200) {
				document.getElementById('hum').innerHTML = request.responseText;
			} else {
				alert("Что то пошло не так, попробуйте перезагрузить страницу.");
			}
		}
	};
	request.open('POST', '/select_current_hum.py', true);
	request.send(null);
	setTimeout('getCurHum()', 4000);
	return false;
};

$("#process p").click(function() {
	$("#process p").toggle();
});

$(document).ready(function getHumPar() {
	nocache = "&nocache=" + Math.random() * 1000000;
	var request = new XMLHttpRequest();
	request.onreadystatechange = function() {
		if (request.readyState === 4) {
			if (request.status === 200) {
				var x = request.responseText;
				x = parseFloat(x);
				document.getElementById('humidity').value = x;
			} else {
				alert("Что то пошло не так, попробуйте перезагрузить страницу.");
			}
		}
	};
	request.open('POST', '/get_hum_par.py', true);
	request.send(null);
	return false;
});
	
$(document).ready(function getTempPar() {
	nocache = "&nocache=" + Math.random() * 1000000;
	var request = new XMLHttpRequest();
	request.onreadystatechange = function() {
		if (request.readyState === 4) {
			if (request.status === 200) {
				var x = request.responseText;
				x = parseFloat(x);
				document.getElementById('temperature').value = x;
				
			} else {
				alert("Что то пошло не так, попробуйте перезагрузить страницу.");
			}
		}
	  };
	request.open('POST', '/get_temp_par.py', true);
	request.send(null);
	return false;
});

$(document).ready(function getAerStartPar() {
	nocache = "&nocache=" + Math.random() * 1000000;
	var request = new XMLHttpRequest();
	request.onreadystatechange = function() {
		if (request.readyState === 4) {
			if (request.status === 200) {
				var x = request.responseText;
				x = parseFloat(x);
				document.getElementById('aer-start').value = x;
			} else {
				alert("Что то пошло не так, попробуйте перезагрузить страницу.");
			}
		}
	};
	request.open('POST', '/get_aer_start_par.py', true);
	request.send(null);
	return false;
});

$(document).ready(function getAerStopPar() {
	nocache = "&nocache=" + Math.random() * 1000000;
	var request = new XMLHttpRequest();
	request.onreadystatechange = function() {
		if (request.readyState === 4) {
			if (request.status === 200) {
				var x = request.responseText;
				x = parseFloat(x);
				document.getElementById('aer-stop').value = x;
			} else {
				alert("Что то пошло не так, попробуйте перезагрузить страницу.");
			}
		}
	};
	request.open('POST', '/get_aer_stop_par.py', true);
	request.send(null);
	return false;
});
	
$(document).ready(function isEnabled() {
	nocache = "&nocache=" + Math.random() * 1000000;
	var request = new XMLHttpRequest();
	request.onreadystatechange = function() {
		if (request.readyState === 4) {
			if (request.status === 200) {
				var x = request.responseText;
				x = parseInt(x);
				if (x === 1)
					$("#process p").toggle();
			} else {
				alert("Что то пошло не так, попробуйте перезагрузить страницу.");
			}
		}
	  };
	request.open('POST', '/is_enabled.py', true);
	request.send(null);
	return false;
});	
$("#processon").click(function processOn() {
	$.get("processon.py");
});

$("#processoff").click(function processOff() {
	$.get("processoff.py");
});

$("#camera-params").submit(function (Event) {
	Event.preventDefault()
	var temperature = $("#temperature").val();
	var humidity = $("#humidity").val();
		$.get("set_params.py", { "temperature" : temperature, "humidity" : humidity });
});


$("#aeration-params").submit(function (Event) {
	Event.preventDefault()
	var astart = $("#aer-start").val();
	var astop = $("#aer-stop").val();
		$.get("set_aer_params.py", { "astart" : astart, "astop" : astop });
});
