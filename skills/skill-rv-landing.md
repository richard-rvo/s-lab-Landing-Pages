---
name: rv-landing
description: Use ao criar landing pages e modelos de LP para a galeria S-LAB (público nutricionistas / profissionais de saúde). Entrega páginas single-file HTML, tokenizadas (camaleão), com 3 peles-preset (Clean/Médico, Editorial/Premium, Caloroso/Lifestyle), regras anti-genérico e estrutura de conversão embutida. Irmão do skill rv-design (este é para LANDING PAGES de cliente; o rv-design é para o hub/produto S-LAB).
---

# RV Landing — Sistema de Modelos de Landing Page

Fundação de **todos os modelos da galeria** de Landing Pages. O objetivo é que
um aluno sem experiência técnica baixe um HTML, troque ~5 variáveis (ou cole um
prompt) e tenha uma LP na marca dele que **não parece template de IA**.

## Quando usar

- Criar um modelo novo para a galeria (link-bio, WhatsApp, página de vendas…).
- Adaptar um modelo existente para outra pele/marca.
- Revisar uma LP para tirar o "AI look".

**Não** use para o hub/galeria em si (esse é marca S-LAB âmbar/glass → use o skill `rv-design`).

---

## 1. Os 3 pilares inegociáveis

1. **Single-file.** Um `.html` autocontido: CSS no `<head>`, ícones SVG inline,
   fontes via Google Fonts `<link>`. Zero build, zero bundler, zero dependência.
   O aluno baixa **um arquivo** → sobe no Netlify arrastando, ou cola no Codex.
2. **Camaleão (tokenização total).** Nenhuma cor ou fonte hardcoded fora do
   `:root`. Trocar ~5 variáveis vira a marca do aluno sem efeito colateral.
3. **Anti-genérico por regra, não por sorte.** O "foda" visual vem das regras
   da seção 4 — não de "gerar bonito". IA sozinha entrega o padrão ChatGPT
   (hero centralizado, Inter 400, gradiente roxo). As regras corrigem isso.

---

## 2. As 5 variáveis-camaleão (contrato de todo modelo)

Todo modelo expõe, no topo do `:root`, marcadas com `[TROCAR]`:

```css
:root {
  --brand:        #......;   /* cor principal (autoridade, CTAs, links) */
  --accent:       #......;   /* destaque humano — usar em ~5% do layout  */
  --paper:        #......;   /* fundo quente, NUNCA branco puro           */
  --font-display: "...";     /* títulos — fonte com personalidade         */
  --font-text:    "...";     /* corpo — legibilidade neutra               */
}
```

Tudo o mais (`--ink`, `--ink-2`, `--hairline`, sombras, raios) é **derivado** e
normalmente não se mexe. Regra de ouro: a cor de marca aparece **uma única vez**
no arquivo (no token); todo o resto é `var(--brand)`.

---

## 3. As 3 identidades (cor + tipografia + UX + VOZ)

A unidade de trabalho é a **identidade**, não o tipo de página: cada identidade é
uma marca completa que gera os 3 sites (`bio` / `whatsapp` / `vendas`) com a MESMA
cara e a MESMA voz. As 3 cobrem os 3 posicionamentos mais comuns de nutri. Escolha
pela persona — cor, fonte E tom de voz mudam juntos.

### 🟢 Identidade 1 · Verde Herbal — natural / funcional / leve
Persona-tipo: nutri comportamental, tom de amiga, anti-dieta (ex: Cami Brandão).
```css
--brand:#40583F; --accent:#C9893D; --paper:#F3F1E9;
--font-display:"Fraunces",Georgia,serif;        /* serif orgânica */
--font-text:"Nunito Sans",system-ui,sans-serif;
/* UX: orgânica, arredondada (20–28px), traços de folha, muito respiro */
```
**Voz:** calorosa, 2ª pessoa, encorajadora. Anti-dieta, sem terror nutricional.
Tira a culpa da paciente. *"Você não acorda sem força de vontade — o problema é o método."*

### 🟤 Identidade 2 · Terracota — feminino / premium / acolhedor
Persona-tipo: nutri hormonal feminina, ticket alto (ex: Dra. Helena Vasco).
```css
--brand:#B5654A; --accent:#3E5641; --paper:#F6F2EC;
--font-display:"DM Serif Display",Georgia,serif;
--font-text:"Inter",system-ui,sans-serif;
/* UX: editorial revista, arcos, raios refinados (~22px), 1 sombra quente */
```
**Voz:** científica-mas-humana, autoridade serena, investigativa.
*"Investigar a raiz, não silenciar o sintoma."*

### 🔵 Identidade 3 · Azul Clínico — científico / confiança / investigativo
Persona-tipo: nutri clínica/esportiva, baseada em exames (ex: Dra. Marina Reis).
```css
--brand:#2C6E7F; --accent:#DDA15E; --paper:#F1F4F5;
--font-display:"Archivo",system-ui,sans-serif;  /* grotesca técnica, 700–800 */
--font-text:"IBM Plex Sans",system-ui,sans-serif;
/* UX: grid estruturado, faixa de dados (3 stats), cantos mais retos (12–18px) */
```
**Voz:** precisa, baseada em dados e especificidade. Confiança pela medição.
*"Seu cansaço tem causa — e aparece nos seus exames."*

> **Regra de distinção:** as 3 cores-marca (verde / terracota / azul) precisam ser
> **dominantes** em sua identidade — não acentos. É o que mantém as 3 reconhecíveis.

---

## 4. Anti-genérico — alavancas em ordem de impacto

Aplique nesta ordem. Cada uma corrige um sintoma típico de IA.

1. **Tipografia com personalidade.** Par display + texto. Título peso 600–800,
   `letter-spacing: -0.02em a -0.04em`, `line-height` curto (0.95–1.05).
   Eyebrows/labels sempre em **mono UPPERCASE**, `letter-spacing` largo (~0.14em).
   *Nunca* Inter 400 como fonte de título.
2. **Espaço em branco agressivo.** IA enche; mandar esvaziar. Padding generoso,
   poucas coisas por tela, hierarquia clara. Respiro > densidade.
3. **Um movimento só.** UM gradiente OU um blob OU um reveal escalonado no load.
   Nunca os três. Sombra sempre com tint colorido (quente), **nunca cinza/preto**.
4. **Imagem real ou nenhuma.** Zero stock genérico. Retrato gerado por IA on-brand,
   ou monograma/composição. Stock corporativo mata a peça.
5. **Hierarquia brutal.** Headline grande de verdade: `clamp(32px, 6vw, 72px)` em
   LP; em link-bio menor. Um foco visual claro por tela.

Cheiro de "AI look" (corrigir na hora): roxo/azul genérico, branco puro `#FFF`,
sombra cinza dura, cantos retos, Inter em tudo, gradiente neon, hero perfeitamente
centralizado e simétrico em tudo, ícones emoji.

---

## 5. Estrutura de conversão (esqueleto)

A copy segue o AgentSkill de Copy (`agentskill-copy-lp-nutris.md`):
**headline → dor → oferta → prova → garantia → CTA.** O esqueleto de layout por tipo:

- **Link-bio:** retrato → nome → credencial → bio-assinatura → stack de 5 links
  (1 primário + 4 ghost) → card de oferta → sociais → rodapé. CTA = link primário.
- **LP de WhatsApp:** hero (headline + sub + 1 CTA) → 3 benefícios → como funciona
  (3 passos) → prova curta → CTA final. **Um só destino:** `wa.me` com mensagem
  pré-preenchida (`?text=`). Foco mono-CTA.
- **Página de vendas:** hero → dor/agitação → apresentação da solução → o que você
  recebe (módulos/itens) → prova (depoimentos) → bônus → **garantia** → oferta/preço
  → FAQ → CTA repetido. Estrutura longa, CTA aparece 2–3×.

---

## 6. Saúde — caveats obrigatórios (público nutri)

- **Nunca prometer resultado/cura/emagrecimento garantido.** Use "acompanhamento",
  "investigar a raiz", "cuidar de", "protocolo individualizado".
- Sempre exibir credencial (CRN) como placeholder visível.
- Depoimentos com tom realista; evitar "antes e depois" milagroso.
- Sem alegação terapêutica de suplemento/dieta.

---

## 7. Entrega técnica (checklist de aceite)

- [ ] Single-file, abre por duplo-clique, sem console error.
- [ ] Responsivo: testar viewport ~375px e largo.
- [ ] Fontes do Google carregam; fallback de sistema no token.
- [ ] `:root` com as 5 variáveis-camaleão marcadas `[TROCAR]`; cor de marca 1× só.
- [ ] Trocar `--brand` recolore a página inteira sem efeito colateral.
- [ ] Áreas de toque ≥44px; `alt` em imagens; `aria-label` em ícones-link.
- [ ] `prefers-reduced-motion` respeitado.
- [ ] Slots de conteúdo marcados `[TROCAR]`; `href` placeholders nomeados.
- [ ] Prompt de regeneração (arquivo irmão `.txt`) acompanha o modelo.
- [ ] **Teste-âmbar (subjetivo):** parece o site real de um profissional caro,
      não um template. Se parecer "padrão ChatGPT", voltar à seção 4.

---

## 8. Cada modelo entrega 3 artefatos

1. `modelo-*.html` — o single-file (na sua pele).
2. `prompt-regeneracao.txt` — o "copiar prompt" (design + estrutura + slots +
   restrições anti-genérico) + o prompt de imagem IA da persona.
3. Persona fictícia crível (nome, credencial, bio, oferta coerentes) para a peça
   parecer um site real na galeria — nunca um template vazio.
