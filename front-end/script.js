const roleSelect = document.getElementById('select1');
const button = document.getElementById('subb');

console.log(button);

button.addEventListener('click', function() {
    console.log("1111");
    if (roleSelect.value === 'student') {
        window.location.href = 'index.html';
    }
});
// const input = document.getElementById("select");
// const inputValue = input.value;
// console.log(inputValue);
