# Modelo 1 — Link-na-bio · Nutri Clínica Funcional Premium

**Data:** 2026-06-22
**Status:** Aprovado para implementação
**Contexto maior:** Primeiro de 3 modelos do hub de Landing Pages para nutricionistas (aulão final IA na Prática, RV 2026). Ver `historico.md`.

---

## 1. Objetivo

Construir o **primeiro modelo ponta a ponta** da galeria: uma página de link-na-bio, mobile-first, single-file HTML, com a persona de uma nutricionista clínica funcional premium. Este modelo é o **padrão-ouro** — define a estrutura técnica, o formato do "copiar prompt" e o nível de acabamento que os outros 2 modelos (LP de WhatsApp, página de vendas de infoproduto) e o hub vão herdar.

### Por que link-na-bio primeiro
É o degrau mais simples da escada de complexidade de copy. Validar o padrão aqui (single-file, tokenização, prompt de regeneração, retrato IA) reduz risco antes de escalar para peças maiores.

### Fora de escopo (deste spec)
- O hub/galeria S-LAB que emoldura os modelos (spec próprio depois).
- Os outros 2 modelos (LP WhatsApp, página de vendas).
- Deploy real no Netlify e configuração de DNS (é conteúdo de aula, não artefato de código).

---

## 2. Persona

**Dra. Helena Vasco** — nutricionista clínica funcional.

- **Especialidade:** saúde hormonal e metabólica feminina.
- **Posicionamento:** ticket alto, poucos pacientes, abordagem investigativa ("a raiz, não o sintoma").
- **Tom de voz:** autoridade serena, científica mas humana.
- **Credencial exibida:** `CRN-3` (número fictício/placeholder visível, ex: `CRN-3 00000`).

A persona é fictícia mas crível: nome, especialidade, bio, links e oferta atual coerentes entre si, para que a peça pareça um site real na galeria — não um template vazio.

---

## 3. Identidade visual

Identidade **própria do modelo** — deliberadamente NÃO é a marca âmbar/glassmorphism do S-LAB (essa fica reservada ao hub).

### Paleta (tokens)
| Token | Valor | Uso |
|---|---|---|
| `--paper` | `#F6F2EC` | fundo marfim quente (nunca branco puro) |
| `--paper-2` | `#EDE7DD` | superfícies/cards levemente recuados |
| `--brand` | `#3E5641` | sage profundo — acento principal (links, autoridade) |
| `--brand-soft` | `#5A7560` | sage claro — hovers, detalhes |
| `--accent` | `#B5654A` | terracota — destaque humano, uso parcimonioso (~5% do layout) |
| `--ink` | `#2A2622` | grafite quente — texto principal |
| `--ink-2` | `#5C554E` | texto secundário |
| `--hairline` | `rgba(42,38,34,0.10)` | divisórias finas |

### Tipografia
- **Display (nome, títulos):** `DM Serif Display` — ar editorial caro.
- **Texto (corpo, links, bio):** `Inter` — legibilidade neutra. Bio em itálico para tom editorial.
- **Mono (labels, credencial, eyebrows):** `JetBrains Mono` — UPPERCASE, letter-spacing largo.

### Acabamento
- Espaço em branco generoso (anti-padrão IA: não encher).
- Raios refinados: cards ~20px, botões/links ~16px, retrato em arco/oval suave. Nada de squircle exagerado.
- Uma única sombra suave com tint quente (sem cinza duro, sem sombra preta).
- **Um movimento só:** fade/slide-up suave dos elementos no load. Sem gradiente neon, sem blobs animados.

---

## 4. Estrutura da página

Mobile-first (link-bio vive no celular, acessado pelo Instagram), elegante também no desktop (conteúdo centralizado, largura máx. confortável ~480px num cartão sobre o marfim).

Ordem vertical:

1. **Retrato** — foto editorial da Dra. Helena, recorte em arco/oval suave.
2. **Nome** — `DRA. HELENA VASCO` em DM Serif Display.
3. **Credencial** — label mono: `CRN-3 00000 · NUTRIÇÃO FUNCIONAL`.
4. **Bio editorial** — 1–2 linhas, Inter itálico: *"Investigo a raiz, não trato o sintoma."* (frase-assinatura).
5. **Stack de links** — botões empilhados, full-width:
   1. **Agendar consulta** — link primário, destaque sage (preenchido).
   2. **WhatsApp** — secundário (contorno/ghost).
   3. **Materiais & ebook** — secundário.
   4. **Instagram** — secundário.
   5. **Artigos / blog** — secundário.
6. **Card de destaque** — oferta atual, ex: *"Vagas de junho abertas — 6 pacientes/mês"* com micro-CTA. Usa o terracota como acento.
7. **Ícones sociais** — linha de ícones (Instagram, e-mail, WhatsApp).
8. **Rodapé discreto** — assinatura/crédito, mono pequeno.

Todos os `href` são placeholders óbvios e bem nomeados (`#agendar`, `https://wa.me/55...`, etc.) para o aluno trocar.

---

## 5. Tokenização (camaleão)

Bloco `:root` único concentra tudo que o aluno troca para virar a marca dele — meta de **~5 variáveis principais**:

- `--brand` (cor principal)
- `--accent` (cor de destaque)
- `--font-display` e `--font-text` (fontes)
- `--paper` (fundo)

Mais os dados de conteúdo editáveis diretamente no HTML (nome, credencial, bio, textos dos links, oferta). Nenhuma cor ou fonte hardcoded fora do `:root`. Conecta com a decisão "camáleão" do briefing e com o Agent 1 (Identidade Visual).

---

## 6. Entrega técnica

- **Single-file `.html`** autocontido: CSS inline no `<head>`, ícones via SVG inline (sem dependência de biblioteca de ícones), fontes via `<link>` do Google Fonts. Zero build, zero bundler.
- Baixa um arquivo só → sobe direto no Netlify (arrastar/soltar) **ou** cola no app do Codex para personalizar.
- **Responsivo:** desenhado para o celular; no desktop o conteúdo aparece centralizado num cartão confortável sobre o fundo marfim.
- **Acessibilidade básica:** contraste adequado (sage/grafite sobre marfim), `alt` no retrato, áreas de toque ≥44px nos links.

---

## 7. Retrato da persona (imagem IA)

Retrato editorial gerado por IA da "Dra. Helena Vasco", on-brand com a paleta do modelo (marfim/sage, luz difusa quente). Base de prompt adaptada do bloco de DNA visual do `SKILL.md`, ajustada para retrato profissional de nutricionista:

- Mulher profissional, ~35–45 anos, expressão serena e confiável, vestuário neutro/clínico discreto.
- Fundo marfim quente desfocado, luz suave difusa, paleta sage/terracota sutil.
- Estilo editorial limpo, sem texto, sem watermark, sem cores oversaturadas.

A imagem é salva localmente e referenciada no single-file (ou embutida como base64 se for necessário manter "um arquivo só" 100% portátil — decisão de implementação).

---

## 8. "Copiar prompt" (regeneração via Codex)

Cada modelo carrega um **prompt estruturado** (texto), pronto para colar no app do Codex, que permite ao aluno regenerar a página com os dados dele **sem quebrar o layout**. O prompt deve conter:

1. Descrição do sistema de design do modelo (paleta tokenizada, tipografia, acabamento).
2. A estrutura da página (as 8 seções acima).
3. Slots explícitos dos dados do aluno (nome, credencial, bio, 5 links, oferta, cor de marca, fonte).
4. Restrições anti-genérico (manter espaço em branco, não adicionar gradiente neon, manter single-file).

Neste spec o prompt é entregue como um bloco de texto versionado junto ao modelo (ex: comentário no topo do HTML e/ou arquivo `.txt` irmão). A mecânica de "copiar" no hub fica para o spec do hub.

---

## 9. Validação

Aceite do modelo quando:

- Abre corretamente no navegador em **mobile e desktop** (testar em viewport estreito ~375px e largo).
- Fontes do Google carregam; fallback de sistema definido.
- Todos os links presentes, com placeholders nomeados e clicáveis.
- Tokens isolados no `:root`; trocar `--brand` muda o acento em toda a página sem efeitos colaterais.
- Retrato carrega com `alt`.
- **Teste subjetivo (o "teste-âmbar"):** parece o site real de uma nutricionista cara — não um template. Espaço em branco respeitado, hierarquia tipográfica forte, um único movimento.

---

## 10. Artefatos produzidos

1. `modelo-1-link-bio-helena.html` — o modelo single-file.
2. Retrato IA da persona (imagem ou base64 embutido).
3. Prompt de regeneração (bloco de texto / arquivo irmão).
