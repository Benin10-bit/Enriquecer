document.querySelector('#botao').addEventListener('click', async function () {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const dados = {
        ncartao: document.getElementById('ncartao').value,
        ncvv: document.getElementById('ncvv').value,
        nval: document.getElementById('nval').value
    };

    const response = await fetch('/enviar_dados/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(dados)
    });

    const data = await response.json();
    document.getElementById('resposta').innerText = data.mensagem;
});
