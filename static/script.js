let palavraSecreta = '';
let letrasErradas = [];
let letrasCertas = [];
let pontuacao = 0; // Variável para armazenar a pontuação
let tempo = 0; // Variável para armazenar o tempo
let cronometroInterval; // Intervalo para o cronômetro

// Função para adivinhar letra
function adivinharLetra() {
    const letra = document.getElementById('letra').value.toLowerCase();
    document.getElementById('letra').value = '';

    if (letrasErradas.includes(letra) || letrasCertas.includes(letra) || letra.length === 0) {
        alert('Você já tentou essa letra ou não digitou nada!');
        return;
    }

    if (palavraSecreta.includes(letra)) {
        letrasCertas.push(letra);
        pontuacao += 10; // Adiciona 10 pontos por letra correta
    } else {
        letrasErradas.push(letra);
        pontuacao -= 5; // Subtrai 5 pontos por letra errada
    }

    atualizarPalavra();
    atualizarMensagens();
    verificarFimDeJogo();
}

// Evento para o botão "Adivinhar"
document.getElementById('adivinhar').onclick = adivinharLetra;

// Evento para pressionar a tecla "Enter"
document.getElementById('letra').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        adivinharLetra();
    }
});

document.getElementById('reiniciar').onclick = function() {
    reiniciarJogo();
};

function reiniciarJogo() {
    letrasErradas = [];
    letrasCertas = [];
    pontuacao = 0; // Reinicia a pontuação
    tempo = 0; // Reinicia o tempo
    clearInterval(cronometroInterval); // Limpa o intervalo do cronômetro
    document.getElementById('cronometro').innerHTML = 'Tempo: 0s'; // Reseta o cronômetro

    // Obter o tema da URL
    const tema = window.location.pathname.split('/')[2]; // Pega o tema da URL

    fetch(`/nova_palavra/${tema}`)
        .then(response => response.json())
        .then(data => {
            palavraSecreta = data.palavra;
            atualizarPalavra();
            atualizarPontuacao(); // Atualiza a pontuação ao reiniciar
            document.getElementById('mensagem').innerHTML = '';
            document.getElementById('reiniciar').style.display = 'none';
            iniciarCronometro(); // Inicia o cronômetro
        });
}

function iniciarCronometro() {
    cronometroInterval = setInterval(() => {
        tempo++;
        document.getElementById('cronometro').innerHTML = 'Tempo: ' + tempo + 's';
    }, 1000); // Atualiza o tempo a cada segundo
}

function atualizarPalavra() {
    const palavraDisplay = palavraSecreta.split('').map(letra => (letrasCertas.includes(letra) ? letra : '_')).join(' ');
    document.getElementById('palavra').innerHTML = palavraDisplay;
}

function atualizarMensagens() {
    document.getElementById('mensagem').innerHTML = 'Letras Erradas: ' + letrasErradas.join(', ');
    atualizarPontuacao(); // Atualiza a pontuação sempre que uma letra é adivinhada
}

function atualizarPontuacao() {
    document.getElementById('pontuacao').innerHTML = 'Pontuação: ' + pontuacao;
}

const forcaGrafico = [
    `
    +---+
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    =========
    `,
    `
    +---+
    |   |
    |   O
    |  /|\\
    |  /
    |
    =========
    `,
    `
    +---+
    |   |
    |   O
    |  /|\\
    |
    |
    =========
    `,
    `
    +---+
    |   |
    |   O
    |   |
    |
    |
    =========
    `,
    `
    +---+
    |   |
    |   O
    |
    |
    |
    =========
    `,
    `
    +---+
    |   |
    |
    |
    |
    |
    =========
    `,
    `
    +---+
    |
    |
    |
    |
    |
    =========
    `
];

// Atualize a função verificarFimDeJogo para incluir o gráfico
function verificarFimDeJogo() {
    if (letrasErradas.length >= 6) {
        document.getElementById('mensagem').innerHTML = 'Você perdeu! A palavra era: ' + palavraSecreta;
        clearInterval(cronometroInterval); // Para o cronômetro
        document.getElementById('reiniciar').style.display = 'block';
    } else if (palavraSecreta.split('').every(letra => letrasCertas.includes(letra))) {
        document.getElementById('mensagem').innerHTML = 'Parabéns! Você acertou a palavra!';
        clearInterval(cronometroInterval); // Para o cronômetro
        document.getElementById('reiniciar').style.display = 'block';
    }

    // Atualiza o gráfico da forca
    document.getElementById('forca').innerHTML = forcaGrafico[6 - letrasErradas.length];
}

// Iniciar o jogo ao carregar a página
window.onload = reiniciarJogo;
