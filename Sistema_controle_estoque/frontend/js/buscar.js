const botao = document.getElementById("botaoBuscar");
const inputCodigo = document.getElementById("codigo");
const resultado = document.getElementById("resultado");

function mostrarErro(mensagem) {
  botao.hidden = false;
  resultado.className = "erro";
  resultado.innerHTML = `<i class="fa-solid fa-circle-exclamation"></i> ${mensagem}`;
}

async function buscarProduto() {
  const codigo = inputCodigo.value.trim();

  if (codigo === "") {
    mostrarErro("Digite o código de barras");
    return;
  }

  botao.hidden = true;
  resultado.className = "consultando";
  resultado.textContent = "Consultando produto...";

  try {
    const resposta = await fetch("/buscar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ codigo_barras: codigo })
    });

    const dados = await resposta.json();
    console.log(dados);

    if (!resposta.ok) {
      mostrarErro(dados.mensagem || "Erro ao buscar produto.");
      return;
    }

    const valor = Number(dados.valor_prod).toFixed(2).replace(".", ",");
    const quantidade = Number(dados.quantidade).toLocaleString("pt-BR");

    botao.hidden = true;
    resultado.className = "sucesso";
    resultado.innerHTML = `
      <button type="button" id="fecharResultado" class="botao-fechar" aria-label="Fechar resultado" title="Fechar resultado">
        <i class="fa-solid fa-xmark"></i>
      </button>
      <div class="resultado-titulo">
        <i class="fa-solid fa-circle-check"></i> Produto encontrado
      </div>
      <div class="resultado-linha">
        <span class="rotulo"><i class="fa-solid fa-tag"></i> Nome</span>
        <span class="valor">${dados.nome_produto}</span>
      </div>
      <div class="resultado-linha">
        <span class="rotulo"><i class="fa-solid fa-coins"></i> Valor</span>
        <span class="valor">R$ ${valor}</span>
      </div>
      <div class="resultado-linha">
        <span class="rotulo"><i class="fa-solid fa-boxes-stacked"></i> Quantidade</span>
        <span class="valor">${quantidade}</span>
      </div>
      <button type="button" id="novaBusca" class="botao-nova-busca">
        <i class="fa-solid fa-magnifying-glass"></i> Nova busca
      </button>
    `;
  } catch (erro) {
    console.error("Erro ao buscar produto:", erro);
    mostrarErro("Erro ao conectar com o servidor.");
  }
}

botao.addEventListener("click", buscarProduto);

resultado.addEventListener("click", (e) => {
  if (e.target.closest("#novaBusca") || e.target.closest("#fecharResultado")) {
    resultado.replaceChildren();
    resultado.className = "";
    botao.hidden = false;
    inputCodigo.focus();
  }
});

inputCodigo.addEventListener("keydown", (e) => {
  if (e.key === "Enter") buscarProduto();
});
