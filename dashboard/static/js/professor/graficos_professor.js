fetch("/dashboard/api/charts/aluno-por-turma/")
    .then(response => response.json())
    .then(dados => {
    const ctx = document.getElementById('aluno-por-turma');
    new Chart(ctx,{
        type:'doughnut',
        data:{
            labels:dados.labels,
            datasets:[{
                label:"Alunos por turma",
                data:dados.data
            }]

        },
        options:{
            reponsive:true,
            maintainAspectRatio:false
        }

    })
});