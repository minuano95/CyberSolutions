
$(document).ready(function() {
    const now = new Date();
    // Define o fuso horário para 'America/Sao_Paulo' (Brasil/São Paulo)
    const options = { timeZone: 'America/Sao_Paulo' };
    const dataHoraAtual = now.toLocaleString('pt-BR', options);
    // Define a data e hora atual nos campos de hora de início e término
    $('#hora_inicio').val(dataHoraAtual);
    $('#hora_termino').val(dataHoraAtual);
    
});

