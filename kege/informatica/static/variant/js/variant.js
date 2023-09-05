// JavaScript-код
//$(document).ready(function() {
//  $("button[id^='button-']").click(function() {
//    let elementId = $(this).attr("id").replace("button-", "");
//    $("#" + elementId).show();
//    $("[id^='my-element-']").not("#" + elementId).show();
//    $("button[id^='button-']").removeClass("task-current");
//    $(this).addClass("task-current");
//  });
//});

function showElement(elementId) {
  let element = document.getElementById(elementId);
  element.style.display = "block";

  let allElements = document.querySelectorAll("[id^='my-element']");
  for(let i = 0; i < allElements.length; i++) {
    if(allElements[i].id !== elementId) {
      allElements[i].style.display = "none";
    }
  }
}

$(document).ready(function() {
  $("button[id^='button-']").click(function() {
    let elementId = $(this).attr("id").replace("button-", "");
//    $("#" + elementId).show();
//    $("[id^='my-element']").not("#" + elementId).hide();
    $("button[id^='button-']").removeClass("task-current");
    $(this).addClass("task-current");
  });
});

$(document).ready(function() {
  var step = 400; // высота одного элемента
  var count = 13; // количество элементов, видимых в панели
  var nav = $('.navigation');
  var navHeight = nav.height();
  var maxTop = nav.find('ul').height() - navHeight;
  var current = 0;

  $('.arrow-up').click(function() {
    current -= step;

    if (current < 0) {
      current = 0;
    }

    nav.scrollTop(current);
  });

  $('.arrow-down').click(function() {
    current += step;

    if (current > maxTop) {
      current = maxTop;
    }

    nav.scrollTop(current);
  });
});