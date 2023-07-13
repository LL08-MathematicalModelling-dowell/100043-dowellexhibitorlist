$(document).ready(function(){
  var v = $("#msform").validate({
      rules: {
        email: {
          hidden: true,
          email: true,
          maxlength: 256,
        },
        name: {
          required: true,
          // text: true,
          maxlength: 256,
        },
        brand_name: {
          required: true,
          // text: true,
          maxlength: 256,
        },
        name_incharge: {
          required: true,
          // text: true,
          maxlength: 256,
        },
        designation_incharge: {
          required: true,
          // text: true,
          maxlength: 500,
        },
        exhibitor_page_link: {
          required: false,
          // url: true,
          maxlength: 2048,
        },
        exhibitor_website: {
          required: true,
          // url: true,
          maxlength: 2048,
        },
        exhibitor_email: {
          required: true,
          // email: true,
          maxlength: 256,
        },
        exhibitor_both_number: {
          required: true,
          // text: true,
          maxlength: 500,
        },
        exhibitor_city: {
          required: true,
          // text: true,
          maxlength: 500,
        },
        exhibitor_country: {
          required: true,
          // text: true,
          maxlength: 500,
        },
        exhibitor_address: {
          required: true,
          // text: true,
          maxlength: 500,
        },
        type: {
          required: true,
          // text: true,
          maxlength: 50,
        },
        exhibitor_product: {
          required: true,
          // text: true,
          maxlength: 500,
        },
        linkedin: {
          url: true,
          maxlength: 2048,
        },
        twitter: {
          url: true,
          maxlength: 2048,
        },
        facebook: {
          url: true,
          maxlength: 2048,
        },
        instagram: {
          url: true,
          maxlength: 2048,
        },
        youtube: {
          url: true,
          maxlength: 2048,
        },
        tiktok: {
          url: true,
          maxlength: 2048,
        },
        hashtag: {
          required: true,
          // text: true,
          maxlength: 256,
        },
        hashtag: {
          required: true,
          // text: true,
          maxlength: 256,
        },
        mention: {
          required: true,
          // text: true,
          maxlength: 256,
        },
        description: {
          required: true,
          // text: true,
          maxlength: 256,
        },
        logo:{
          required: true,
        }

      },
      errorElement: "span",
      errorClass: "help-inline",
    });

var current_fs, next_fs, previous_fs; //fieldsets
var opacity;

$(".next").click(function(){
  if (v.form()) {

  current_fs = $(this).parent();
  next_fs = $(this).parent().next();

  //Add Class Active
  $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
  // $("#three").addClass("active");

  //show the next fieldset
  next_fs.show();
  //hide the current fieldset with style
  current_fs.animate({opacity: 0}, {
  step: function(now) {
  // for making fielset appear animation
  opacity = 1 - now;

  current_fs.css({
  'display': 'none',
  'position': 'relative'
  });
  next_fs.css({'opacity': opacity});
  },
  duration: 600
  });
}
  });

$(".previous").click(function(){

current_fs = $(this).parent();
previous_fs = $(this).parent().prev();

//Remove class active
$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

//show the previous fieldset
previous_fs.show();

//hide the current fieldset with style
current_fs.animate({opacity: 0}, {
step: function(now) {
// for making fielset appear animation
opacity = 1 - now;

current_fs.css({
'display': 'none',
'position': 'relative'
});
previous_fs.css({'opacity': opacity});
},
duration: 600
});
});

$('.radio-group .radio').click(function(){
$(this).parent().find('.radio').removeClass('selected');
$(this).addClass('selected');
});

$(".submit").click(function(){
return false;
})
});
function checkValue() {
    	var email = document.getElementById("email");
        if(email == null ) {
          var att = document.createAttribute("required");
          email.setAttributeNode(att);
        }
    }
