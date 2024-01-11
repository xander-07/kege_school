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