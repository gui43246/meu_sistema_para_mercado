const usuario = document.getElementById("drt");
const senha = document.getElementById("senha");
const botao = document.querySelector("button");

botao.addEventListener("click", async (event) => {
  event.preventDefault();
  await Fazer_login();
});

async function Fazer_login() {
  try {
    const response = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        drt: usuario.value,
        senha_digitada: senha.value
      })
    });

    const dados = await response.json();

    if (dados.sucesso === true) {
      window.location.href = "pages/index.html";
    } else {
      alert(dados.mensagem); 
    }
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro ao conectar com o servidor.");
  }
}
