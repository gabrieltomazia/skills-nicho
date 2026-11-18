# Skills de nicho pro Claude Code

Duas skills que fazem a pesquisa e o roteiro do seu conteúdo:

| Skill | O que faz |
| --- | --- |
| **[viral-brand-analyst](./skills/viral-brand-analyst/SKILL.md)** | Lê os canais e perfis do seu nicho, compara cada vídeo com a média do próprio canal e te mostra o que tá bombando de verdade, o que já saturou e o que ninguém tá fazendo. Também desmonta um post que viralizou e explica por quê. |
| **[content-script-writer](./skills/content-script-writer/SKILL.md)** | Pega o que a primeira achou (ou qualquer ideia sua) e transforma no roteiro pronto pra gravar: fala palavra por palavra, tempo de cada parte, o que aparece na tela e legenda. |

Funcionam no **Claude Code** (terminal ou aba **Code** do app do Claude no
computador). Precisa da assinatura paga do Claude (Pro ou Max).

## Instalar

Abra o Claude Code e cole:

```text
Instala as duas skills desse repositório na minha pasta de skills do usuário
(.claude/skills): https://github.com/Synaptica24/skills-nicho
Cada pasta de dentro de skills/ tem que ficar direto em .claude/skills.
No fim, me mostra o que tem dentro de .claude/skills.
```

Tem Node? Também dá com um comando:

```bash
npx skills add Synaptica24/skills-nicho -g -a claude-code
```

Ou na mão: baixe o repositório (botão **Code → Download ZIP**) e copie as
pastas `skills/viral-brand-analyst` e `skills/content-script-writer` para
`.claude/skills/` dentro da sua pasta de usuário. O `SKILL.md` tem que ficar
direto dentro de cada pasta:

```text
.claude/skills/viral-brand-analyst/SKILL.md
.claude/skills/content-script-writer/SKILL.md
```

Depois abra uma conversa **nova** e digite `/viral`: tem que aparecer
`viral-brand-analyst`.

## Montar o seu perfil

1. Crie uma pasta só pro seu conteúdo.
2. Copie o [`perfil-modelo.md`](./perfil-modelo.md) pra lá e renomeie pra `perfil.md`.
3. Abra o Claude Code nessa pasta e peça: *"me entrevista pra preencher o
   perfil.md, uma pergunta de cada vez"*.

As duas skills leem esse arquivo antes de começar.

## Usar

```text
O que tá bombando no nicho de [SEU ASSUNTO] agora? Minhas referências são
[@conta1, @conta2, canal do YouTube X]. Compara cada vídeo com a média do
próprio canal e me diz o que tá funcionando, o que já saturou e o que ninguém
tá fazendo.
```

```text
Transforma a ideia 1 do relatório num roteiro de reel de 30 segundos.
```

## Opcional

- **Python:** puxa os números dos canais do YouTube sem login. Sem ele, a
  skill avisa e segue de outro jeito.
- **Extensão Claude in Chrome**, com o Chrome logado no Instagram e no
  TikTok: assim o Claude lê os números de lá também. No terminal, abra com
  `claude --chrome`. Sem ela, cole os links, prints e números na conversa.
