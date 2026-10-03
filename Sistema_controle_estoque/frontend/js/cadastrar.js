const botaoAbrirCadastro = document.getElementById("BotaoCadastrar");
const modalCadastro = document.getElementById("modalCadastro");
const formCadastro = document.getElementById("formCadastro");
const botaoFecharCadastro = document.getElementById("fecharCadastro");
const botaoCancelarCadastro = document.getElementById("cancelarCadastro");
const botaoEnviarCadastro = document.getElementById("enviarCadastro");
const mensagemCadastro = document.getElementById("mensagemCadastro");

function mostrarMensagemCadastro(texto, tipo = "") {
  mensagemCadastro.textContent = texto;
  mensagemCadastro.className = `mensagem-cadastro ${tipo}`.trim();
}

function fecharModalCadastro() {
  modalCadastro.close();
}

botaoAbrirCadastro.addEventListener("click", () => {
  mostrarMensagemCadastro("");
  modalCadastro.showModal();
  document.getElementById("codigoBarras").focus();
});

botaoFecharCadastro.addEventListener("click", fecharModalCadastro);
botaoCancelarCadastro.addEventListener("click", fecharModalCadastro);

modalCadastro.addEventListener("click", (evento) => {
  if (evento.target === modalCadastro) fecharModalCadastro();
});

formCadastro.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  mostrarMensagemCadastro("Cadastrando produto...");
  botaoEnviarCadastro.disabled = true;

  const formulario = new FormData(formCadastro);
  const dados = {
    codigo_barras: formulario.get("codigo_barras").trim(),
    nome_produto: formulario.get("nome_produto").trim(),
    valor_prod: Number(formulario.get("valor_prod")),
    setor_id: Number.parseInt(formulario.get("setor_id"), 10),
  };

  try {
    const resposta = await fetch("/cadastrarProduto", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados),
    });

    const resultado = await resposta.json().catch(() => ({}));

    if (!resposta.ok) {
      mostrarMensagemCadastro(
        resultado.mensagem || "Não foi possível cadastrar o produto.",
        "mensagem-cadastro-erro"
      );
      return;
    }

    formCadastro.reset();
    mostrarMensagemCadastro(
      resultado.mensagem || "Produto cadastrado com sucesso!",
      "mensagem-cadastro-sucesso"
    );
  } catch (erro) {
    console.error("Erro ao cadastrar produto:", erro);
    mostrarMensagemCadastro(
      "Não foi possível conectar ao servidor.",
      "mensagem-cadastro-erro"
    );
  } finally {
    botaoEnviarCadastro.disabled = false;
  }
});
