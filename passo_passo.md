# Criar HTML Personalizada

Acessar o Tag Manager

Clicar em "Tags" no menu à esquerda 

Clicar em "Nova", para gerar uma nova Tag

Clicar em "Configuração da Tag"

No menu à direita, ir até o final e selecionar "HTML Personalizada"

Copie o código abaixo 


```
<script>
    var target = document.querySelector('.wpcf7-response-output.wpcf7-display-none')
    var botao_enviar = document.querySelector('input[value="Enviar Mensagem"]')
    
    var email;
    var phone;

    if(botao_enviar) {
        botao_enviar.addEventListener('click', function() {
            email = document.querySelector('input[name="your-email"]').value
            phone = document.querySelector('input[name="fone"]').value
        })
    }

    if (target) {
        var observer = new MutationObserver(function (mutations) {
            mutations.forEach(function (mutation) {
                dataLayer.push({'event' : 'form_submit',});                
                console.log('Form enviado')
            });
        });

        var config = {childList: true};
        observer.observe(target, config);
    }
</script>
```

Colocar o código dentro do quadrado de HTML

Embaixo, clique em "acionamento" 

Clique no botão com sinal de "+" no canto superior direito

Clique em "Configuração do acionador"

Selecione no menu à direita a opção "DOM Pronto"

Marque a opção "Todos os eventos DOM Prontos"

Salve tudo 


# Editar Tag de formulaŕio

Selecionar a tag "Acompanhamento de conversões do Google Ads"

Clicar em configuração da tag

Marcar a caixinha "Fornecer os dados para envio"

Clicar em "Select user-provided...", depois ir em "Nova variável"

Cicar em email, depois ir em "Nova variável"

Clicar em "Configuração da variável"

Selecionar "Javascript personalizado"

Copiar o código abaixo 

```
function() {
    return JSON.parse(localStorage.getItem('en_data'))['email']
}
```

Cole o código dentro do retângulo 

Salve

Faça o mesmo precesso para o "Telefone" e cole o seguinte código 

```
function() {
    return JSON.parse(localStorage.getItem('en_data'))['number']
}
```

Salve 

Vamos agora adicionar um novo acionador

Remova o que já existe clicando no sinal de menos "-"

Embaixo, clique em "acionamento" 

Clique no botão com sinal de "+" no canto superior direito

Clique em "Configuração do acionador"

Selecione no menu à direita a opção "Evento personalizado"

No campo "Nome do evento", digite "form_submit"

Marque a opção "Todos eventos personalizados"

Salve tudo 







