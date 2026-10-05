# Ajustes no site projetorenovamente.com.br

Este arquivo tem duas partes:
- **Parte A:** o Everton faz no Google Ads, antes de tudo (5 minutos).
- **Parte B:** copiar e colar no chat do Claude que edita o site.

---

## PARTE A — Everton, no Google Ads (fazer primeiro)

### A1. Criar a conversão de ligação
1. Google Ads → **Metas** → **Conversões** → **Resumo** → botão **+ Nova ação de conversão**.
2. Escolha **Site** e digite `projetorenovamente.com.br` → **Verificar**.
3. Desça até **"Adicionar uma ação de conversão manualmente"**.
4. Preencha:
   - Meta: **Contato**
   - Nome: **Clique para ligar**
   - Valor: **Não usar um valor**
   - Contagem: **Uma**
5. Salve. Na próxima tela, escolha **"Usar o Google Tag Manager"** ou **"Instalar a tag você mesmo"**.
6. Copie o código que aparece no formato **`AW-123456789/AbCdEfGhIj`** (ID/rótulo de conversão).
   Ele vai no lugar de `COLE-AQUI-O-ID-DA-LIGACAO` na Parte B.

### A2. Ligações direto do anúncio
1. **Anúncios e recursos** → **Recursos** → **+** → **Ligação**.
2. Coloque o telefone da clínica e marque para **medir as ligações como conversão**.

### A3. Tirar "Visualização de página" das conversões principais
1. **Metas** → **Conversões** → **Resumo** → clique em **Visualização de página**.
2. **Editar configurações** → em "Otimização da meta da ação", marque **Ação secundária** → **Salvar**.
   (Assim o Google para de otimizar por visitas e passa a otimizar por contatos.)

---

## PARTE B — Copie tudo abaixo e cole no Claude que edita o site

> Preciso de 3 ajustes no site da Clínica Renovamente. Não mude o visual nem os textos além do que está pedido aqui, e não quebre a medição que já existe no botão do WhatsApp.
>
> **1. Medir cliques no telefone como conversão do Google Ads**
> - Todo número de telefone visível no site deve ser um link `tel:` (ex.: `<a href="tel:+55DDDNUMERO">`). Se algum telefone estiver só como texto, transforme em link.
> - Se ainda não houver um botão "Ligar agora" visível no celular, crie um ao lado do botão do WhatsApp, no mesmo estilo.
> - Confirme que a tag do Google (gtag.js) já está no `<head>` de todas as páginas. Ela já existe por causa da conversão do WhatsApp: não duplique.
> - Antes de `</body>`, adicione:
>
> ```html
> <script>
> document.addEventListener('click', function (e) {
>   var link = e.target.closest('a[href^="tel:"]');
>   if (link && typeof gtag === 'function') {
>     gtag('event', 'conversion', { send_to: 'COLE-AQUI-O-ID-DA-LIGACAO' });
>   }
> });
> </script>
> ```
>
> **2. Texto sobre internação involuntária**
> Internação involuntária só pode ser feita em hospital ou unidade de saúde (Lei 13.840/2019). Procure no site qualquer frase que ofereça ou prometa "internação involuntária" ou "compulsória" e reescreva assim:
> "Para casos que precisam de internação involuntária, orientamos a família sobre o encaminhamento para atendimento hospitalar."
> Me mostre a lista do que mudou.
>
> **3. Verificação final**
> - Me diga em quais páginas a tag do Google está instalada.
> - Me diga se o clique no WhatsApp continua disparando a conversão (não altere esse código).
> - Liste todos os links `tel:` e `wa.me` do site.
