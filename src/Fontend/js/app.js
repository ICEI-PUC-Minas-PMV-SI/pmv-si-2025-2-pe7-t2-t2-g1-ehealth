document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("formSaude");
  const feedbackArea = document.getElementById("feedbackArea");
  const feedbackIcon = document.getElementById("feedbackIcon");
  const feedbackHeader = document.getElementById("feedbackHeader");
  const feedbackMsg = document.getElementById("feedbackMsg");

  if (!form) return;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);

    const anoNascimento = Number(formData.get("anoNascimento"));
    const horasEstudo = Number(formData.get("horasEstudo"));
    const habitosAlimentares = Number(formData.get("habitosAlimentares"));
    const pressaoAcademica = Number(formData.get("pressaoAcademica"));
    const satisfacaoEstudos = Number(formData.get("satisfacaoEstudos"));
    const grauEstudo = Number(formData.get("grauEstudo"));
    const pensamentosSuicidas = Number(formData.get("pensamentosSuicidas"));
    const estresseFinanceiro = Number(formData.get("estresseFinanceiro"));

    const anoAtual = new Date().getFullYear();
    const age = anoAtual - anoNascimento;

    const payload = {
      age: age,
      academic_pressure: pressaoAcademica,
      study_satisfaction: satisfacaoEstudos,
      dietary_habits: habitosAlimentares,
      degree: grauEstudo,
      suicidal_thoughts: pensamentosSuicidas,
      workstudy_hours: horasEstudo,
      financial_stress: estresseFinanceiro
    };

    console.log("Payload enviado para API:", payload);

    try {
      const response = await fetch("https://api.dpy.me", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });

      let result = null;
      try {
        result = await response.json();
      } catch (e) {
        console.error("Erro ao analisar a resposta JSON:", e);
      }

      mostrarFeedback(response.ok, result);
    } catch (error) {
      console.error("Erro ao enviar dados:", error);
      mostrarFeedback(false, { error: "Erro de conexão com o servidor." });
    }
  });
  function mostrarFeedback(sucesso, result) {
    if (!feedbackArea || !feedbackIcon || !feedbackHeader || !feedbackMsg) return;

    feedbackArea.classList.remove("d-none");

    const depression = result?.depression;

    const depressionResult = depression ? 'Foram identificados possíveis sinais de depressão*' : 'O resultado indica ausência de sinais de depressão*';

    if (sucesso) {
        if (depression) {
          feedbackArea.classList.add('alert-secondary');
          feedbackIcon.className = "bi bi-exclamation-circle feedback-icon";
          feedbackMsg.textContent = '*Considerando uma margem de erro de 15%. Recomendamos que você procure um profissional qualificado para uma avaliação adequada e acompanhamento, caso necessário.';
        } else {
          feedbackArea.classList.add('alert-primary');
          feedbackIcon.className = "bi bi-exclamation-circle feedback-icon";
          feedbackMsg.textContent = '*Considerando uma margem de erro de 15%. Lembre-se: esta ferramenta não substitui a avaliação de um profissional de qualificado.';
        }
        feedbackHeader.textContent =
        (result && (result.message || result.msg)) || `${depressionResult}`;
    
    } else {
      feedbackArea.classList.add('alert-danger');
      feedbackIcon.className = "bi bi-dash-circle feedback-icon";
      feedbackHeader.textContent = "Erro!";
      feedbackMsg.textContent =
        (result && (result.error || result.message || result.msg)) ||
        "Ocorreu um erro ao enviar os dados. Tente novamente mais tarde.";
    }

    feedbackArea.scrollIntoView({ behavior: "smooth", block: "center" });
  }
});
