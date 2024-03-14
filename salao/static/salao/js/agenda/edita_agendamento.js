
$(document).ready(function() {
    $('.editar-agendamento').click(function(event) {
        event.preventDefault(); // Impedir o comportamento padrão do link

        var agendamentoId = $(this).data('agendamento-id');

        $.ajax({
            url: '/edita_agendamento/' + agendamentoId + '/', // URL da view para obter o agendamento
            method: 'GET',
            success: function(data) {
                // Manipular os dados recebidos para preencher o formulário de edição
                // Aqui você pode usar os dados para preencher o formulário
                console.log(data);
                // Abra o formulário de edição com os dados recuperados
            },
            error: function(error) {
                console.log('Erro ao obter os dados do agendamento:', error);
            }
        });
    });
});