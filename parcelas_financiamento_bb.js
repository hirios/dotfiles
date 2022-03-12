var linhas = document.querySelectorAll('.rich-table-row')
var total = 0

linhas.forEach(function(line) {
    var price = line.querySelector('td ~ td').innerText.split(' ')[1].replace('.', '').replace(',', '.')
    var price = Number(price)
    total += price
})

var formatoBR = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' })
console.log(formatoBR.format(total));
