function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
  
    element.style.display = 'none';
    document.body.appendChild(element);
  
    element.click();
    document.body.removeChild(element);
}

function toBR(numero) {
    let out = (numero / 100).toString().replace('.', ',') //.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'})
    return out
}

function GASTOS(nuJson) {
    let csvSting = ''
    nuJson.bill.line_items.forEach((e) => {
        csvSting += e.post_date + ';' + e.title + ';' + toBR(e.amount) + '\n'
    })

    download('text.txt', csvSting)
}

var header = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "Authorization": JSON.parse(sessionStorage.getItem('token__pf')).token_type + ' ' + JSON.parse(sessionStorage.getItem('token__pf')).access_token
    }
  }

async function logJSONData() {
    let url = JSON.parse(sessionStorage.getItem('discovery_endpoints__bills')).open
    const response = await fetch(url, header);
    const jsonData = await response.json();
    return jsonData
  }


GASTOS(await logJSONData())
