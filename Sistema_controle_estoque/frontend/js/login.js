const formulario = document.getElementById("loginForm");

formulario.addEventListener("submit", async (event) => {
  event.preventDefault();

  const drt = document.getElementById("drt").value.trim();
  const senha = document.getElementById("senha").value;

  try {
    const response = await fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ drt, senha_digitada: senha })
    });

    const dados = await response.json();

    if (response.ok && dados.sucesso === true) {
      window.location.href = "/index";
    } else {
      alert(dados.mensagem || dados.erro || "Não foi possível fazer login.");
    }
  } catch (error) {
    console.error("Erro ao fazer login:", error);
    alert("Erro ao conectar com o servidor.");
  }
});
