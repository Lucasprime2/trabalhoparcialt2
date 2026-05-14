const API_URL = "http://127.0.0.1:8000/tarefas";

async function cadastrar() {
    const desc = document.getElementById('inputTarefa').value;
    await fetch(API_URL, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({descricao: desc})
    });
    document.getElementById('inputTarefa').value = "";
    listar();
}

async function listar() {
    const res = await fetch(API_URL);
    const dados = await res.json();
    const lista = document.getElementById('lista');
    lista.innerHTML = dados.map(t => `<li>${t.descricao}</li>`).join('');
}

listar();