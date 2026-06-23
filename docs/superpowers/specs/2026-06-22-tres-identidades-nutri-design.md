# 3 Identidades Visuais de Nutri × 3 Sites — Design

**Data:** 2026-06-22
**Status:** Aprovado para implementação
**Contexto:** Evolução da galeria de Landing Pages (ver `historico.md` e o spec
do Modelo 1). A unidade de trabalho deixa de ser "tipo de página" e passa a ser
a **identidade visual completa**: cada identidade é uma marca (cor + tipografia +
UX + voz própria) e gera os **3 sites** do funil — link na bio, captação de leads e vendas.

---

## 1. Objetivo

Entregar **3 identidades de nutricionista genérica**, cada uma com os 3 sites,
totalizando **9 páginas single-file**. Cada identidade tem uma **forma de
comunicação distinta**, coerente com o estilo daquela nutri imaginária. Corrigir
o problema da v1 (peles espalhadas entre tipos de página, sem marca coerente) e
reescrever toda a copy com frameworks de marketing, sem vícios de IA.

## 2. As 3 identidades

### 🟢 Verde Herbal — natural / funcional / leve
- **Persona:** Cami Brandão, nutri comportamental; tom de amiga, anti-dieta.
- **Cor:** `--brand #40583F` (sage) · `--accent #C9893D` (mel) · `--paper #F3F1E9`.
- **Tipografia:** Fraunces (display, serif orgânica) + Nunito Sans (texto).
- **UX:** orgânico, arredondado (raios 20–28px), arejado, traços de folha, muito respiro.
- **Voz:** calorosa, 2ª pessoa, encorajadora. Linguagem de comida real, sem terror nutricional.

### 🟤 Terracota — feminino / premium / acolhedor
- **Persona:** Dra. Helena Vasco, saúde hormonal feminina; ticket alto.
- **Cor:** `--brand #B5654A` (terracota) · `--accent #3E5641` (sage) · `--paper #F6F2EC` (marfim).
- **Tipografia:** DM Serif Display + Inter.
- **UX:** editorial revista, elegância assimétrica, arcos, sombra quente única.
- **Voz:** científica-mas-humana, investigativa, autoridade serena.

### 🔵 Azul Clínico — científico / confiança / investigativo
- **Persona:** Dra. Marina Reis, nutri clínica e esportiva; baseada em exames.
- **Cor:** `--brand #2C6E7F` (azul-petróleo quente) · `--accent #DDA15E` (âmbar) · `--paper #F1F4F5`.
- **Tipografia:** Archivo (display, grotesca técnica) + IBM Plex Sans (texto).
- **UX:** estruturado em grid, blocos de números/dados, linhas precisas, clínico moderno.
- **Voz:** precisa, baseada em dados e especificidade, confiança sem promessa.

## 3. Estrutura por tipo de site (compartilhada entre identidades)

- **bio.html** — retrato/monograma → nome → credencial → bio-assinatura → 5 links
  (1 primário + 4 ghost) → card de oferta → sociais → rodapé. CTA = link primário.
- **captura-leads.html** — hero (headline + sub + CTA WhatsApp) → 3 benefícios → como
  funciona (3 passos) → prova → CTA final + FAB. Mono-CTA `wa.me?text=`.
- **vendas.html** — nav → hero → dor (PAS) → solução → o que recebe (módulos) →
  prova → bônus → garantia → preço → FAQ (`<details>`) → CTA. Estrutura longa.

Cada site adapta a estrutura à **voz e UX da sua identidade** (não é o mesmo
layout pintado de cor diferente — muda ritmo, hierarquia e tom).

## 4. Copy — frameworks e regras

- **PAS** (Problema-Agitação-Solução) e **Before-After-Bridge** na espinha.
- **Especificidade concreta** (números, situações nomeadas) e **voz do cliente**.
- **Quebra de objeção** + **inversão de risco** (garantia) nas páginas de vendas.
- Headline puxa **resultado/curiosidade**, nunca o método.
- **Anti-IA:** sem "transforme/jornada/equilíbrio" vazios, sem cliché "não é X é Y"
  repetido, sem tríades simétricas, sem benefício vago.
- **Saúde (obrigatório):** sem promessa de cura/emagrecimento/quilos; CRN sempre
  visível; depoimentos realistas marcados `(confirme)`; disclaimer nas vendas.

## 5. Técnico (herdado do skill rv-landing)

- Single-file, CSS no `<head>`, SVG inline, fontes Google. Zero build.
- Camaleão: 5 vars no `:root` (`--brand`,`--accent`,`--paper`,`--font-display`,
  `--font-text`); cor de marca aparece 1× por arquivo.
- Um movimento só (reveal escalonado) + `prefers-reduced-motion`.
- A11y: `alt`, `aria-label` em ícones-link, áreas de toque ≥44px, viewport mobile.

## 6. Organização e hub

```
identidades/
├── 01-verde-herbal/  bio.html captura-leads.html vendas.html prompts-regeneracao.txt
├── 02-terracota/     bio.html captura-leads.html vendas.html prompts-regeneracao.txt
└── 03-azul-clinico/  bio.html captura-leads.html vendas.html prompts-regeneracao.txt
hub/index.html        agrupado POR identidade (3 marcas → 9 sites), Baixar HTML + Copiar prompt
```
- A pasta `modelos/` da v1 é **substituída** por `identidades/` (conteúdo superado).
- `skill-rv-landing.md` e `agentskill-copy-lp-nutris.md` atualizados: as 3 peles
  viram as 3 identidades, cada uma com voz própria.

## 7. Validação (aceite)

Script automatizado confirma, para os 9 arquivos: 5 vars-camaleão isoladas; cor
de marca 1×; sem hex de paleta fora do `:root` (neutros ok); um único `@keyframes`
+ reduced-motion; `alt`/`aria-label`/viewport; CRN presente; sem promessa proibida;
tags balanceadas. Hub: aponta para os 9 arquivos existentes, 9 prompts embutidos,
download + copy com fallback, JS sem erro de sintaxe. Mais teste-âmbar subjetivo
(parece marca real, não template).
