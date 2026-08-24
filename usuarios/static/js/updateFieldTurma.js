document.addEventListener('DOMContentLoaded', function () {

    const radiosTipo = document.querySelectorAll('input[name="tipo_usuario"]');
    const wrapperTurma = document.getElementById('wrapper-turma');

    function atualizarCampos() {

        const selecionado = document.querySelector('input[name="tipo_usuario"]:checked');

        wrapperTurma.style.display = 'none';

        if (!selecionado) {
            return;
        }
        if (selecionado.value === 'aluno') {
            wrapperTurma.style.display = 'block';

        } else {
            wrapperTurma.style.display = 'none';
        }
    }

    radiosTipo.forEach(function(radio){ radio.addEventListener('change', atualizarCampos)});

    atualizarCampos();
});