// document.getElementById('submit-btn').addEventListener('click', function() {
//     const answer = document.getElementById('answer').value;
//     const feedback = document.getElementById('feedback');
//
//     // Предположим, что правильный ответ - 5
//     const correctAnswer1 = "-5";
//     const correctAnswer2 = "7";
//
//     if (answer === correctAnswer1 || answer === correctAnswer2) {
//         feedback.textContent = "Ответ правильный!";
//         feedback.style.color = "green";
//     } else {
//         feedback.textContent = "Ответ неверный. Попробуйте еще раз.";
//         feedback.style.color = "red";
//     }
// });
document.getElementById('submit-btn').addEventListener('click', function() {
    const answer = document.getElementById('answer').value;
    const feedback = document.getElementById('feedback');

    // Предположим, что правильный ответ -5 или 7
    const correctAnswer1 = "12";
    const correctAnswer2 = "-7";

    if (answer === correctAnswer1 || answer === correctAnswer2) {
        feedback.textContent = "Ответ правильный!";
        feedback.style.color = "green";
    } else {
        feedback.textContent = "Ответ неверный. Попробуйте еще раз.";
        feedback.style.color = "red";
    }
});

// Обработка клика на левую стрелку
document.getElementById('left-arrow').addEventListener('click', function() {
    const currentTask = 1; // Номер текущего задания, измените по необходимости
    if (currentTask === 1) {
        window.location.href = "menu.html"; // Возвращаемся в меню
    } else {
        // Переход к предыдущему заданию
        window.location.href = `task${currentTask - 1}.html`;
    }
});
