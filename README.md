# Greemark — central de projetos

Aqui fica tudo do trabalho do Everton: landing pages, briefings e o controle dos clientes.

## Como usar (pelo tablet ou celular)

Abra o Claude Code e converse direto. Não precisa passar pelo Gemini antes.

1. **Novo projeto:** diga "novo cliente: [nome], vende [o quê], em [cidade]".
   O Claude faz as perguntas do briefing, que fica salvo em `briefings/`.
2. **Página:** o Claude monta a landing page e manda um link de prévia.
3. **Ajustes:** peça mudanças em texto normal ("troca a cor do botão", "muda o telefone").
4. **No ar:** quando aprovar, o Claude publica e passa o endereço final.
5. **Google Ads:** peça "monta a campanha". Vêm títulos, descrições e palavras-chave prontos para colar.
   Travou em algum botão do Google Ads? Mande um print e peça "onde eu clico?".

## Pastas

| Pasta | O que tem |
|---|---|
| `paginas/` | Landing pages da própria Greemark |
| `modelos/landing-page/` | Modelo base reaproveitado em cada cliente novo |
| `briefings/` | Briefing de cada cliente (modelo em `briefings/MODELO.md`) |
| `CLIENTES.md` | Lista de clientes, repositório e status de cada um |

Cada cliente ganha um **repositório próprio** (`lp-nome-do-cliente`), para o controle ficar separado.
