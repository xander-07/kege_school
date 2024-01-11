// Показ задания
function showElement(elementId, fileId, answerId, answerTableId, type_task) {
    // Скрываем все элементы с аналогичными идентификаторами
    let allElements = document.querySelectorAll("[id^='my-element']");
    let allFiles = document.querySelectorAll("[id^='my-file']");
    let allAnswerBlocks = document.querySelectorAll("[id^='my-answer-block']");
    let allAnswerTableBlocks = document.querySelectorAll("[id^='my-table-answer-block']");

    for (let i = 0; i < allElements.length; i++) {
        allElements[i].style.display = "none";
        allFiles[i].style.display = "none";
        allAnswerBlocks[i].style.display = "none";
        if (allAnswerTableBlocks[i]) {
            allAnswerTableBlocks[i].style.display = "none";
        }
    }

    // Отображаем элементы, если type_task равен 17
    if (type_task === '17' || type_task === '18' || type_task === '20' || type_task === '26' || type_task === '27' || type_task === '25') {
        let element = document.getElementById(elementId);
        let file = document.getElementById(fileId);
        let answerBlock = document.getElementById(answerId);
        let answerTableBlock = document.getElementById(answerTableId);

        if (element && file && answerBlock) {
            element.style.display = "block";
            file.style.display = 'flex';
            answerBlock.style.display = 'none';
        }

        if (answerTableBlock) {
            answerTableBlock.style.display = 'block';

        }
    } else {
        // Отображаем элементы, если type_task не равен 17
        let element = document.getElementById(elementId);
        let file = document.getElementById(fileId);
        let answerBlock = document.getElementById(answerId);
        if (element) {
            element.style.display = "block";
            file.style.display = 'flex';
            answerBlock.style.display = 'flex';
        }
    }
}

$(document).ready(function () {
    $("button[id^='button-']").click(function () {
        let elementId = $(this).attr("id").replace("button-", "");
        $("button[id^='button-']").removeClass("task-current");
        $(this).addClass("task-current");
    });
});

// Слайдер прокрутки заданий варианта
$(document).ready(function () {
    var step = 390; // высота одного элемента
    var count = 13; // количество элементов, видимых в панели
    var nav = $('.navigation');
    var navHeight = nav.height() - 30;
    var maxTop = nav.find('ul').height() - navHeight;
    var current = 0;

    $('.arrow-up').click(function () {
        current -= step;

        if (current < 0) {
            current = 0;
        }

        nav.scrollTop(current);
    });

    $('.arrow-down').click(function () {
        current += step;

        if (current > maxTop) {
            current = maxTop;
        }

        nav.scrollTop(current);
    });
});

// Функция сохранения ответов
function saveAnswer(button) {
    let answerText = document.getElementById('answer-' + button.getAttribute('data-counter')).value;
    let counter = button.getAttribute('data-counter');
    let idTask = button.getAttribute('data-id-task');
    let idKim = button.getAttribute('data-id_kim');
    let Kim = button.getAttribute('data-kim');
    let type = button.getAttribute('data-type');
    let csrfToken = button.getAttribute('data-csrf');
    let counterAnswer = document.getElementById('counter_answer').innerText;


    let btn_answer = document.getElementById('button-' + counter);

    // var currentValue = parseInt(counterAnswer.value);

    // Выполните AJAX-запрос для сохранения ответа
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/inf/save-answer/', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Обработайте успешное выполнение при необходимости
            console.log('Ответ успешно сохранен');
            var newValue = Number(counterAnswer) + 1;
            document.getElementById('counter_answer').innerText = newValue;
            btn_answer.classList.add('task-fill');
            btn_answer.classList.remove('task-empty');

        } else {
            // Обработайте ошибку при необходимости
            console.error('Ошибка сохранения ответа');
        }
    };
    let data = 'answer_text=' + encodeURIComponent(answerText) + '&counter=' + encodeURIComponent(counter) + '&id_kim=' + encodeURIComponent(idKim) + '&kim=' + encodeURIComponent(Kim) + '&id_question=' + encodeURIComponent(idTask) + '&type=' + encodeURIComponent(type);
    xhr.send(data);
}


function saveAnswer_25(button) {
    let answer_1 = document.getElementById('answer-table-1-' + button.getAttribute('data-counter')).value;
    let answer_2 = document.getElementById('answer-table-2-' + button.getAttribute('data-counter')).value;
    let answer_3 = document.getElementById('answer-table-3-' + button.getAttribute('data-counter')).value;
    let answer_4 = document.getElementById('answer-table-4-' + button.getAttribute('data-counter')).value;
    let answer_5 = document.getElementById('answer-table-5-' + button.getAttribute('data-counter')).value;
    let answer_6 = document.getElementById('answer-table-6-' + button.getAttribute('data-counter')).value;
    let answer_7 = document.getElementById('answer-table-7-' + button.getAttribute('data-counter')).value;
    let answer_8 = document.getElementById('answer-table-8-' + button.getAttribute('data-counter')).value;
    let answer_9 = document.getElementById('answer-table-9-' + button.getAttribute('data-counter')).value;
    let answer_10 = document.getElementById('answer-table-10-' + button.getAttribute('data-counter')).value;
    let answer_11 = document.getElementById('answer-table-11-' + button.getAttribute('data-counter')).value;
    let answer_12 = document.getElementById('answer-table-12-' + button.getAttribute('data-counter')).value;
    let answer_13 = document.getElementById('answer-table-13-' + button.getAttribute('data-counter')).value;
    let answer_14 = document.getElementById('answer-table-14-' + button.getAttribute('data-counter')).value;
    let answer_15 = document.getElementById('answer-table-15-' + button.getAttribute('data-counter')).value;
    let answer_16 = document.getElementById('answer-table-16-' + button.getAttribute('data-counter')).value;
    let answer_17 = document.getElementById('answer-table-17-' + button.getAttribute('data-counter')).value;
    let answer_18 = document.getElementById('answer-table-18-' + button.getAttribute('data-counter')).value;
    let answer_19 = document.getElementById('answer-table-19-' + button.getAttribute('data-counter')).value;
    let answer_20 = document.getElementById('answer-table-20-' + button.getAttribute('data-counter')).value;
    let answer_21 = document.getElementById('answer-table-21-' + button.getAttribute('data-counter')).value;
    let answer_22 = document.getElementById('answer-table-22-' + button.getAttribute('data-counter')).value;
    let answer_23 = document.getElementById('answer-table-23-' + button.getAttribute('data-counter')).value;
    let answer_24 = document.getElementById('answer-table-24-' + button.getAttribute('data-counter')).value;

    let answerText = [answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10, answer_11, answer_12, answer_13, answer_14, answer_15, answer_16, answer_17, answer_18, answer_19, answer_20, answer_21, answer_22, answer_23, answer_24];

    let counter = button.getAttribute('data-counter');
    let idTask = button.getAttribute('data-id-task');
    let idKim = button.getAttribute('data-id_kim');
    let Kim = button.getAttribute('data-kim');
    let type = button.getAttribute('data-type');
    let csrfToken = button.getAttribute('data-csrf');
    let counterAnswer = document.getElementById('counter_answer').innerText;

    console.log(answerText);

    let btn_answer = document.getElementById('button-' + counter);

    // var currentValue = parseInt(counterAnswer.value);

    // Выполните AJAX-запрос для сохранения ответа
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/inf/save-answer/', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Обработайте успешное выполнение при необходимости
            console.log('Ответ успешно сохранен');
            var newValue = Number(counterAnswer) + 1;
            document.getElementById('counter_answer').innerText = newValue;
            btn_answer.classList.add('task-fill');
            btn_answer.classList.remove('task-empty');

        } else {
            // Обработайте ошибку при необходимости
            console.error('Ошибка сохранения ответа');
        }
    };
    let data = 'answer_text=' + encodeURIComponent(answerText) + '&counter=' + encodeURIComponent(counter) + '&id_kim=' + encodeURIComponent(idKim) + '&kim=' + encodeURIComponent(Kim) + '&id_question=' + encodeURIComponent(idTask) + '&type=' + encodeURIComponent(type);
    xhr.send(data);
}

function saveAnswer_table(button) {
    let answer_1 = document.getElementById('answer-table-1-' + button.getAttribute('data-counter')).value;
    let answer_2 = document.getElementById('answer-table-2-' + button.getAttribute('data-counter')).value;
    let answer_3 = document.getElementById('answer-table-3-' + button.getAttribute('data-counter'))?.value || "";
    let answer_4 = document.getElementById('answer-table-4-' + button.getAttribute('data-counter'))?.value || "";
    let answer_5 = document.getElementById('answer-table-5-' + button.getAttribute('data-counter'))?.value || "";
    let answer_6 = document.getElementById('answer-table-6-' + button.getAttribute('data-counter'))?.value || "";
    let answer_7 = document.getElementById('answer-table-7-' + button.getAttribute('data-counter'))?.value || "";
    let answer_8 = document.getElementById('answer-table-8-' + button.getAttribute('data-counter'))?.value || "";
    let answer_9 = document.getElementById('answer-table-9-' + button.getAttribute('data-counter'))?.value || "";
    let answer_10 = document.getElementById('answer-table-10-' + button.getAttribute('data-counter'))?.value || "";
    let answer_11 = document.getElementById('answer-table-11-' + button.getAttribute('data-counter'))?.value || "";
    let answer_12 = document.getElementById('answer-table-12-' + button.getAttribute('data-counter'))?.value || "";
    let answer_13 = document.getElementById('answer-table-13-' + button.getAttribute('data-counter'))?.value || "";
    let answer_14 = document.getElementById('answer-table-14-' + button.getAttribute('data-counter'))?.value || "";
    let answer_15 = document.getElementById('answer-table-15-' + button.getAttribute('data-counter'))?.value || "";
    let answer_16 = document.getElementById('answer-table-16-' + button.getAttribute('data-counter'))?.value || "";
    let answer_17 = document.getElementById('answer-table-17-' + button.getAttribute('data-counter'))?.value || "";
    let answer_18 = document.getElementById('answer-table-18-' + button.getAttribute('data-counter'))?.value || "";
    let answer_19 = document.getElementById('answer-table-19-' + button.getAttribute('data-counter'))?.value || "";
    let answer_20 = document.getElementById('answer-table-20-' + button.getAttribute('data-counter'))?.value || "";

    let answerText = [answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10, answer_11, answer_12, answer_13, answer_14, answer_15, answer_16, answer_17, answer_18, answer_19, answer_20];

    let counter = button.getAttribute('data-counter');
    let idTask = button.getAttribute('data-id-task');
    let idKim = button.getAttribute('data-id_kim');
    let Kim = button.getAttribute('data-kim');
    let type = button.getAttribute('data-type');
    let csrfToken = button.getAttribute('data-csrf');
    let counterAnswer = document.getElementById('counter_answer').innerText;

    console.log(answerText);

    let btn_answer = document.getElementById('button-' + counter);

    // var currentValue = parseInt(counterAnswer.value);

    // Выполните AJAX-запрос для сохранения ответа
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/inf/save-answer/', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Обработайте успешное выполнение при необходимости
            console.log('Ответ успешно сохранен');
            var newValue = Number(counterAnswer) + 1;
            document.getElementById('counter_answer').innerText = newValue;
            btn_answer.classList.add('task-fill');
            btn_answer.classList.remove('task-empty');

        } else {
            // Обработайте ошибку при необходимости
            console.error('Ошибка сохранения ответа');
        }
    };
    let data = 'answer_text=' + encodeURIComponent(answerText) + '&counter=' + encodeURIComponent(counter) + '&id_kim=' + encodeURIComponent(idKim) + '&kim=' + encodeURIComponent(Kim) + '&id_question=' + encodeURIComponent(idTask) + '&type=' + encodeURIComponent(type);
    xhr.send(data);
}










