# Greemark — fábrica de projetos

Central do Everton para criar **landing pages** e o **tráfego no Google Ads** de cada cliente, tudo pelo Claude Code.

## Começar um projeto novo
Escreva no Claude Code (com este repositório aberto):

> **novo projeto: [nome do cliente], vende [o quê], em [cidade]**

O Claude conduz o resto:
1. Briefing (perguntas rápidas)
2. Você cria o repositório vazio `lp-nome-do-cliente` em github.com/new
3. Landing page com prévia por link
4. Medição de WhatsApp e ligações no Google Ads
5. Plano da campanha (palavras-chave, anúncios, negativas, orçamento) para aprovar
6. Campanha criada **pausada** e ativada só com o seu "ok"
7. Relatórios com 7 e 30 dias

## O que tem aqui
| Pasta | O que tem |
|---|---|
| `modelos/landing-page/` | Página base, já com tag do Google e conversões de WhatsApp/ligação |
| `modelos/google-ads/` | Modelo do plano de campanha |
| `ferramentas/` | Conferidor de tamanho de títulos e descrições |
| `briefings/` | Modelo de briefing |
| `paginas/greemark/` | Landing page da própria Greemark |
| `CLIENTES.md` | Todos os clientes, repositório e status |
