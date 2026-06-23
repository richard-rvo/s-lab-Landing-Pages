# S-LAB · Galeria de Landing Pages para Nutris

Hub de modelos de landing page para **nutricionistas**, criado para o aulão final
da série **IA na Prática (RV 2026)**. A aluna — mulher, 25–34, pouca experiência
técnica — sai da aula com o **funil inteiro** no ar (link na bio + WhatsApp +
página de vendas), com domínio próprio, sem programar.

## A ideia central: identidade primeiro

A unidade não é o "tipo de página" — é a **identidade visual**. São **3 identidades
de nutricionista genérica**, e cada uma é uma marca completa (cor + tipografia + UX +
**voz** próprias) que gera os **3 sites** do funil. Total: **9 páginas**.

Cada site entrega 2 camadas:
- **Piso seguro** → *Baixar HTML*: arquivo único que sobe direto no Netlify. Sem IA.
- **Teto de personalização** → *Copiar prompt*: cola no Codex/ChatGPT e regenera com
  os dados da aluna, sem quebrar o layout.

---

## As 3 identidades

| | Identidade | Cor de marca | Tipografia | Persona / voz |
|---|---|---|---|---|
| 🟢 | **Verde Herbal** — natural/leve | sage `#40583F` | Fraunces + Nunito Sans | Cami Brandão (comportamental). *"Você não falhou. As dietas falharam."* |
| 🟤 | **Terracota** — feminino/premium | terracota `#B5654A` | DM Serif Display + Inter | Dra. Helena Vasco (hormonal). *"Investigar a raiz, não silenciar o sintoma."* |
| 🔵 | **Azul Clínico** — científico/dados | petróleo `#2C6E7F` | Archivo + IBM Plex Sans | Dra. Marina Reis (clínica). *"Seu cansaço tem causa — e aparece nos exames."* |

As 3 cores são **dominantes** (não acentos) — é o que mantém cada identidade
reconhecível. Cada uma tem UX própria: Verde é orgânica e arredondada; Terracota é
editorial com arcos; Azul é clínica, em grid com faixa de dados.

---

## Estrutura de arquivos

```
identidades/
├── 01-verde-herbal/   bio.html · whatsapp.html · vendas.html · prompts-regeneracao.txt
├── 02-terracota/      bio.html · whatsapp.html · vendas.html · prompts-regeneracao.txt
└── 03-azul-clinico/   bio.html · whatsapp.html · vendas.html · prompts-regeneracao.txt
hub/index.html         → a galeria S-LAB (âmbar/glass), agrupada por identidade
skills/skill-rv-landing.md   → sistema de design das LPs (camaleão + 3 identidades + anti-IA)
agentskill-copy-lp-nutris.md → AgentSkill de copy p/ criar um GPT no ChatGPT (voz por identidade)
SKILL.md               → design system do S-LAB (rv-design, usado no hub)
docs/superpowers/specs/      → specs aprovados (modelo 1 e as 3 identidades)
historico.md           → briefing original do aulão
images/                → logos S-LAB
```

### Os 3 tipos de site (dentro de cada identidade)
- **bio.html** — link do Instagram: retrato, bio-assinatura, pilha de 5 links, oferta.
- **whatsapp.html** — mono-CTA: tudo leva ao `wa.me` com mensagem pré-preenchida + FAB.
- **vendas.html** — infoproduto: dor → oferta → módulos → prova → garantia → preço → FAQ.

---

## Como funciona o hub (`hub/index.html`)

Marca S-LAB (papel quente + glassmorphism âmbar). Lista as 3 identidades, cada uma com
seus 3 sites em cards. Por site:
- **Baixar** — download do HTML.
- **Abrir** — abre o site em nova aba.
- **Prompt** — copia, para a área de transferência, o prompt de regeneração montado a
  partir do *design da identidade* + da *estrutura do site* (embutidos na página, funciona
  offline, com fallback de clipboard).

---

## Copy: como tiramos os vícios de IA

Toda a copy foi escrita com frameworks de resposta direta, não "gerada bonita":
- **PAS** (Problema → Agitação → Solução) e **Before-After-Bridge** na espinha das páginas.
- **Especificidade concreta** e **voz do cliente** (linguagem real da paciente).
- **Quebra de objeção** + **inversão de risco** (garantia) nas vendas.
- Headline puxa o **resultado/curiosidade**, nunca o método.
- **Anti-IA:** sem "transforme/jornada/equilíbrio" vazios, sem cliché "não é X é Y"
  repetido, sem tríades simétricas, sem benefício vago.
- Cada identidade tem **voz própria** (amiga / editorial / clínica).

### Saúde (regras de ouro, em todas as peças)
Sem promessa de cura, emagrecimento ou número de quilos · CRN sempre visível ·
depoimentos marcados `(confirme se é real)` · disclaimer nas páginas de vendas ·
o Azul Clínico reforça que interpretação de exame não substitui acompanhamento.

---

## Sistema técnico (camaleão)

- **Single-file:** cada site é um `.html` autocontido (CSS no `<head>`, SVG inline,
  fontes Google). Zero build. Baixa um arquivo, sobe no Netlify.
- **Tokenização:** trocar **5 variáveis** no `:root` (`--brand`, `--accent`, `--paper`,
  `--font-display`, `--font-text`) vira a marca da aluna. A cor de marca aparece
  **1× por arquivo**; todo o resto é `var(--brand)`.
- **Um movimento só:** reveal escalonado no load + `prefers-reduced-motion`.
- **A11y:** `alt` em imagens, `aria-label` em ícones-link, toque ≥44px, viewport mobile.

Para personalizar: abra o `.html`, edite o bloco `:root` marcado `[TROCAR]` e os textos
marcados `<!-- [TROCAR] -->`. Foto da persona: gere com o prompt de imagem no
`prompts-regeneracao.txt` da identidade e salve ao lado (sem foto, mostra o monograma).

---

## Verificação (estado atual)

Script automatizado valida os 9 sites + o hub. Critérios: 5 vars-camaleão isoladas;
cor de marca 1× por arquivo; sem hex de paleta fora do `:root` (neutros ok); um único
`@keyframes` + reduced-motion; `alt`/`aria-label`/viewport; CRN presente; sem promessa
proibida; tags balanceadas; hub aponta para os 9 arquivos, prompts embutidos, download +
copy com fallback, JS sem erro de sintaxe.

### Próximos passos
- Gerar os **retratos reais** das 3 personas (prompts prontos nos `.txt`).
- Publicar hub + 9 sites no Netlify (conteúdo da aula).
- Escalar: novas identidades seguindo `skills/skill-rv-landing.md`.
