# Instruções para o Claude

Usuário: Everton, cria landing pages e gerencia tráfego no Google Ads. Fala português e usa tablet Android.
Responda sempre em português simples, com passos curtos.

## Fluxo de um projeto novo (landing page + Google Ads)
1. **Briefing:** perguntas de `briefings/MODELO.md` (poucas por vez). Salvar em `briefings/<cliente>.md`.
2. **Repositório:** o Everton cria `lp-<cliente>` vazio em github.com/new (o Claude não tem permissão
   para criar repositórios). Depois o Claude conecta (add_repo), clona e monta o projeto lá.
3. **Página:** partir de `modelos/landing-page/index.html`, com identidade própria do cliente.
   Publicar prévia (Artifact), ajustar, depois GitHub Pages ou hospedagem do cliente.
4. **Medição:** no Google Ads do cliente, criar as conversões "Clique no WhatsApp" e "Clique para
   ligar"; colocar ID e rótulos no bloco de conversões da página (já existe no modelo).
5. **Campanha:** preencher `modelos/google-ads/CAMPANHA-MODELO.md` em `campanha.md` do projeto e
   rodar `python3 ferramentas/checar_anuncios.py <arquivo>` para conferir os limites.
6. **Aprovação:** mostrar o resumo ao Everton. Só depois do "ok" criar a campanha **PAUSADA** pelo
   Adspirer; ativar só com novo "ok".
7. **Acompanhamento:** raio-X com 7 e 30 dias; salvar em `google-ads/` do projeto.
8. Atualizar `CLIENTES.md`.

## Adspirer (conector do Google Ads)
- Plano grátis: 15 ações/mês e só 1 conta de anúncios ativa por vez (hoje: Renovamente).
  Conta de cliente novo exige trocar a conta principal ou plano pago: avisar o Everton antes.
- Ações de leitura gastam pouco; conferir o saldo com get_usage_status antes de trabalhos grandes.

## Regras das páginas
- Um único objetivo por página (geralmente WhatsApp via `https://wa.me/55DDDNUMERO`).
- Rápida no celular: sem bibliotecas pesadas, imagens otimizadas.
- Deixar o espaço da tag do Google (gtag.js) e o evento de conversão no clique do WhatsApp.
- Nunca inventar depoimentos, números ou prêmios do cliente.

## Google Ads
- Títulos até 30 caracteres, descrições até 90. Sempre informar a contagem.
- Entregar também palavras-chave negativas.
- Se ele mandar print, indicar exatamente onde tocar, passo a passo.

## Conector do Google Ads (Adspirer)
- Antes de criar, ativar ou mudar orçamento de qualquer campanha, mostrar o resumo
  (campanha, palavras-chave, anúncios, orçamento diário) e só executar após o "ok" do Everton.
- Criar campanhas novas sempre **pausadas**; ativar só com aprovação.
- Nunca apagar campanhas; no máximo pausar.
- Clínica Renovamente: tudo no repositório `renovamente` (regras no CLAUDE.md de lá). NÃO alterar a conta do Google Ads sem autorização.
