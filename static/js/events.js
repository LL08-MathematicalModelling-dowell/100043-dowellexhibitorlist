$(document).ready(function(){
  var v = $("#msform").validate({
      rules: {
        email: {
          required: true,
          email: true,
          maxlength: 254,
        },
        venue: {
          required: true,
          maxlength: 254,
        },
        name: {
          required: true,
          maxlength: 254,
        },
        tagline:{
          required: true,
          maxlength: 500,
        },
        vanue_page_link:{
          required: true,
          maxlength: 2048,
        },
        organiser_website:{
          required: true,
          maxlength: 2048,
        },
        organiser_email:{
          required: true,
          maxlength: 254,
        },
        website:{
          required: true,
          maxlength: 2048,
        },
        type: {
          required: true,
          maxlength: 50,
        },
        category: {
          required: true,
          maxlength: 50,
        },
        business_category:{
          required: true,
          maxlength: 1000,
        },
        start_date:{
          required: true,
        },
        end_date:{
          required: true,
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
          maxlength: 256,
        },
        hashtag: {
          required: true,
          maxlength: 256,
        },
        mention: {
          required: true,
          maxlength: 256,
        },
        visitors_number:{
          required: true,
        },
        exhibitors_number:{
          required: true,
        },
        description: {
          required: true,
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
