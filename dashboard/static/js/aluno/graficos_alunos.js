fetch("/dashboard/api/charts/numero-de-submissoes/")
    .then(response => response.json())
    .then(dados => {
    const ctx = document.getElementById('numero-submissoes');
    new Chart(ctx,{
        type:'doughnut',
        data:{
            labels:dados.labels,
            datasets:[{
                label:"Submissões",
                data:dados.data
            }]

        },
        options:{
            responsive:true,
            maintainAspectRatio:false
        }

    })
});