// --- Todo list ---
const form = document.getElementById('todo-form');
const input = document.getElementById('todo-input');
const list = document.getElementById('todo-list');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text) return;
    addTodo(text);
    input.value = '';
});

function addTodo(text) {
    const li = document.createElement('li');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', () => {
        li.classList.toggle('done', checkbox.checked);
    });

    const span = document.createElement('span');
    span.textContent = text;

    const btn = document.createElement('button');
    btn.textContent = '×';
    btn.addEventListener('click', () => li.remove());

    li.append(checkbox, span, btn);
    list.appendChild(li);
}
