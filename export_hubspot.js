function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

var stop = false;
var linhasCSV = [];

while (!stop) {
  var tbody = document.querySelector("tbody");
  console.log('Nova busca')
  await sleep(3000)

  tbody.querySelectorAll('tr').forEach(row => {
    const colunas = Array.from(row.querySelectorAll('td')).map(cell => cell.textContent.trim());
    linhasCSV.push(colunas.join(';'));
    });

    var Button = document.querySelector('[aria-label="Próxima página"]');
    var statusButton = Button.getAttribute('aria-disabled');

    if (statusButton == 'true') {
      stop = true;

      var textToSave = linhasCSV.join('\n');

      var hiddenElement = document.createElement('a');

      hiddenElement.download = 'string.txt';
      var blob = new Blob([textToSave], {
          type: 'text/plain'
      });
      hiddenElement.href = window.URL.createObjectURL(blob);
      hiddenElement.click();
      var a = new Audio('https://s3.amazonaws.com/freecodecamp/drums/Chord_3.mp3');
      a.play();
    } else {
      Button.click()
    }
}

// [print(x[:-9].replace(' de Agosto de 2024', '/08/2024')) for x in var]

// https://s3.amazonaws.com/freecodecamp/drums/Chord_1.mp3

// https://s3.amazonaws.com/freecodecamp/drums/Chord_3.mp3

// https://s3.amazonaws.com/freecodecamp/drums/RP4_KICK_1.mp3
