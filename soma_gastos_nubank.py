
function GASTOS(nuJson) {
    nuJson.bill.line_items.forEach((e) => {
        console.log(e.post_date + '|' + e.title + '|' + e.amount.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'}))
    })
}

GASTOS()


